import requests

token = 'oauth:wdzwxtagmy8u73tfh6jw11zq0jcr4r'
nickname = 'Archit47'
channel = 'fl0m'
clientid='hodyhhd1f7xfovtn1cqr73dsow7utq'
clientsecret='vm2vzb2kj3piz550tcgzs02vxsj44i'

def getkeys():
	body={
		'client_id':clientid,
		'client_secret':clientsecret,
		'grant_type':'client_credentials'
	}
	r=requests.post('https://id.twitch.tv/oauth2/token', body)
	keys=r.json()
	return keys

def checklive():
	keys=getkeys()
	headers={
		'Client-ID':clientid,
		'Authorization':'Bearer '+keys['access_token']
	}

	query={
	    'user_login':channel
	}
	response = requests.get('https://api.twitch.tv/helix/streams',headers=headers,params=query)
	response = response.json()
	if len(response['data'])==0:
		print('Stream is currently Offline\n')
	else:
		print('Stream is Live\n')