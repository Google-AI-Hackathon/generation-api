import json
import datetime
from app.models.agent.agent import Agent

def save_agent(agent: Agent):
    with open("app/data/record/agents.json") as f:
        agents_record = json.load(f)
    agents_record.append(agent.model_dump())
    with open("app/data/record/agents.json", "w") as f:
        json.dump(agents_record, f, indent=4)
        
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