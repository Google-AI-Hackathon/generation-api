from app.models.agent.conversational_agent import ConversationalAgent
from app.models.conversation.conversation import Conversation, Interaction, Counter

from app.services.agent_service import generate_conversation_interaction_response
from app.utils.conversation import shuffle_participants

def initialize_conversation(title: str, agents: list[ConversationalAgent], n_interactions: int) -> Conversation:
    counter = Counter(remaining_interactions={agent.identity.name: n_interactions for agent in agents})
    return Conversation(title=title, n_interactions=n_interactions, participants=agents, interactions=[], counter=counter)

def run_conversation(conversation: Conversation):
    for i in range(conversation.n_interactions):
        print(f"Conversation round {i+1}")
        for agent in conversation.participants:
            print(f"Running conversation with {agent.identity.name}")
            response = generate_conversation_interaction_response(agent, conversation)
            conversation.interactions.append(Interaction(agent=agent, message=response))
            conversation.counter.remaining_interactions[agent.identity.name] -= 1
        shuffle_participants(conversation)
    print("Conversation complete")
            