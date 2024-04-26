from app.setup.config import MAX_AGENT_INTERACTIONS

from app.models.agent.agent import Agent
from app.models.conversation.conversation import Conversation, Interaction, Counter

from app.services.agent_service import generate_conversation_interaction_response

def initialize_conversation(topic: str, goal: str, agents: list[Agent]) -> Conversation:
    counter = Counter(remaining_interactions={agent.identity.name: MAX_AGENT_INTERACTIONS for agent in agents})
    return Conversation(topic=topic, goal=goal, participants=agents, interactions=[], counter=counter)

def run_conversation(conversation: Conversation, agents: list[Agent]):
    for i in range(MAX_AGENT_INTERACTIONS):
        print(f"Conversation round {i+1}")
        for agent in agents:
            print(f"Running conversation with {agent.identity.name}")
            response = generate_conversation_interaction_response(agent, conversation)
            conversation.interactions.append(Interaction(agent=agent, message=response))
            conversation.counter.remaining_interactions[agent.identity.name] -= 1
    print("Conversation complete")
            