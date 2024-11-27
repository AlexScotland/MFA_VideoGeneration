"""
Video Generation for ModularFastAPI
Alex Scotland, 2024
"""
# Imports the base necessities
from fastapi import Response, APIRouter

# Assign the API Router to variable ROUTER.
# This is necessary - as in `src.routers.__init__.py` we look for `.ROUTER`

PREFIX = "/video"
ROUTER = APIRouter(
    prefix = PREFIX,
    tags=[
        "Text To Image To Video",
        "Text To Video"]
)


# Build your api end points as you would!
@ROUTER.get("/generate/")
def generate_video():
    return Response("Hello")
