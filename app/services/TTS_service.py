import google.cloud.texttospeech as tts
from app.models.TTS.tts import GenerateTTSRequest
from app.setup.config import TTS_LANGUAGE
import app.setup.creds  

class TTS_service:
    def __init__(self):
        self.client = tts.TextToSpeechClient()
        
    def list_voices(self , language_code: str = TTS_LANGUAGE):
        client = tts.TextToSpeechClient()
        response = client.list_voices(language_code=language_code)
        voices = sorted(response.voices, key=lambda voice: voice.name)
        print(f"Voices: {voices}")
        return voices
    


    def synthesize_text(self, params: GenerateTTSRequest):
        synthesis_input = tts.SynthesisInput(text=params.text)
        voice = tts.VoiceSelectionParams(
            language_code=params.language, name=params.voice_name.name
        )
        audio_config = tts.AudioConfig(
            audio_encoding=tts.AudioEncoding.LINEAR16
        )
        response = self.client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )
        return response.audio_content


    def save_tts(self, params: GenerateTTSRequest):
        audio_content = self.synthesize_text(params)
        with open(params.filename, "wb") as out:
            out.write(audio_content)
        return params.filename
     
    

        

    


