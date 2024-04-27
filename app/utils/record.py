import os
import json
import datetime
from app.models.agent.agent import Agent
from app.models.conversation.conversation import Conversation

def save_agent(agent: Agent, conversation_title: str):
    json_file = f"app/data/conversations/{conversation_title}/agents.json"
    if not os.path.exists(json_file):
        agents_record = []
    else:
        with open(json_file) as f:
            agents_record = json.load(f)
    agents_record.append(agent.model_dump())
    with open(json_file, "w") as f:
        json.dump(agents_record, f, indent=4)
        
def save_conversation(conversation: Conversation, conversation_title: str):
    if not os.path.exists(f"app/data/conversations/{conversation_title}"):
        os.makedirs(f"app/data/conversations/{conversation_title}")
    json_file = f"app/data/conversations/{conversation_title}/conversation.json"
    
    conversations_record = {
        'interactions': [{interaction.agent.identity.name: interaction.message} for interaction in conversation.interactions],
    }
    
    with open(json_file, "w") as f:
        json.dump(conversations_record, f, indent=4)
        
def save_interaction(agent: Agent, prompt: str, response: str):
    with open("app/data/record/interactions.json") as f:
        interactions_record = json.load(f)
    
    interactions_record.append({
        'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'agent': agent.model_dump(),
        'prompt': prompt,
        'response': response
    })
    
    with open("app/data/record/interactions.json", "w") as f:
        json.dump(interactions_record, f, indent=4)