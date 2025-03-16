from fastapi import FastAPI

from SocialMediaAPI.routers.post import router as post_router

app = FastAPI()


app.include_router(post_router)
