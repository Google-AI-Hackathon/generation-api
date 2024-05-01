from app.utils.record import save_interactions
from app.services.podcast_service import create_dual_podcast, run_dual_podcast, podcast_audio
from app.services.tts_service import save_tts

from app.data.simulation.ai.agents import title, host, participant
from app.models.podcast.podcast import Style, Depth, DetailLevel

podcast = create_dual_podcast(
    topic='AI Future',
    style=Style.entertaining,
    depth=Depth.deep,
    detail_level=DetailLevel.detailed,
    n_interactions=5,
    host=host,
    participant=participant
)

run_dual_podcast(podcast)
save_interactions(podcast.interactions, title)

output = podcast_audio(podcast, filename=f'./media/{title}.wav')