from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fitz import fitz
import os
import shutil

# create instance of FastAPI() class to represent your web app
app = FastAPI()



# define route
# function defines what happens when parameter is hit
@app.post("/")

# save dropped file
async def save_file(file: UploadFile = File(...)):

    print(file)
    file_path = f"saves/{file.filename.replace(' ', '_')}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    count = 0

    # Create a new folder
    folder_path = "./textfiles"

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.rmdir(dir_path)

    os.makedirs(folder_path, exist_ok=True)

    doc = fitz.open(file_path)
    for page in doc:
        current_page=page.get_text()
        # Save text as a numbered text file in the new folder
        with open(os.path.join(folder_path, "output_file_{}.txt".format(count)), "w", encoding="utf-8") as file:
            file.write(current_page)
            count += 1
    from chat import date_response, contact_response, delivery_response, commodity_response

    print(date_response, contact_response, delivery_response, commodity_response)
    return[date_response, contact_response, delivery_response, commodity_response]

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://localhost:1000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

