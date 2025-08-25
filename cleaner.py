import re
import pandas as pd

def clean_dataframe(df):
    df['Name'] = df['Name'].str.strip().str.title()
    df['Aadhaar Number'] = df['Aadhaar Number'].str.replace(r"\D", "", regex=True)
    df['Address'] = df['Address'].str.replace(r'\s+', ' ', regex=True).str.strip()
    df['Valid Aadhaar'] = df['Aadhaar Number'].apply(lambda x: len(x) == 12)
    df['Address'] = df['Address'].apply(standardize_address)
    return df

def standardize_address(addr):
    if not addr:
        return ""
    addr = re.sub(r"\bRd\.?\b", "Road", addr, flags=re.IGNORECASE)
    addr = re.sub(r"\bSt\.?\b", "Street", addr, flags=re.IGNORECASE)
    addr = re.sub(r"\bAve\.?\b", "Avenue", addr, flags=re.IGNORECASE)
    addr = re.sub(r"[^A-Za-z0-9\s,./#-]", "", addr)
    addr = re.sub(r"\b(\d{3})\s?(\d{3})\b", r"\1\2", addr)
    return addr.strip()
