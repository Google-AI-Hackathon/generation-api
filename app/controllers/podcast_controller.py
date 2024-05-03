from app.services.podcast_service import create_dual_podcast, run_dual_podcast, save_dual_podcast_audio

from app.models.agent.agent import Agent
from app.models.podcast.podcast import DualPodcast, Style, Depth, DetailLevel, PodcastResponse
from app.utils.record import random_string
from app.utils.response import interaction_as_response
from google.cloud import storage
import os

def create_dual_podcast_controller(topic: str, style: Style, depth: Depth, detail_level: DetailLevel, n_interactions: int, host: Agent, participant: Agent) -> DualPodcast:
    podcast = create_dual_podcast(topic, style, depth, detail_level, n_interactions, host, participant)
    run_dual_podcast(podcast)
    relative_path = f"tmp/{random_string()}.wav"
    save_dual_podcast_audio(podcast, relative_path)
    bucket_name = "mossaab-420311.appspot.com"
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(relative_path)
    blob.upload_from_filename(relative_path)
    os.remove(relative_path)
    relative_path = f"https://storage.googleapis.com/{bucket_name}/{relative_path}"

    return PodcastResponse(
        interactions=[interaction_as_response(interaction) for interaction in podcast.interactions],
        audio_relative_path=relative_path
    )