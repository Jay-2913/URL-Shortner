import requests

def shorten_link(full_link, link_name):
    API_KEY = '85325ee5d898de1cb360c311378f11f1e5c10'
    BASE_URL = 'https://cutt.ly/api/api.php'
    
    payload = {'key': API_KEY, 'short': full_link, 'name': link_name}
    response = requests.get(BASE_URL, params=payload)
    data = response.json()
    
    print(data)

shorten_link('https://hianime.to/search?keyword=arcane+', 'codepalace123')
