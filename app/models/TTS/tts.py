from pydantic import BaseModel
from app.models.TTS.voice import Voice
from uuid import uuid4
from app.setup.config import TTS_LANGUAGE
class GenerateTTSRequest():
    text: str
    voice_name : Voice
    save: bool
    filename: str
    language: str
    def __init__(self, text: str, voice_name: Voice, save: bool):
        self.text = text
        self.voice_name = voice_name
        self.save = save
        self.filename = "./media/" + str(uuid4()) + ".wav"
        self.language = TTS_LANGUAGE



    



