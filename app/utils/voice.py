import json
import random
from io import BytesIO
from pydub import AudioSegment

from app.models.tts.voice import Voice
from app.models.agent.identity import Gender

def gender_num(gender: Gender):
    return 1 if gender==Gender.male else 2

def gender_voices(gender: Gender):
    with open('app/data/podcast/voices/voices.json', 'r') as f:
        voices = json.load(f)
    return [Voice(**voice) for voice in voices if voice['ssml_gender']==gender_num(gender)]

def random_voice(gender: Gender):
    return random.choice(gender_voices(gender))

def merge_audio_sequence(audio_sequence, file_path: str):
    merged_audio = AudioSegment.silent(duration=0)
    for audio_bytes in audio_sequence:
        audio_segment = AudioSegment.from_file(BytesIO(audio_bytes), format="mp3")
        merged_audio += audio_segment
    merged_audio.export(file_path, format="mp3")
    return file_path