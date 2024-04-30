import json
from uuid import uuid4

import google.cloud.texttospeech as tts
from google.cloud.texttospeech import TextToSpeechClient
from app.models.tts.tts import TTSRequest
from app.models.tts.voice import Voice

from app.setup.config import TTS_LANGUAGE
from app.setup.creds import set_google_application_credentials

set_google_application_credentials()
client = TextToSpeechClient()

def list_voices(language_code: str = TTS_LANGUAGE, save: bool = False):
    response = client.list_voices(language_code=language_code)
    voices = sorted(response.voices, key=lambda voice: voice.name)
    if save:
        save_list_voices(voices)
    return voices

def save_list_voices(voices):
    saved_voices = [{'name':voice.name, 'ssml_gender':voice.ssml_gender} for voice in voices]
    with open('app/data/voices/voices.json', 'w') as f:
        json.dump(saved_voices, f, indent=4)

def synthesize_text(params: TTSRequest, save: bool = False):
    synthesis_input = tts.SynthesisInput(text=params.text)
    voice = tts.VoiceSelectionParams(
        language_code=params.language, name=params.voice_name.name
    )
    audio_config = tts.AudioConfig(
        audio_encoding=tts.AudioEncoding.LINEAR16
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    
    if save:
        save_tts(params, response.audio_content)
    return response.audio_content

def save_tts(params: TTSRequest, audio_content):
    filename: str = f"./media/{params.voice_name}-{str(uuid4())}.wav"
    with open(filename, "wb") as out:
        out.write(audio_content)
    return filename