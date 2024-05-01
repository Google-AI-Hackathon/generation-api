import os
import uuid
import json
from app.models.agent.agent import Agent
from app.models.conversation.conversation import Conversation
from app.models.podcast.podcast import DualPodcast
from app.models.interaction.interaction import Interaction, InteractionResponse
from app.utils.conversation import get_interaction_response

def random_string() -> str:
    return str(uuid.uuid4())

def save_agent(agent: Agent, title: str):
    if not os.path.exists(f"app/data/simulation/{title}"):
        os.makedirs(f"app/data/simulation/{title}")
    json_file = f"app/data/simulation/{title}/agents.json"
    if not os.path.exists(json_file):
        agents_record = []
    else:
        with open(json_file) as f:
            agents_record = json.load(f)
    agents_record.append(agent.model_dump())
    with open(json_file, "w") as f:
        json.dump(agents_record, f, indent=4)
        
def save_interactions(interactions: list[Interaction], title: str):
    if not os.path.exists(f"app/data/simulation/{title}"):
        os.makedirs(f"app/data/simulation/{title}")
    json_file = f"app/data/simulation/{title}/interactions.json"
    record = [get_interaction_response(interaction).model_dump() for interaction in interactions]
    with open(json_file, "w") as f:
        json.dump(record, f, indent=4)
        
def save_report(report: str, conversation_title: str):
    with open(f"app/data/conversations/{conversation_title}/report.md", "w") as f:
        f.write(report)
        
def load_agents(conversation_title: str) -> list[Agent]:
    json_file = f"app/data/conversations/{conversation_title}/agents.json"
    with open(json_file) as f:
        agents_record = json.load(f)
    return [Agent(**agent) for agent in agents_record]

def load_conversation_interactions(conversation_title: str) -> str:
    json_file = f"app/data/conversations/{conversation_title}/conversation.json"
    with open(json_file) as f:
        interactions_record = json.load(f)
    return [InteractionResponse(**interaction) for interaction in interactions_record]