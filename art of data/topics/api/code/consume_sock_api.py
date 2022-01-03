import requests

BASE_URL = "https://hm-cs.herokuapp.com"
ENDPOINT = "/socks"
payload = {'key': "ArtOfDataKEY123", 'idx': 0}

# Continue to make requests until an invalid index is passed
requesting = True
while requesting:
  response = requests.get(base_url, params=payload)
  if response.ok:
    print(response.text.replace('\ufeff', ''))
    payload['idx'] += 1
  requesting = response.ok
