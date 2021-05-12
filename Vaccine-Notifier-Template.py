# pip install twilio
# pip install CoWIN-API-by-Kunal-Kumar-Sahoo

from twilio.rest import Client
from cowin_api import CoWinAPI
import time
import datetime
import numpy as np

start_date = datetime.date(2021, 5, 12) #enter date in yyyy,m,d format (without preceding 0)
number_of_days = 5 #range of days you want to check for availability
cowin = CoWinAPI()




pin_code = "110001" # Enter the area pincode
min_age_limit = 45  # Optional. By default returns centers without filtering by min_age_limit
start_date = datetime.date(2021, 5, 12) #enter date in yyyy,m,d format (without preceding 0)
number_of_days = 5 # range of days you want to check for availability

# creating range of dates
date_list = []
for day in range(number_of_days):
    a_date = (start_date + datetime.timedelta(days = day)).strftime('%d-%m-%Y')
    date_list.append(a_date)

def availability(date):
    """
    Function to check availability of slots for a particular date
    Input: string (date - dd-mm-YYYY)
    Output: bool
    """
    available_centers = cowin.get_availability_by_pincode(pin_code, date, min_age_limit)
    slots = [x['sessions'][0]['available_capacity'] for x in available_centers['centers'] if x is not None]
    capacity = bool(len([x for x in slots if x>0]))
    return capacity

    
j = 0

#added a while loop which keeps checking availability every 60 seconds
while j < 1:

    
    if np.any([availability(x) for x in date_list]):
        print('Slot Available')
        i = 0
        while i<10: # you will receive 10 messages if any slots are available
            account_sid = 'Enter Twilio SID'
            auth_token = 'Enter Twilio Authorisation Token'
            client = Client(account_sid, auth_token)

            message = client.messages \
                            .create(
                                body="Vaccine Slot Available.",
                                from_='+123', # Enter Twilio Phone Number
                                to='+123' # Enter Your Phone Number
                            )
            i += 1
            j = 1
            print(message.sid)

    else:
        print('Slot Unavailable')

    time.sleep(60)
