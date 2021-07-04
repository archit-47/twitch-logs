import re
import socket
import logging
import config
from datetime import datetime

class twitchchat:
	def __init__(self,channel):
		self.server = 'irc.chat.twitch.tv'
		self.port = 6667
		self.nickname = config.nickname
		self.token = config.token
		self.channel = '#'+channel

	def setsocket(self):
		self.sock=socket.socket()
		self.sock.connect((self.server, self.port))
		self.sock.send(f"PASS {self.token}\n".encode('utf-8'))
		self.sock.send(f"NICK {self.nickname}\n".encode('utf-8'))
		self.sock.send(f"JOIN {self.channel}\n".encode('utf-8'))

	def startlogs(self,time):
		now = datetime.now()
		# dd/mm/YY H:M:S
		dt_string = now.strftime("%d_%m_%Y")
		if time is not None:
			logging.basicConfig(filename=dt_string+self.channel[1:]+'.log',encoding='utf-8',level=logging.DEBUG,format='%(message)s')
			logging.info("StartTime: "+str(time))
		
		for handler in logging.root.handlers[:]:
			logging.root.removeHandler(handler)
		
		logging.basicConfig(filename=dt_string+self.channel[1:]+'.log',encoding='utf-8',level=logging.DEBUG,format='%(asctime)s\t%(message)s')
		self.count=0
		print("Started Logging!!")
		while True:
		    resp = self.sock.recv(2048).decode('utf-8')
		    if resp.startswith('PING'):
		        self.sock.send("PONG\n".encode('utf-8'))
		        print("PONG\n")

		    try:
		        username, channel, message = re.search(r':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', resp).groups()
		        logging.info(username.strip() + "\t" + message.strip())
		    except AttributeError as e:
		        pass
		    self.count+=1
		    
		    print("\r"+str(self.count), sep=' ', end='', flush=True)
		self.sock.close()
    		

def main():
	start_time = config.checklive() #Remove this line (added from twitch api in config.py)
	streamer=twitchchat(config.channel)
	streamer.setsocket()
	streamer.startlogs(start_time)

if __name__ == "__main__":
	main()