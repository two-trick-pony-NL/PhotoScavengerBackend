from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    print(UploadFile)
    return {"filename": file.filename}