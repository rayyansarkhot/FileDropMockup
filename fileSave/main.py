from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"saves\{file.filename}"  # Specify the desired save location
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"filename": file.filename, "saved_path": file_path}
