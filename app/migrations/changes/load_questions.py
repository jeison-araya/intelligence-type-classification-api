import json
from app.database.mongo import database


def upgrade():
    print('========================')
    print('Loading questions...')
    print('========================\n')

    with open('app/migrations/data/questions.json', 'r', encoding='utf-8') as file:
        questions = json.load(file)

    if 'questions' not in database.list_collection_names():
        print('Creating questions collection... \n')
        database.create_collection('questions')

    for question in questions:
        if database['questions'].find_one({'question': question['question']}):
            print(f'Question: "{question["question"][:30]}..." already exists')
            continue
        else:
            print(f'Loading question" "{question["question"]}"')
            database['questions'].insert_one(question)
