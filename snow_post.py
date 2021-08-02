import requests
import json


def send_to_snow(method, url, data=None):
    user = 'usr'
    pwd = 'pwd'

    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.request(method, url, auth=(user, pwd), headers=headers, data=json.dumps(data))

    res = response.json()
    return res


def export_tickets():
    f = open('dummy_response.json')
    incidents = json.load(f)

    fields = ['clientId', 'customerName', 'cluster', 'errorCode', 'eventInfo', 'id', 'location', 'objectName',
              'objectType', 'priority', 'status', 'adpNotes', 'dateLoggedUTC']

    for i in range(len(incidents['incidents'])):
        x = {f'u_{key.lower()}': value for key, value in incidents['incidents'][i].items() if key in fields}
        x.update({'u_config_item': 'ProtectView', 'u_assignment_group': 'TOC - L1 Support', 'u_caller_id': 'ADP Ticketing'})
        yield x
