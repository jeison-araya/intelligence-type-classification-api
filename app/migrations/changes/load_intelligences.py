import json
from app.database.mongo import database


def upgrade():
    print('========================')
    print('Loading intelligences...')
    print('========================\n')

    with open('app/migrations/data/intelligences.json', 'r', encoding='utf-8') as file:
        intelligences = json.load(file)

    if 'intelligences' not in database.list_collection_names():
        print('Creating intelligences collection... \n')
        database.create_collection('intelligences')

    for intelligence in intelligences:
        if database['intelligences'].find_one({'name': intelligence['name']}):
            print(f'Intelligence: "{intelligence["name"]}" already exists')
            continue
        else:
            print(f'Loading intelligence: "{intelligence["name"]}"')
            database['intelligences'].insert_one(intelligence)

    print()
