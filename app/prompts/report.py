from typing import List
from app.models.conversation.interaction import InteractionResponse

from app.utils.context import conversation_interactions_as_context

def report_prompt(conversation_interactions: List[InteractionResponse]) -> str:
    return f"""
You are a specialized in analyzing a conversation and reporting key insights about it.

CONVERSATION INTERACTIONS:
{conversation_interactions_as_context(conversation_interactions)}

You have successfully analyzed the conversation and reported key insights about it. You can now provide a summary of the conversation, highlighting the key points and insights that you have gathered. Your report should be concise, clear, and informative, providing a comprehensive overview of the conversation dynamics, participants, and interactions. Remember to focus on the most important aspects of the conversation and present your findings in a structured and organized manner.
"""