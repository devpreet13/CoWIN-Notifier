pip install twilio
pip install CoWIN-API-by-Kunal-Kumar-Sahoo

from twilio.rest import Client
from cowin_api import CoWinAPI
import time

j = 0

#added a while loop which keeps checking availability every 60 seconds
while j < 1:

    pin_code = "100001"
    date = '13-05-2021'  # Optional. Default value is today's date
    min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit

    cowin = CoWinAPI()
    available_centers = cowin.get_availability_by_pincode(pin_code, date, min_age_limit)
    slots = [x['sessions'][0]['available_capacity'] for x in available_centers['centers'] if x is not None]
    capacity = [x for x in slots if x>0]
    # print(available_centers)


    if len(capacity)>0:
        print('Slot Available')
        i = 0
        while i<10:
            account_sid = 'Enter Twilio SSID'
            auth_token = 'Enter Twilio Authorisation Token'
            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body="Vaccine Slot Available.",
                                from_='+123', #Enter Twilio Phone Number
                                to='+123' #Enter Your Phone Number
                            )
            i += 1
            j = 1
            print(message.sid)

    else:
        print('Slot Unavailable')

    time.sleep(60)
