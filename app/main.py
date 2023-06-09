"""
Intelligence Type Classification API
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.intelligences.routers import router as intelligences_router
from app.users.routers import router as users_router
from app.questions.routers import router as questions_router
from app.utility.utils import get_origins
from app.answers.routers import router as answers_router
from app.intelligences_profiles.routers import router as intelligences_profiles_router

# APP
app = FastAPI(
    title='Intelligence Type Classification API',
    description='API for intelligence type classification',
    version='1.0.0')

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
app.include_router(intelligences_router, tags=['Intelligences'])
app.include_router(questions_router, tags=['Questions'])
app.include_router(answers_router, tags=['Answers'])
app.include_router(intelligences_profiles_router,
                   tags=['Intelligences Profiles'])
