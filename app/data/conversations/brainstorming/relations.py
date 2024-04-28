from app.data.conversations.brainstorming.agents import ceo, business, design, it

from app.models.agent.conversational_agent import ConversationalAgent

from app.models.relation.relation import Relation, Hierarchy, Style, Intent

ceo = ConversationalAgent(**ceo.model_dump(), relations=[
    Relation(
        other=business,
        hierarchy=Hierarchy.partnership,
        style=Style.professional,
        intent=Intent.cooperative
    ),
    Relation(
        other=it,
        hierarchy=Hierarchy.mentorship,
        style=Style.friendly,
        intent=Intent.cooperative
    ),
    Relation(
        other=design,
        hierarchy=Hierarchy.mentorship,
        style=Style.friendly,
        intent=Intent.cooperative
    ),
], goal="Brainstorm innovative ideas his startup's next project especially in the realm of the current Generative AI technologies")

business = ConversationalAgent(**business.model_dump(), relations=[
    Relation(
        other=ceo,
        hierarchy=Hierarchy.partnership,
        style=Style.professional,
        intent=Intent.cooperative
    )
], goal="Help the startup with business strategies and opportunities for the startup's next project.")

it = ConversationalAgent(**it.model_dump(), relations=[
    Relation(
        other=ceo,
        hierarchy=Hierarchy.friendship,
        style=Style.friendly,
        intent=Intent.cooperative
    ), 
    Relation(
        other=design,
        hierarchy=Hierarchy.unknown,
        style=Style.neutral,
        intent=Intent.cooperative
    ), 
], goal="Help with the technical aspects concerning any suggestions about the startup next project and how to implement them.")

design = ConversationalAgent(**design.model_dump(), relations=[
    Relation(
        other=ceo,
        hierarchy=Hierarchy.mentorship,
        style=Style.professional,
        intent=Intent.cooperative
    ), 
    Relation(
        other=it,
        hierarchy=Hierarchy.unknown,
        style=Style.neutral,
        intent=Intent.cooperative
    ), 
    Relation(
        other=business,
        hierarchy=Hierarchy.mentorship,
        style=Style.friendly,
        intent=Intent.cooperative
    ),
], goal="Deliever the most creative and out-of-the-box ideas for the startup's next project")