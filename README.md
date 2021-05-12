# CoWIN-Notifier
Python script to notify availability of vaccine slots in an area near you


The script relies on using APIs to fetch slot availability from CoWIN portal and notifies you in case a slot is available in your area (pincode) using Twilio.
All you need is:
1) Python Wrapper for Cowin API - https://pypi.org/project/CoWIN-API-by-Kunal-Kumar-Sahoo/
2) A free Twilio Account - https://www.twilio.com/

(This is no rocket science, in case you were looking for an elaborate complex code)

You can edit the script to search multiple dates, search by districts or lat-long etc. More details in the python wrapper link above.

Install the respective helper libraries through pip and you are good to go.

Some useful resources:
1) Sending SMS using Twilio in Python - https://www.twilio.com/docs/sms/quickstart/python
2) Troubleshooting Twilio SSL Error when using Anaconda3 distribution - https://stackoverflow.com/questions/54135206/requests-caused-by-sslerrorcant-connect-to-https-url-because-the-ssl-module
