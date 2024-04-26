from app.services.llm_service import generate_response_text

prompt = "What is the meaning of life?"

response = generate_response_text(prompt)
print(response)