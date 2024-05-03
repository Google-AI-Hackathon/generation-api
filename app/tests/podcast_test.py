from app.utils.record import save_interactions
from app.services.podcast_service import create_dual_podcast, run_dual_podcast, save_dual_podcast_audio, upload_dual_podcast_audio

from app.utils.record import random_string
from app.data.podcast.ai.agents import title, host, participant
from app.models.podcast.podcast import Style, Depth, DetailLevel

podcast = create_dual_podcast(
    topic='AI Future',
    style=Style.entertaining,
    depth=Depth.deep,
    detail_level=DetailLevel.detailed,
    n_interactions=1,
    host=host,
    participant=participant
)

run_dual_podcast(podcast)
save_interactions(podcast.interactions, title)
print(f"Podcast complete: {title}")

file_path = f"media/{random_string()}.wav"
save_dual_podcast_audio(podcast, file_path)
print(f"Podcast audio saved: {file_path}")

public_url = upload_dual_podcast_audio(file_path)
print(f"Podcast audio uploaded: {public_url}")