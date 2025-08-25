from faker import Faker
from PIL import Image, ImageDraw, ImageFont
import random

fake = Faker("en_IN")

def generate_fake_aadhar_data():
    aadhaar_number = " ".join(
        ["".join([str(random.randint(0, 9)) for _ in range(4)]) for _ in range(3)]
    )
    return {
        "Name": fake.name(),
        "Gender": random.choice(["Male", "Female"]),
        "DOB": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%d-%m-%Y"),
        "Aadhaar Number": aadhaar_number,
        "Address": fake.address().replace("\n", ", "),
    }

def create_aadhar_card_image(data, filename="aadhaar_style.png"):
    img = Image.new("RGB", (600, 350), "white")
    draw = ImageDraw.Draw(img)

    font = ImageFont.load_default()
    draw.text((200, 20), "Government of India", fill="black", font=font)
    draw.text((30, 70), f"Name: {data['Name']}", fill="black", font=font)
    draw.text((30, 100), f"Gender: {data['Gender']}", fill="black", font=font)
    draw.text((30, 130), f"DOB: {data['DOB']}", fill="black", font=font)
    draw.text((30, 160), f"Aadhaar No: {data['Aadhaar Number']}", fill="black", font=font)
    draw.text((30, 200), f"Address: {data['Address']}", fill="black", font=font)

    img.save(filename)
    return filename
