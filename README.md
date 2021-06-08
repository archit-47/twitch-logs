# twitch-chat-logs

Using web sockets to log twitch channel messages.
Go to https://twitchapps.com/tmi/ to request an auth token for your twitch account.

Clone this github repo and create a new file config.py
Add the following lines to this file :

token = 'your_token'
nickname = 'your_nickname'
channel = 'channel_chat_to_log'

Run the python file getchatlogs.py
