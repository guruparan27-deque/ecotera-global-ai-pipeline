import requests

URL = "https://zenodo.org/api/records/13881899"

response = requests.get(URL)
data = response.json()

file_info = data["files"][0]

print("Filename:", file_info["key"])
print("Download URL:", file_info["links"]["self"])