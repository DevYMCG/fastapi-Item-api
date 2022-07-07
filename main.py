from fastapi import FastAPI

from v1.router.user_router import router as user_router
from v1.router.item_router import router as item_router


app = FastAPI()

app.include_router(user_router)
app.include_router(item_router)