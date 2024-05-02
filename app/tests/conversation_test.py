from app.services.conversation_service import initialize_conversation, run_conversation
from app.utils.record import save_conversation

from app.data.conversations.brainstorming.relations import ceo, business, it, design
from app.data.podcast.ai.agents import host, participant

topic = "podcast" # "brainstorming", "podcast"
# agents = [ceo, business, it, design]
agents = [host, participant]

conversation = initialize_conversation(agents)
run_conversation(conversation)
save_conversation(conversation, topic)