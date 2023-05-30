"""
Intelligence Type Classification API
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.questionnaires.routers import router as questionnaires_router
from app.users.routers import router as users_router
from app.intelligences.routers import router as intelligences_router
from app.utility.utils import get_origins


# APP
app = FastAPI()

# MIDDLEWARES
app.add_middleware(
    CORSMiddleware,
    allow_origins=get_origins(),
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# ROUTERS
app.include_router(users_router, tags=['Users'])
app.include_router(questionnaires_router, tags=['Questionnaires'])
app.include_router(intelligences_router, tags=['Intelligences'])
