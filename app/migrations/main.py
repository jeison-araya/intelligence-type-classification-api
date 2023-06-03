from app.migrations.changes import load_intelligences
from app.migrations.changes import load_questions


def upgrade():
    load_intelligences.upgrade()
    load_questions.upgrade()
