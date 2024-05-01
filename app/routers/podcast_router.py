# from fastapi import APIRouter

# from app.controllers.podcast_controller import create_dual_podcast_controller
# from app.models.podcast.podcast import PodcastRequest, PodcastResponse

# router = APIRouter()

# @router.post("/", response_model=PodcastResponse)
# async def create_dual_podcast(request: PodcastRequest) -> PodcastResponse:
#     return create_dual_podcast_controller(
#         request.topic,
#         request.style,
#         request.depth,
#         request.detail_level,
#         request.n_interactions,
#         request.host,
#         request.participant
#     )