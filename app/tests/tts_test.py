import json
from app.services.tts_service import list_voices, synthesize_text, save_tts
from app.models.tts.tts import TTSRequest
from app.models.tts.voice import Voice

def list_voices_test(save: bool = False):
    return list_voices(save=save)

def test_voice(params: TTSRequest):
    synthesize_text(params)
    
def test_all_voices():
    with open('app/data/podcast/voices/voices.json', 'r') as f:
        voices_names = json.load(f)
    for voice_name in voices_names:
        params = TTSRequest(
            text = 'Google Artificial Intelligence Hackathon',
            voice_name=Voice(**voice_name)
        )
        audio = synthesize_text(params)
        # save_tts(audio, f'app/data/podcast/voices/tests/{voice_name["name"]}.wav')
        
# list_voices_test(save=True)
# test_all_voices()