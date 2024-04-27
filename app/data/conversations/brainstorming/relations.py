from app.data.conversations.brainstorming.agents import nobara, mark, yuri

from app.models.agent.conversational_agent import ConversationalAgent

from app.models.relation.relation import Relation, Hierarchy, Style, Intent

nobara = ConversationalAgent(**nobara.model_dump(), relations=[
    Relation(
        other=mark,
        hierarchy=Hierarchy.partnership,
        style=Style.friendly,
        intent=Intent.cooperative
    ), 
    Relation(
        other=yuri,
        hierarchy=Hierarchy.friendship,
        style=Style.friendly,
        intent=Intent.cooperative
    ), 
], goal="Brainstorm innovative ideas for an AI startup project")

mark = ConversationalAgent(**mark.model_dump(), relations=[
    Relation(
        other=nobara,
        hierarchy=Hierarchy.partnership,
        style=Style.professional,
        intent=Intent.cooperative
    ),
    Relation(
        other=yuri,
        hierarchy=Hierarchy.friendship,
        style=Style.friendly,
        intent=Intent.cooperative
    ), 
], goal="Network with AI people")


yuri = ConversationalAgent(**yuri.model_dump(), relations=[
    Relation(
        other=mark,
        hierarchy=Hierarchy.friendship,
        style=Style.friendly,
        intent=Intent.cooperative
    ), 
    Relation(
        other=nobara,
        hierarchy=Hierarchy.friendship,
        style=Style.friendly,
        intent=Intent.cooperative
    ), 
], goal="Just meet and enjoy with best friends")
