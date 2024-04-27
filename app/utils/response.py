from app.models.conversation.interaction import Interaction, InteractionResponse

def interaction_as_response(interaction: Interaction) -> InteractionResponse:
    return InteractionResponse(agent_name=interaction.agent.identity.name, message=interaction.message)