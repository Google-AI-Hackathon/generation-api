from app.services.podcast_service import create_dual_podcast, run_dual_podcast, save_dual_podcast_audio, upload_dual_podcast_audio

from app.models.agent.agent import Agent
from app.models.podcast.podcast import DualPodcast, Style, Depth, DetailLevel, PodcastResponse
from app.utils.record import random_string
from app.utils.response import interaction_as_response

def create_dual_podcast_controller(topic: str, style: Style, depth: Depth, detail_level: DetailLevel, n_interactions: int, host: Agent, participant: Agent) -> DualPodcast:
    podcast = create_dual_podcast(topic, style, depth, detail_level, n_interactions, host, participant)
    run_dual_podcast(podcast)
    file_path = f"media/{random_string()}.wav"
    save_dual_podcast_audio(podcast, file_path)
    return PodcastResponse(
        interactions=[interaction_as_response(interaction) for interaction in podcast.interactions],
        public_url=upload_dual_podcast_audio(file_path)
    )