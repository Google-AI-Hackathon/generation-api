from app.services.conversation_service import initialize_conversation, run_conversation

from app.data.conversations.football.agents import coach, coach_assistant, captain, team_star

from app.utils.record import save_conversation

conversation = initialize_conversation(topic="Next Derby Match", goal="Establish team tactics and spread motivation environment within the team", agents=[coach, coach_assistant, captain, team_star])

run_conversation(conversation, [coach, coach_assistant, captain, team_star])
save_conversation(conversation, "football")