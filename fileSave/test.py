import requests

url = "http://127.0.0.1:8000/"
file_path = "fileSave\doc.pdf"

with open(file_path, "rb") as file:
    response = requests.post(url, files={"file": file})

print(response.status_code)
print(response.json())
