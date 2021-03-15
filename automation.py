from requests.api import options
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy,  ProxyType 
from selenium.webdriver.chrome.options import Options 
import random

from proxies import get_proxies
from emails import get_emails,split_emails
import time

def setup_proxy(proxy):
  proxy_config = Proxy()
  proxy_config.proxy_type = ProxyType.MANUAL
  proxy_config.http_proxy = proxy
  proxy_config.ssl_proxy = proxy
  capabilities = webdriver.DesiredCapabilities.CHROME 
  proxy_config.add_to_capabilities(capabilities)
  return proxy_config

def vote():
  emails = get_emails()
  for item in emails:
    print(item)
    proxies = get_proxies()
    proxy_index = random.randrange(0,5)
    proxy = proxies[proxy_index]
    print(proxy)
    full_name = item[0]
    email= item[1]
    print(full_name)
    print(email)
    proxy_config = Proxy()
    proxy_config.proxy_type = ProxyType.MANUAL
    proxy_config.http_proxy = proxy
    proxy_config.ssl_proxy = proxy
    capabilities = webdriver.DesiredCapabilities.CHROME 
    proxy_config.add_to_capabilities(capabilities)
    chrome_options = Options()
    chrome_options.headless = True
    driver = webdriver.Chrome("./chromedriver",desired_capabilities=capabilities,options=chrome_options)
    driver.get("") # FILL IN WITH WEBSITE
    time.sleep(10) # give page time to load
    form_full_name = driver.find_element_by_xpath('') #FILL IN WITH X PATH
    form_full_name.send_keys(full_name)
    form_radio_button = driver.find_element_by_xpath('') #FILL IN WITH X PATH
    form_radio_button.click()
    form_video_dropdown = driver.find_element_by_xpath('') #FILL IN WITH X PATH
    form_video_dropdown.click()
    form_video_choice = driver.find_element_by_xpath('') #FILL IN WITH X PATH
    form_video_choice.click()
    form_email_address = driver.find_element_by_xpath('') #FILL IN WITH X PATH
    form_email_address.send_keys(email)
    form_submit_button = driver.find_element_by_xpath('') #FILL IN WITH X PATH
    form_submit_button.click()
    time.sleep(10) # give time to submit
    get_confirmation_text = driver.find_element_by_css_selector('') #FILL IN WITH X PATH
    if ((get_confirmation_text.text) == ""): #FILL IN WITH CONFIRMATION MESSAGE
      print ("Successfully voted!")
    else:
      print ("Did not vote successfully.")
    driver.quit()
    time.sleep(300) # wait 5 mins

vote()
