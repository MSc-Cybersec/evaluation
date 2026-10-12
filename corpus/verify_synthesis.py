"""
Regenerates the synthesis claims of the dissertation from the published mapping
manifest alone:

  1. Measured synthesis characteristics  -> Table 5.6
  2. Citation integrity by framework     -> Table H.1
  3. Risk and category distribution      -> Appendix H.4
  4. ISO/IEC 27001 reverse coverage      -> Appendix H.11

Run from the replication-package root:

    python corpus/verify_synthesis.py

The manifest carries record identifiers, domains, risk, category and framework
control identifiers only. The corpus itself is withheld (Appendix F); none of
the measures below depends on its normative text.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from statistics import mean, median

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "mapping_manifest.json"

# ISO/IEC 27001:2022 Annex A is a closed set of 93 controls.
ISO_27001 = ({f"A.5.{i}" for i in range(1, 38)} | {f"A.6.{i}" for i in range(1, 9)}
             | {f"A.7.{i}" for i in range(1, 15)} | {f"A.8.{i}" for i in range(1, 35)})
NIST_FAMILIES = set("AC AT AU CA CM CP IA IR MA MP PE PL PM PS PT RA SA SC SI SR".split())
CSF_FUNCTIONS = set("GV ID PR DE RS RC".split())

SCHEMES = {
    "nist": re.compile(r"^[A-Z]{2}-\d+(\(\d+\))?$"),
    "nist_csf": re.compile(r"^[A-Z]{2}\.[A-Z]{2}-\d{2}$"),
    "iso_27001": re.compile(r"^A\.\d+\.\d+$"),
    "cobit_2019": re.compile(r"^[A-Z]{3}\d{2}\.\d{2}$"),
    "cwe": re.compile(r"^CWE-\d+$"),
}
LABELS = {
    "nist": "NIST SP 800-53 Rev. 5",
    "iso_27001": "ISO/IEC 27001:2022",
    "nist_csf": "NIST CSF 2.0",
    "cobit_2019": "COBIT 2019",
    "cwe": "CWE",
}
ENUMERABLE = {"nist", "iso_27001", "nist_csf"}


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    corpus = data["corpus"]

    per_record = [len(r["mappings"]) for r in corpus]
    refs = [sum(len(v) for v in r["mappings"].values()) for r in corpus]
    pairs = {f"{fw}::{cid}" for r in corpus
             for fw, ids in r["mappings"].items() for cid in ids}

    print("Table 5.6 - Measured synthesis characteristics")
    print(f"  {'Governance records':<46}{len(corpus):>8}")
    print(f"  {'Record-to-framework mappings':<46}{sum(per_record):>8}")
    print(f"  {'Mean frameworks discharged per record':<46}{mean(per_record):>8.2f}")
    print(f"  {'Median frameworks per record':<46}{median(per_record):>8.0f}")
    print(f"  {'Range (minimum - maximum)':<46}{min(per_record):>5} - {max(per_record)}")
    print(f"  {'Control-level references across all records':<46}{sum(refs):>8}")
    print(f"  {'Distinct framework-control pairs referenced':<46}{len(pairs):>8}")
    print(f"  {'Mean control references per record':<46}{mean(refs):>8.1f}")
    # Appendix H.3 counts domains by record-identifier prefix, not by the
    # human-readable domain label; both are reported.
    prefixes = {r["id"].split("-")[0] for r in corpus if r.get("id")}
    print(f"  {'Distinct domains (record-identifier prefix)':<46}{len(prefixes):>8}")
    print(f"  {'Distinct domain labels':<46}{len({r['domain'] for r in corpus}):>8}")
    print(f"  {'Distinct frameworks':<46}"
          f"{len({fw for r in corpus for fw in r['mappings']}):>8}\n")

    print("Table H.1 - Citation integrity by framework")
    print(f"  {'Framework':<24}{'refs':>7}{'distinct':>10}{'conforming':>12}{'outside':>9}")
    for key, scheme in SCHEMES.items():
        ids = [cid for r in corpus for cid in r["mappings"].get(key, [])]
        if not ids:
            continue
        distinct = set(ids)
        ok = sum(1 for cid in ids if scheme.match(cid))
        if key == "iso_27001":
            outside = sum(1 for cid in distinct if scheme.match(cid) and cid not in ISO_27001)
        elif key == "nist":
            outside = sum(1 for cid in distinct
                          if scheme.match(cid) and cid.split("-")[0] not in NIST_FAMILIES)
        elif key == "nist_csf":
            outside = sum(1 for cid in distinct
                          if scheme.match(cid) and cid.split(".")[0] not in CSF_FUNCTIONS)
        else:
            outside = None
        shown = str(outside) if key in ENUMERABLE else "n/e"
        print(f"  {LABELS[key]:<24}{len(ids):>7}{len(distinct):>10}"
              f"{ok / len(ids) * 100:>11.1f}%{shown:>9}")

    iso_cited = {cid for r in corpus for cid in r["mappings"].get("iso_27001", [])}
    mapped = iso_cited & ISO_27001
    print(f"\n  ISO/IEC 27001 reverse coverage: {len(mapped)} of {len(ISO_27001)} "
          f"Annex A controls mapped, {len(ISO_27001) - len(mapped)} unmapped\n")

    print("Appendix H.4 - Distribution by risk and implementation category")
    for label, counter in (("risk", Counter(r["risk"] for r in corpus)),
                           ("category", Counter(r["category"] for r in corpus))):
        for name, n in counter.most_common():
            print(f"  {label:<10}{str(name):<28}{n:>5}")


if __name__ == "__main__":
    main()
