from app.data.conversations.podcast.agents import interviewer, interviewee

from app.models.agent.conversational_agent import ConversationalAgent

from app.models.relation.relation import Relation, Hierarchy, Style, Intent

interviewer = ConversationalAgent(**interviewer.model_dump(), relations=[
    Relation(
        other=interviewee,
        hierarchy=Hierarchy.unknown,
        style=Style.neutral,
        intent=Intent.neutral
    )
], goal="Finding the ultimate correct religion")

interviewee = ConversationalAgent(**interviewee.model_dump(), relations=[
    Relation(
        other=interviewer,
        hierarchy=Hierarchy.unknown,
        style=Style.neutral,
        intent=Intent.neutral
    )
], goal="To engage in deep discourse on religion")