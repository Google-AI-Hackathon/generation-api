from app.services.conversation_service import initialize_conversation, run_conversation
from app.utils.record import save_conversation

from app.data.conversations.brainstorming.relations import yuri, nobara, mark

topic = "brainstorming"
agents = [yuri, nobara, mark]

conversation = initialize_conversation(agents)
run_conversation(conversation)
save_conversation(conversation, topic)