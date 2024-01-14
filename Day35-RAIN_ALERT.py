#RAIN ALERT PROJECT

"""using openweathermap.org find if it will rain today
and alert the user if it does using twilio by sending an sms"""

#TODO IMPORT MODULES
import requests
from twilio.rest import Client
"""request module for api calling 
twilio app for sending sms"""

#TODO CONSTANTS
account_sid=""
auth_token=""
my_twilio_phno=""
"""twilio constants"""

API_KEY=""
weather_parameter={
"lat":46.608139
,"lon":-121.671577
,"appid":API_KEY
,"exclude":"daily,minutely"
}
"""openweathermap.org constants"""

#TODO ACQUIRE WEATHER DATA FOR 12 HOURS
response=requests.get(url="https://api.openweathermap.org/data/2.5/onecall?",params=weather_parameter)
print("status_code-",response.status_code)
json_data=response.json()
weather_data=json_data["hourly"][:12]
print(weather_data)

weather_id_list=[]
for i in weather_data:
    weather_id=i["weather"][0]["id"]
    weather_id_list.append(weather_id)
print(weather_id_list)

#TODO CHECK FOR RAIN
for id in weather_id_list:
    if id <600:
        print("Take an umbrella ")
        #TODO SEND SMS
        client=Client(account_sid,auth_token)
        message=client.messages \
                        .create(
            body="It's going to rain today,take an umbrella ☂",
            from_=my_twilio_phno,
            to=""
        )
        print(message.sid)
        print(message.status)

        break



