import requests
def urlget(self, url,username,password):
    proxyDict = {}
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.get(url, auth=(username,password), headers=headers,proxies=proxyDict)
    Tickets = response.json()
    TicketList = Tickets['records']
    for i in TicketList:
        print i

url=""
username=""
password=""
urlget(url,username,password)
