import json

from app.models.learning.learning import LearningRequest, Terminology, Depth, DetailLevel

from app.services.learning_service import create_mind_map

request = LearningRequest(
    topic="Building SaaS (Software as a Service)",
    keywords=["Development", "Marketing", "Business"],
    terminology=Terminology.technical,
    depth=Depth.deep,
    detail_level=DetailLevel.detailed
)

mind_map = create_mind_map(request)
print(mind_map)

with open('test.txt', 'w') as f:
    f.write(mind_map)

# with open('test.json', 'w') as f:
#     json.dump(mind_map.model_dump(), f, indent=4)