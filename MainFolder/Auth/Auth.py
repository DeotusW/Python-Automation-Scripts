from configparser import ConfigParser

import requests
from requests.auth import HTTPBasicAuth
from RequestMethods.requestMethods import RequestMain


class fuseAuth:

    URL = "https://aaat.agcocorp.com/auth/oauth2/access_token?realm=/fuse"

    def __init__(self, config):
        self.request = RequestMain()
        # Basic Auth Credentials
        self.Fuse_ClientID = config.get("Auth", "Fuse_ClientID")
        self.Fuse_Secret = config.get("Auth", "Fuse_Secret")
        # Username and Password
        self.Fuse_User = config.get("Auth", "Fuse_User")
        self.Fuse_Password = config.get("Auth", "Fuse_Password")

        self.basicURL = self.URL
        self.body = {
            "grant_type": "password",
            "username": self.Fuse_User,
            "password": self.Fuse_Password,
            "scope": "status.read status.cancel devices.activate devices.deactivate countries.read countries.write"
        }
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

    def authentication(self):
        response = requests.post(self.basicURL,self.body,self.header,auth=HTTPBasicAuth(self.Fuse_ClientID,self.Fuse_Secret))
        #response = self.request.post_method(self.basicURL,body=self.body,headers=self.header,auth=HTTPBasicAuth(self.Fuse_ClientID,self.Fuse_Secret))
        jsonAuthResponse = response.json()
        print(jsonAuthResponse)
        accessToken = jsonAuthResponse["access_token"]

        return accessToken

