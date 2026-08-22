import requests

URL = (
    "https://www.waterqualitydata.us/data/Result/search?"
    "characteristicName=Dissolved%20oxygen"
    "&mimeType=csv"
    "&dataProfile=fullPhysChem"
    "&zip=no"
)

response = requests.get(URL)

print("Status:", response.status_code)

with open("data/raw/wqp_raw.csv", "wb") as file:
    file.write(response.content)

print("Saved to data/raw/wqp_raw.csv")