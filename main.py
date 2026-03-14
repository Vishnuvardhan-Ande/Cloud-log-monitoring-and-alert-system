from fastapi import FastAPI, UploadFile, File
from log_analyzer import analyze_logs
from fastapi.middleware.cors import CORSMiddleware
from email_alert import send_alert

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

latest_stats = {}

@app.get("/")
def home():
    return {"message": "Cloud Log Monitoring System"}

@app.post("/upload-log")
async def upload_log(file: UploadFile = File(...)):
    global latest_stats

    content = await file.read()
    text = content.decode("utf-8")

    stats = analyze_logs(text)
    latest_stats = stats

    if stats["ERROR"] > 0 or stats["CRITICAL"] > 0:
        send_alert("Critical error detected in uploaded log file")

    return {
        "log_statistics": stats
    }


@app.get("/dashboard")
def dashboard():
    return {
        "latest_log_statistics": latest_stats
    }