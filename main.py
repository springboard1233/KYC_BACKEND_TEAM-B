import pandas as pd
from src.generator import generate_fake_aadhar_data, create_aadhar_card_image
from src.ocr_reader import extract_from_image
from src.cleaner import clean_dataframe

# Example: Generate one fake Aadhaar card
data = generate_fake_aadhar_data()
create_aadhar_card_image(data, filename="data/fake_aadhaar.png")

# OCR process on sample images
image_paths = [
    "data/aadhaar_sample_1.png",
    "data/aadhaar_sample_2.png",
    "data/aadhaar_sample_3.png",
    "data/aadhaar_sample_4.png",
    "data/aadhaar_sample_5.png"
]

records = [extract_from_image(path) for path in image_paths]

# Convert to DataFrame
df = pd.DataFrame(records)

# Clean & Standardize
df = clean_dataframe(df)

# Save results
df.to_csv("output/final_aadhaar_data.csv", index=False, encoding="utf-8")
df.to_json("output/final_aadhaar_data.json", orient="records", indent=4)

print("✅ Final dataset saved in 'output/' folder")
print(df)
