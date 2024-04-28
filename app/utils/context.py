from app.setup.config import MAX_CONTEXT_INTERACTIONS
from app.models.agent.conversational_agent import ConversationalAgent
from app.models.conversation.interaction import Interaction, InteractionResponse
from app.models.conversation.conversation import Conversation
from app.models.relation.relation import Relation

def interaction_as_context(interaction: Interaction) -> str:
    return f"""
[{interaction.agent.identity.name}]: {interaction.message}
"""

def interaction_response_as_context(interaction: InteractionResponse) -> str:
    return f"- {interaction.agent_name}: {interaction.message}"

def relations_as_context(relations: list[Relation]) -> str:
    context = ""
    for relation in relations:
        context += f"""
- Relation with {relation.other.identity.name} with a {relation.hierarchy} hierarchy, {relation.style} style and {relation.intent} intent."""
    return context

def agent_as_context(agent: ConversationalAgent) -> str:
    return f"""
- Identity: {agent.identity.name}, {agent.identity.age} years old.
- Personality: {agent.personality.social_orientation.value} social orientation, {agent.personality.information_processing.value} information processing style, {agent.personality.decision_making_style.value} decision-saking style, {agent.personality.approach_to_structure.value} approach to structure.
- Background: background story: "{agent.background.background_story}", memories: {", ".join(agent.background.memories)}, and interests: {", ".join(agent.background.interests)}.
- Expertise: {agent.expertise.level.value} in {agent.expertise.domain} along {", ".join(agent.expertise.subdomains)} subdomains with {agent.expertise.thinking_process} thinking process.
- Mood: social tones: {", ".join(agent.mood.social_tone)}, emotional tones: {", ".join(agent.mood.emotional_tone)}, mental tones: {", ".join(agent.mood.mental_tone)}, {agent.mood.thinking_flexibility.value} thinking flexibility, {agent.mood.expectation_attitude.value} expectation attitude, {agent.mood.elaboration_length.value} elaboration length.
"""

def conversation_participants_as_context(conversation: Conversation) -> str:
    context = ""
    for participant in conversation.participants:
        context += agent_as_context(participant)
    return context

def conversation_interactions_as_context(conversation_interactions: list[InteractionResponse]) -> str:
    context = ""
    for interaction in conversation_interactions:
        context += f"{interaction_response_as_context(interaction)}\n"
    return context

def get_context(conversation: Conversation) -> str:
    context = ""
    for interaction in conversation.interactions[-MAX_CONTEXT_INTERACTIONS:]:
        context += interaction_as_context(interaction)
    return context