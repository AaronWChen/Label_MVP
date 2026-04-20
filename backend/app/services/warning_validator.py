import re
from rapidfuzz import fuzz

REQUIRED_PREFIX = "GOVERNMENT WARNING:"


def normalize(t):
    return re.sub(r"\s+", " ", t).strip()


def validate_warning(text: str):
    result = {"is_valid": False, "issues": []}

    match = re.search(r"GOVERNMENT WARNING:.*", text, re.DOTALL)

    if not match:
        result["issues"].append("Missing GOVERNMENT WARNING")
        return result

    warning = match.group(0)

    if not warning.startswith(REQUIRED_PREFIX):
        result["issues"].append("Prefix incorrect")

    if warning[:len(REQUIRED_PREFIX)] != warning[:len(REQUIRED_PREFIX)].upper():
        result["issues"].append("Must be ALL CAPS")

    score = fuzz.partial_ratio(normalize(warning), normalize(REQUIRED_PREFIX))

    if score < 80:
        result["issues"].append("Text mismatch")

    result["is_valid"] = len(result["issues"]) == 0
    return result
