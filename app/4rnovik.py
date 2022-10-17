import json
import requests

url_server = "https://server-game-millionaire.herokuapp.com"
command = "get_data_about_user"
get_user = requests.post(f"{url_server}/{command}", data=json.dumps({"user_id": "ufttfrrnxfgxybwfrdzjlccot"}))
# print(get_user)
if get_user.ok:
    data = get_user.json()
    print(data)
else:
    print(get_user.text)
    print("Eror")