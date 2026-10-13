import re

PII_PATTERNS = {
    "saudi_id": r"\b[12]\d{9}\b",
    "iban": r"\bSA\d{22}\b",
    "phone": r"\b(?:\+966|0)5\d{8}\b",
    "email": r"\b[\w.-]+@[\w.-]+\.\w+\b",
}

def detect_pii(text: str) -> dict:
    found = {}
    for name, pattern in PII_PATTERNS.items():
        found[name] = list(set(re.findall(pattern, text, flags=re.IGNORECASE)))
    return found

def mask_pii(text: str) -> str:
    for name, pattern in PII_PATTERNS.items():
        text = re.sub(pattern, f"[{name.upper()}_HIDDEN]", text, flags=re.IGNORECASE)
    return text