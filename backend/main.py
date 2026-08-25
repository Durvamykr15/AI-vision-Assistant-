from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="AI Vision Assistant API",
    description="Backend API for the AI Vision Assistant project.",
    version="0.1.0",
)


# Allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "AI Vision Assistant API is running",
        "status": "ok",
    }


@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "Image received successfully. AI analysis will be connected next.",
    }