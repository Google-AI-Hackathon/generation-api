from pydantic import BaseModel
from app.setup.config import TTS_LANGUAGE

from app.models.TTS.voice import Voice

class TTSRequest(BaseModel):
    text: str
    voice_name: Voice
    language: str = TTS_LANGUAGE