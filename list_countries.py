import http.client
import json
conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")


headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "8d5fc3b1ffmsh05bc5eb93529793p119c12jsnbb8a4b9065b4"
    }

def getCountriesList():

    conn.request("GET", "/countries", headers=headers)
    res = conn.getresponse()
    data = res.read()

    decoded=data.decode("utf-8")
    final_data=json.loads(decoded)
    final_countries_list=final_data['response'][:5]
    # print(final_countries_list)
    str = ", "
    final_string=str.join(final_countries_list)
    msg = "sorry no data"
    print(final_string)
    if final_string:
        return final_string
    else:
        return msg

if __name__ == '__main__':
    getCountriesList()
