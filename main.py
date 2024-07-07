import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5dee93da8d5ad3d12f4f981df7c3c1c4'
HEADER = {'content-type' : 'application/json', 'trainer_token': TOKEN}
body_pokemons = {
    "trainer_token": TOKEN,
    "email": "legreilabripei-2854@yopmail.com",
    "password": "Qwerty123"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_change = {
    "pokemon_id": "42130",
    "name": "bob",
    "photo_id": 2
}
body_add_pokeball = {
    "pokemon_id": "42130"
}
'''response = requests.post(url = f'{URL}/trainers/reg', headers= HEADER, json = body_pokemons)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers=HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers=HEADER, json = body_create)
print(response_create.text)'''

'''pokemon_id= response_create.json()['id']
print(pokemon_id)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers=HEADER, json = body_change)
print(response_change.text)'''

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)