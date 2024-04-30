from app.utils.voice import podcast_to_voice, merge_wav_files

podcast_to_voice('podcast', ['en-US-Neural2-H', 'en-US-Casual-K'])
dir = 'app/data/conversations/podcast'
merge_wav_files(f"{dir}/voice", f"{dir}/podcast.wav")