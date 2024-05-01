from app.setup.config import MAX_PODCAST_CONTEXT_INTERACTIONS

from app.models.agent.agent import Agent
from app.models.interaction.interaction import Interaction
from app.models.podcast.podcast import DualPodcast, Style, Depth, DetailLevel, Counter

from app.services.agent_service import generate_podcast_host_interaction_response, generate_podcast_participant_interaction_response
from app.utils.voice import random_voice, merge_audio_sequence
from app.services.tts_service import synthesize_text, TTSRequest

def create_dual_podcast(topic: str, style: Style, depth: Depth, detail_level: DetailLevel, n_interactions: int, host: Agent, participant: Agent) -> DualPodcast:
    counter = Counter(remaining_interactions={agent.identity.name: n_interactions for agent in [host, participant]})
    return DualPodcast(
        topic=topic,
        style=style,
        depth=depth,
        detail_level=detail_level,
        n_interactions=n_interactions,
        host=host,
        participant=participant,
        interactions=[],
        counter=counter
    )

def run_dual_podcast(podcast: DualPodcast):
    for i in range(podcast.n_interactions):
        print(f"Podcast round {i+1}")
        for agent in [podcast.host, podcast.participant]:
            print(f"Running podcast with {agent.identity.name}")
            if agent == podcast.host:
                response = generate_podcast_host_interaction_response(agent, podcast)
            elif agent == podcast.participant:
                response = generate_podcast_participant_interaction_response(agent, podcast)
            podcast.interactions.append(Interaction(agent=agent, message=response))
            podcast.counter.remaining_interactions[agent.identity.name] -= 1
    print("Podcast complete")
    
def podcast_audio(podcast: DualPodcast, filename: str):
    host_voice = random_voice(podcast.host.identity.gender)
    participant_voice = random_voice(podcast.participant.identity.gender)
    audio_sequence = []
    for interaction in podcast.interactions:
        if interaction.agent == podcast.host:
            request = TTSRequest(
                text=interaction.message,
                voice_name=host_voice
            )
            audio_sequence.append(synthesize_text(request))
        elif interaction.agent == podcast.participant:
            request = TTSRequest(
                text=interaction.message,
                voice_name=participant_voice
            )
            audio_sequence.append(synthesize_text(request))
    return merge_audio_sequence(audio_sequence, filename)