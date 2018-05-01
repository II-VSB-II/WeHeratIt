import requests
def urlget(url,username,password):
    proxyDict = {}
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.get(url, auth=(username,password), headers=headers,proxies=proxyDict)
    Tickets = response.json()
    TicketList = Tickets['records']
    for i in TicketList:
        print i

url="https://<instance>.service-now.com/incident.do?JSONv2&amp;sysparm_action=getRecords&amp;sysparm_query=assignment_group=<group_id>^incident_state=1"
username=""
password=""
urlget(url,username,password)
