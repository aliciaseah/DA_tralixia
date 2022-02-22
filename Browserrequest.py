import requests
headers = {
    'User Agent': 'Mobile'
}
url = 'http://192.168.137.146/photography/'
r = requests.get(url)