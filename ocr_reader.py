import easyocr
import re

# Initialize OCR reader (only once for performance)
reader = easyocr.Reader(['en'])

# -------------------------
# Regex Patterns
# -------------------------
aadhaar_pattern = r"\b\d{4}\s\d{4}\s\d{4}\b"
pan_pattern = r"[A-Z]{5}[0-9]{4}[A-Z]{1}"   # PAN format: ABCDE1234F
name_pattern = r"(?:Name|NAME)[:\s]*([A-Za-z ]{3,})"
address_pattern = r"(?:Address|ADDRESS)[:\s]*([A-Za-z0-9/.,\-\s]+?\d{6})"


# -------------------------
# OCR Extraction Function
# -------------------------
def extract_from_image(img_path: str) -> dict:
    """
    Extracts structured information from Aadhaar/PAN or other KYC documents.
    Returns JSON-friendly dictionary with raw text + fields.
    """
    try:
        # Run OCR
        results = reader.readtext(img_path, detail=0)
        text = "\n".join(results)

        # Aadhaar
        aadhaar_number = re.search(aadhaar_pattern, text)
        aadhaar_number = aadhaar_number.group() if aadhaar_number else ""

        # PAN
        pan_number = re.search(pan_pattern, text)
        pan_number = pan_number.group() if pan_number else ""

        # Name
        name = re.search(name_pattern, text, re.IGNORECASE)
        name = name.group(1).strip() if name else ""

        # Address
        address = re.search(address_pattern, text, re.IGNORECASE)
        address = address.group(1).strip() if address else ""

        # Detect document type
        if aadhaar_number:
            doc_type = "Aadhaar Card"
        elif pan_number:
            doc_type = "PAN Card"
        else:
            doc_type = "Unknown Document"

        return {
            "Document Type": doc_type,
            "Name": name,
            "Aadhaar Number": aadhaar_number,
            "PAN Number": pan_number,
            "Address": address,
            "Raw OCR Text": text
        }

    except Exception as e:
        return {"error": str(e), "message": "OCR extraction failed"}
