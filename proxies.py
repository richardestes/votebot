import requests
import json
import config

def get_proxies():
  print ("Getting proxies...")
  response = requests.get("https://proxy.webshare.io/api/proxy/list/?page=1&countries=US-FR", headers={"Authorization": "Token " + config.key})
  data = response.json()
  proxy_results = data['results']
  proxies = []
  for proxy in proxy_results:
    proxy_item = 'http://' + str(proxy['proxy_address']) + ':' + str(proxy['ports']['http'])
    proxies.append(proxy_item)
  return proxies
