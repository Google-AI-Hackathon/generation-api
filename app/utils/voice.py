import os
import json
from pydub import AudioSegment

from app.models.tts.voice import Voice
from app.models.tts.tts import TTSRequest
from app.services.tts_service import synthesize_text

def podcast_to_voice(conversation_title: str, voice_names: list[str]):
    with open('app/data/conversations/podcast/conversation.json', 'r') as f:
        conversation = json.load(f)
    for i, interaction in enumerate(conversation):
        params = TTSRequest(
            text = interaction['message'],
            voice_name=Voice(name=voice_names[i % 2], ssml_gender=1)
        )
        interaction_audio = synthesize_text(params=params)
        with open(f"app/data/conversations/podcast/voice/{i+1}.wav", "wb") as out:
            out.write(interaction_audio)

def merge_wav_files(directory, output_file):
    wav_files = [file for file in os.listdir(directory) if file.endswith(".wav")]

    wav_files.sort(key=lambda x: int(os.path.splitext(x)[0]))
    merged_audio = AudioSegment.silent(duration=0)
    for wav_file in wav_files:
        audio = AudioSegment.from_wav(os.path.join(directory, wav_file))
        merged_audio += audio

    merged_audio.export(output_file, format="wav")