from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from each_country import eachCountry
from list_countries import getCountriesList
import http.client
import json
from india_state import stateData
from districts import districtData
conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")
# from chatterbot import ChatBot


headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "8d5fc3b1ffmsh05bc5eb93529793p119c12jsnbb8a4b9065b4"
    }
app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    sender_number = request.values.get('From')
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
            responded = True
            print(quote)
            print(type(quote))
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'

        msg.body(quote)

    elif 'list' in incoming_msg:
        conn.request("GET", "/countries", headers=headers)
        res = conn.getresponse()
        data = res.read()
        decoded = data.decode("utf-8")
        final_data = json.loads(decoded)
        print(len(final_data['response']))

        final_countries_list2=final_data['response'][:110]


        spacing = ", "

        empty = "‎‎ ‎"

        joining_all2 = spacing.join(final_countries_list2)
        final_string2 = f'{joining_all2} {empty}\n *(For coronavirus list of countries from L-Z type "part2" or include it in a phrase)* '
        # msg.body(final_string1)
        msg.body(final_string2)


    elif 'part2' in incoming_msg:
        conn.request("GET", "/countries", headers=headers)
        res = conn.getresponse()
        data = res.read()
        decoded = data.decode("utf-8")
        final_data = json.loads(decoded)
        print(len(final_data['response']))

        final_countries_list1 = final_data['response'][110:]


        spacing = ", "
        joining_all1 = spacing.join(final_countries_list1)

        final_string1 = f'{joining_all1}'
        empty = "‎‎ ‎"

        msg.body(final_string1)
# here in 1 request only 1500 characters can be send
    elif 'country' in incoming_msg:
        country_name = incoming_msg.split("country", 1)[1].strip()
        con_dic=eachCountry(country_name)
        if type(con_dic)==str:
            msg.body(con_dic)
        else:
            print(con_dic)
            final_string=f"_country name_ : *{con_dic['Country_name']}*\nTotal Corona Cases: *{con_dic['total_cases']}*\nactive covid cases : *{con_dic['active_cases']}*" \
                         f"\ncritical corona cases: *{con_dic['critical_cases']}*\ntotal people recovered: *{con_dic['total_recovered']}*\nNew Corona cases: *{con_dic['new_cases']}*" \
                         f"\nTotal People Died: *{con_dic['total_deaths']}*\nNew death cases: *{con_dic['new_deaths']}*\nLast Time updated: *{con_dic['last_updated_time']}*" \
                         f"\n_(Note: add 4hr 30mins to UTC for IST)_"

            msg.body(final_string)


    elif 'state' in incoming_msg:
        splited_list=[]
        state_name=incoming_msg.split('state',1)[1].strip().title()
        if 'And' in state_name:
            splited_list=state_name.split(' ')
            splited_list[1]=splited_list[1].lower()
            print(splited_list[1])

            state_name=' '.join(splited_list)
            print(state_name)


        # str(state_name)
        print(state_name)
        print(type(state_name))
        state_dic=stateData(state_name)
        if type(state_dic) == str:
            msg.body(state_dic)
        else:
            final_string = f"_state name_ : *{state_dic['state_name']}*\nTotal Confirmed Cases: *{state_dic['confirmed_cases']}*\nactive covid cases : *{state_dic['active_cases']}*" \
                           f"\ntotal people recovered: *{state_dic['cases_recovered']}*\nTotal Deaths in State: *{state_dic['total_deaths']}*" \
                           f"\nLast Time Updated: *{state_dic['last_update_time']}*"
            msg.body(final_string)

    elif 'districts' in incoming_msg:
        splited_list=[]
        state_name=incoming_msg.split('districts',1)[1].strip().title()
        if 'And' in state_name:
            splited_list=state_name.split(' ')
            splited_list[1]=splited_list[1].lower()
            print(splited_list[1])

            state_name=' '.join(splited_list)
            print(state_name)


        # str(state_name)
        print(state_name)
        n=0
        empty = "‎‎ ‎"
        state_dic=districtData(state_name)
        if type(state_dic) == str:
            msg.body(state_dic)
        else:
            for key in state_dic:
                n = n+1
                final_string = f"*{n}.* District name : *{key}*\n" \
                               f"Confirmed cases:  *{state_dic[key]}*\n{empty}"

                msg.body(final_string)
    # elif 'cat' in incoming_msg:
    #     #     # return a cat pic
    #     #     msg.media('https://cataas.com/cat')
    #     #     responded = True

    elif "help" in incoming_msg:
        msg.body('''You can give me the following commands
    😀 *list* (which will give you the list of all the countries infected with covid-19 A-L)
    😁 *part2* (same as list but names from L-Z)
    😎 *country <any country name>* (will give the info about the covid-19 situation of the country)
    😉 *state <name of the state>* (will give the info about the covid-19 situation of the indian-state)
    😍 *district <name of the state>* (to view all the district of the given state only for Indian state and districts)
    😋 *quote* (will give random quote just for some positivity😆 in covid-19 pressure😔)
    👉 *help* (bro you definitely typed this to come here 🤣)
    ''')


    else:
        msg.body('I only know about things related to coronavirus sorry!')
    return str(resp)
