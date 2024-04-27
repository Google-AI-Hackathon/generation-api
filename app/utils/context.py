from app.setup.config import MAX_CONTEXT_INTERACTIONS
from app.models.conversation.interaction import Interaction
from app.models.conversation.conversation import Conversation
from app.models.relation.relation import Relation

def interaction_as_context(interaction: Interaction) -> str:
    return f"""
[{interaction.agent.identity.name}]: {interaction.message}
"""

def relations_as_context(relations: list[Relation]) -> str:
    context = ""
    for relation in relations:
        context += f"""
- Relation with {relation.other.identity.name} with a {relation.hierarchy} hierarchy, {relation.style} style and {relation.intent} intent."""
    return context

def get_context(conversation: Conversation) -> str:
    context = ""
    for interaction in conversation.interactions[-MAX_CONTEXT_INTERACTIONS:]:
        context += interaction_as_context(interaction)
    return context