from pypdf import PdfReader

def extract_text(filepath: str) -> str:
    try:
        reader = PdfReader(filepath)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    except Exception as e:
        return f"Error: {e}"

def detect_language(text: str) -> str:
    arabic = sum(1 for c in text if '\u0600' <= c <= '\u06FF')
    latin = sum(1 for c in text if c.isalpha() and ord(c) < 128)
    if arabic > latin:
        return "ar"
    if latin > 0:
        return "en"
    return "unknown"

def classify_document(text: str) -> str:
    t = text.lower()
    if "invoice" in t or "vat" in t or "amount due" in t:
        return "invoice"
    if "contract" in t or "agreement" in t:
        return "contract"
    if "passport" in t or "national id" in t or "iqama" in t:
        return "identity"
    if "policy" in t or "regulation" in t:
        return "policy"
    return "general"