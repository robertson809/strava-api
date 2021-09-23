import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"
kudos_url = "https://www.strava.com/api/v3//activities/{horse}/kudos"
# print(kudos_url.format(id='trump'))

payload = {
    'client_id': "38050",
    'client_secret': '7bc695a978b6f1b043525dc637e8f001fe29e2ff',
    'refresh_token': 'a67b04f293fba98320be9c7673208bbebf8b00f5',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()

def mt_mi(meters):
    return round(meters * 0.000621371,1)

for item in my_dataset:
    print(item['name'],':', mt_mi(item['distance']))
    kudos_givers = requests.get(kudos_url.format(horse=item['id']), headers=header).json()
    for giver in kudos_givers:
        print('Got kudos from', giver['firstname'] + ' ' + giver['lastname'])