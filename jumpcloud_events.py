import requests
import datetime
import os

url = "https://events.jumpcloud.com/events"

dt = datetime.datetime.today()
dt2 =dt - datetime.timedelta(days=7)

end= "{0:%Y-%m-%dT%H:%M:%SZ}".format(dt)
start="{0:%Y-%m-%dT%H:%M:%SZ}".format(dt2)

payload = 'startDate=' + start + '&' + 'endDate' +end
headers = {
    'x-api-key': os.environ["JCAPI"],
    'content-type': "application/json",
    }

response = requests.request("GET", url, params=payload, headers=headers)

print(response.text)
