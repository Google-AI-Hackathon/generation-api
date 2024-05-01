from app.models.agent.agent import Agent
from app.models.agent.conversational_agent import ConversationalAgent

from app.models.conversation.conversation import Conversation
from app.models.podcast.podcast import DualPodcast

from app.prompts.agent import single_interaction_prompt, conversational_interaction_prompt, podcast_host_interaction_prompt, podcast_participant_interaction_prompt
from app.services.llm_service import generate_response

def generate_single_interaction_response(agent: Agent, prompt: str) -> str:
    return generate_response(single_interaction_prompt(agent, prompt))

def generate_conversation_interaction_response(agent: ConversationalAgent, conversation: Conversation) -> str:
    return generate_response(conversational_interaction_prompt(agent, conversation))

def generate_podcast_host_interaction_response(agent: ConversationalAgent, podcast: DualPodcast) -> str:
    return generate_response(podcast_host_interaction_prompt(agent, podcast))

def generate_podcast_participant_interaction_response(agent: ConversationalAgent, podcast: DualPodcast) -> str:
    return generate_response(podcast_participant_interaction_prompt(agent, podcast))