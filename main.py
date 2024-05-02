from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import conversation_router, summary_router, podcast_router, learning_router

from pathlib import Path
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_credentials=True,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
)

app.mount("/media", StaticFiles(directory=Path('media')), name="media")

@app.get("/", tags=["StormingAI"])
async def storming_ai():
    return {"message": "StormingAI in Google AI Hackathon from Algeria!"}

app.include_router(conversation_router.router, prefix="/conversation", tags=["Conversation"])
app.include_router(summary_router.router, prefix="/summary", tags=["Summary"])
# app.include_router(podcast_router.router, prefix="/podcast", tags=["Podcast"])
app.include_router(learning_router.router, prefix="/learning", tags=["Learning"])