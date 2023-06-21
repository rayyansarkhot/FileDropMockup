from fastapi import FastAPI, UploadFile, File

app = FastAPI(
    max_request_size=100 * 1024 * 1024,  # 100 MB
    max_response_size=100 * 1024 * 1024  # 100 MB
    )

@app.post("/")
async def upload_file(file: UploadFile = File(...)):
    print(file)
    file_path = f"saves\{file.filename}"  # Specify the desired save location
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"filename": file.filename, "saved_path": file_path}
