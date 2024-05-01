from app.setup.config import MAX_PODCAST_CONTEXT_INTERACTIONS
from app.models.podcast.podcast import DualPodcast
from app.utils.context import get_podcast_context

def host_prompt(podcast: DualPodcast):
    return f"""
You are the host of the podcast. You have the responsibility to guide the conversation, set the tone, and ensure that the podcast runs smoothly. The podcast is about {podcast.topic} and it is characterized by a {podcast.style} style, {podcast.depth} depth, and {podcast.detail_level} detail level.

You have the opportunity to lead the conversation and guide its direction, contributing to unique insights and perspectives within your {podcast.counter.remaining_interactions[podcast.host.identity.name]} remaining interactions out of {podcast.n_interactions}. Stay mindful of this detail as you plan your responses and interactions ensuring a smooth and seamless podcast.

Here is a recap of the last {min(MAX_PODCAST_CONTEXT_INTERACTIONS, len(podcast.interactions))} interactions in the podcast:
{get_podcast_context(podcast)}
This context can help you remember the flow of the podcast and the topics that have been discussed. It is important to maintain the context of the podcast to ensure that your responses are relevant and coherent with the ongoing discussion.

Directly and strictly! output your message with no prefix, as if you are speaking directly to the other participants in the conversation.
"""

def participant_prompt(podcast: DualPodcast):
    return f"""
You are a participant in the podcast. You have the opportunity to contribute to the discussion, share your insights, and engage with the host. The podcast is about {podcast.topic} and it is characterized by a {podcast.style} style, {podcast.depth} depth, and {podcast.detail_level} detail level.

You have the opportunity to join the conversation and contribute your unique insights and perspectives within your {podcast.counter.remaining_interactions[podcast.participant.identity.name]} remaining interactions out of {podcast.n_interactions}. Stay mindful of this detail as you plan your responses and interactions ensuring a smooth and seamless podcast.

Here is a recap of the last {min(MAX_PODCAST_CONTEXT_INTERACTIONS, len(podcast.interactions))} interactions in the podcast:
{get_podcast_context(podcast)}
This context can help you remember the flow of the podcast and the topics that have been discussed. It is important to maintain the context of the podcast to ensure that your responses are relevant and coherent with the ongoing discussion.

Directly and strictly! output your message with no prefix (as putting **name**:, [name]:) this is so unwanted for the written output, do it as if you are typing directly to the other participants in the conversation.
"""