from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import fitz
import os
from chatgpt_processing import date_response, contact_response, delivery_response, commodity_response

print(date_response)

# create instance of FastAPI() class to represent your web app
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# define route
# function defines what happens when parameter is hit
@app.post("/")

# save dropped file
async def save_file(file: UploadFile = File(...)):

    print(file)
    file_path = f"saves/{file.filename}"  # Specify the desired save location
    with open(file_path, "wb") as f:
        f.write(await file.read())
    

    return {"filename": file.filename, "message": "File uploaded successfully"}

    count = 0
    output_file_prefix = "output_file_" 

    # Create a new folder
    folder_path = "./textfiles"
    os.makedirs(folder_path, exist_ok=True)

    filename = file.filename
    file_path = f'./saves/{filename}.pdf'

    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        current_page=page.get_text()
        # Save text as a numbered text file in the new folder
        with open(os.path.join(folder_path, "output_file_{}.txt".format(count)), "w", encoding="utf-8") as file:
            file.write(current_page)
            count += 1