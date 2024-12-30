from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CreateFileRequest(BaseModel):
    filename: str


@app.post("/create")
async def create_file(request: CreateFileRequest):
    filepath = f"/files/{request.filename}"
    try:
        with open(filepath, "w") as file:
            pass
        return {"message": "File created successfully", "filename": request.filename}
    except Exception as e:
        return {"error": str(e)}
