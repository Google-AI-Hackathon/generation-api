from app.models.learning.learning import LearningRequest, Terminology, Depth, DetailLevel

from app.services.learning_service import create_mind_map, create_guide_book
from app.utils.record import save_mind_map, save_guide_book

request = LearningRequest(
    topic="Productivity",
    keywords=["Time Management", "Goal Setting", "Habit Building", "Deep Work", "Focus"],
    terminology=Terminology.general,
    depth=Depth.deep,
    detail_level=DetailLevel.detailed
)

title = "productivity"

mind_map = create_mind_map(request)
save_mind_map(mind_map, title)

guide_book = create_guide_book(request, mind_map)
save_guide_book(guide_book, title)