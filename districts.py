import requests
import json
def districtData(state):
    res=requests.get('https://api.covid19india.org/v2/state_district_wise.json')
    data=res.json()
    # stringify=json.dumps(data)
    # print(stringify)

    msg='sorry wrong state name or error in formatting'
    # print(type(data[1]['state']))
    # print(type(state))
    dicToPass={}
    for x in range(len(data)):
        if state == data[x]['state']:
            for y in range(len(data[x]['districtData'])):
                # print(len(data[x]['districtData']))
                # print(data[x]['districtData'][y]['district'])

                dicToPass[f"{data[x]['districtData'][y]['district']}"]=f"{data[x]['districtData'][y]['confirmed']}"
            # print(dicToPass)
            return dicToPass
    if dicToPass=={}:
        return msg
#
# if __name__== "main":
#     name='Delhi'
#     districtData(name)
#

# for key in dicToPass:
#     final_string=f"District name : {key}\n" \
#                 f"Confirmed cases:  {dicToPass[key]}"

    # print(final_string)
