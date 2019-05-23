from .utils.request import request
from .User import User
from .Group import Group
from .Trade import Trade
from .Asset import Asset
from .Auth import Auth
from .Game import Game

class client:
    def __init__(self, cookie=''):
        self.request_client = request(cookie)
        self.Group = Group(self.request_client)
        self.User = User(self.request_client)
        self.Trade = Trade(self.request_client)
        self.Asset = Asset(self.request_client)
        self.Auth = Auth(self.request_client, client)
        self.Game = Game(self.request_client) #TODO: Add more functions to Game class.

        #Info
        self.cookie = cookie



    

