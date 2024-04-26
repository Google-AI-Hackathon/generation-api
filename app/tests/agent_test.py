from app.data.conversations.casual.agents import alex, sarah
from app.services.agent_service import generate_single_interaction_response
from app.utils.record import save_interaction

prompt = "What is the meaning of life?"

alex_response = generate_single_interaction_response(alex, prompt)
save_interaction(alex, prompt, alex_response)

sarah_response = generate_single_interaction_response(sarah, prompt)
save_interaction(sarah, prompt, sarah_response)