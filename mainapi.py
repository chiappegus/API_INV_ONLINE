# main.py

import requests
# Importar las credenciales desde el archivo config.py
import config

# Acceder a las credenciales

username = config.USERNAME
password = config.PASSWORD





def get_token1(username, password):
    url = "https://api.invertironline.com/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "username": username,
        "password": password,
        "grant_type": "password"
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        token_data = response.json()
        return token_data["access_token"]
    else:
        response.raise_for_status()




def get_portfolio(token):
    url = "https://api.invertironline.com/api/portafolio"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

token = get_token1(username, password)



def portafolio():
    return get_portfolio(token)

    