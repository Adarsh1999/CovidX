import requests
import json
# res=requests.get('https://api.covid19india.org/data.json')
# data=res.json()
# stringify=data.dumps()
# print(type(data))
# stringify=json.dumps(data)
# print(stringify)
# print(data['statewise'])

# print(data['statewise'][1]["state"])

# state_name = "Madhya Pradesh"
def stateData(state_name):
    res = requests.get('https://api.covid19india.org/data.json')
    data = res.json()
    # print(data)
    toPass={}
    msg="wrong state name or wrong spelling or formatting"
    for x in range(len(data['statewise'])):
        # print(data['statewise'][x]['state'])
        if state_name==data['statewise'][x]['state']:
           toPass = {
             'active_cases':data['statewise'][x]['active'],
             'confirmed_cases':data['statewise'][x]['confirmed'],
             'total_deaths': data['statewise'][x]['deaths'],
             'last_update_time': data['statewise'][x]['lastupdatedtime'],
             'cases_recovered': data['statewise'][x]['recovered'],
             'state_name': data['statewise'][x]['state'],

            }
           print(toPass)
           return toPass

    return msg

