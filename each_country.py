import http.client
import json
conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")


headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "8d5fc3b1ffmsh05bc5eb93529793p119c12jsnbb8a4b9065b4"
    }
def eachCountry(country):


    conn.request("GET", f"/history?country={country}", headers=headers)

    res = conn.getresponse()
    print(res.status)
    data = res.read()

    decoded=data.decode("utf-8")
    final_data=json.loads(decoded)
    msg="This country either don't have corona or this country doesn't exist"
    if len(final_data['response']) == 0:
        print(msg)
        return msg
    # each_country=final_data['response']
    # print(decoded)
    else:
        toPass = {
            'Country_name': final_data['response'][0]['country'],
            'new_cases': final_data['response'][0]['cases']['new'],
            'active_cases': final_data['response'][0]['cases']['active'],
            'critical_cases': final_data['response'][0]['cases']['critical'],
            'total_recovered': final_data['response'][0]['cases']['recovered'],
            'total_cases': final_data['response'][0]['cases']['total'],
            'total_deaths': final_data['response'][0]['deaths']['total'],
            'new_deaths': final_data['response'][0]['deaths']['new'],
            'last_updated_time': final_data['response'][0]['time']
        }


        return toPass

