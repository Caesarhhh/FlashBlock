from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

VIDEO_ROOT = "demo_videos"

@app.get("/api/categories")
def list_categories():
    return sorted([
        d for d in os.listdir(VIDEO_ROOT)
        if os.path.isdir(os.path.join(VIDEO_ROOT, d))
    ])

@app.get("/api/videos/{category}")
def list_videos(category: str):
    baseline_dir = os.path.join(VIDEO_ROOT, category, "baseline")
    if not os.path.exists(baseline_dir):
        return []
    return sorted([
        f for f in os.listdir(baseline_dir)
        if f.lower().endswith((".mp4", ".webm", ".ogg"))
    ])

# expose video files
app.mount("/videos", StaticFiles(directory=VIDEO_ROOT), name="videos")

# expose frontend
app.mount("/", StaticFiles(directory=".", html=True), name="static")
