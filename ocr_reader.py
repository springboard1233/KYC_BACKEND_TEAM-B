import easyocr
import re

reader = easyocr.Reader(['en'])

aadhaar_pattern = r"\b\d{4}\s\d{4}\s\d{4}\b"
name_pattern = r"Name[:\s]*([A-Z ]+)"
address_pattern = r"Address[:\s]*([A-Za-z0-9/.,\-\s]+?\d{6})"

def extract_from_image(img_path):
    results = reader.readtext(img_path, detail=0)
    text = "\n".join(results)

    aadhaar_number = re.search(aadhaar_pattern, text)
    aadhaar_number = aadhaar_number.group() if aadhaar_number else ""

    name = re.search(name_pattern, text, re.IGNORECASE)
    name = name.group(1).strip() if name else ""

    address = re.search(address_pattern, text, re.IGNORECASE)
    address = address.group(1).strip() if address else ""

    return {
        "Document Type": "Aadhaar Card",
        "Name": name,
        "Aadhaar Number": aadhaar_number,
        "Address": address
    }
