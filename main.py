from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import conversation_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    # allow_credentials=True,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
)

@app.get("/")
async def root():
    return {"message": "Google AI Hackathon from Algeria!"}

app.include_router(conversation_router.router, prefix="/conversations", tags=["conversations"])