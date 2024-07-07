import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5dee93da8d5ad3d12f4f981df7c3c1c4'
HEADER = {'content-type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '6340'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    assert response.status_code == 200 
def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'bob'
@pytest.mark.parametrize('key, value', [('name', 'bob'), ('trainer_id', TRAINER_ID),('id', '42130')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value