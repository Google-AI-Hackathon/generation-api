from app.setup.config import MAX_CONTEXT_INTERACTIONS
from app.models.conversation.conversation import Conversation
from app.models.agent.agent import Agent
from app.utils.context import get_context

def conversation_prompt(conversation: Conversation, agent: Agent):
    return f"""
You are currently engaged in a discussion on "{conversation.topic}" with the overarching goal of "{conversation.goal}".

This conversation is an opportunity for collaborative exploration, where each participant's insights contribute to our collective understanding and progress towards our shared objective.

As we delve deeper into the topic, consider the following:
- Dive into details: Explore specific aspects of the topic to uncover hidden insights.
- Challenge assumptions: Question underlying assumptions and explore alternative perspectives.
- Foster creativity: Encourage innovative ideas and out-of-the-box thinking to tackle challenges.
- Engage actively: Participate actively in the conversation, listening attentively and contributing thoughtfully.
- Embrace diversity: Embrace diverse viewpoints and experiences, enriching our discussion with varied perspectives.

Let's continue our journey of discovery together! You have the opportunity to shape the conversation and guide its direction, contributing your unique insights and perspectives within your {conversation.counter.remaining_interactions[agent.identity.name]} remaining interactions.

Here is a recap of the last {min(MAX_CONTEXT_INTERACTIONS, len(conversation.interactions))} interactions in our conversation:
{get_context(conversation)}
"""