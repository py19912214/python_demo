import json
import urllib.parse

from src.zgy.common import HttpUtils
from src.zgy import *


# 其他服务域名
class CommonParent:
    authorization = ""
    cur_env = ""
    localHostPortRelMap = {}

    def __init__(self, env, localHostPortRelMap, envAndHostRelMap):
        self.cur_env = env
        self.localHostPortRelMap = localHostPortRelMap
        self.envAndHostRelMap = envAndHostRelMap

    def getHost(self):
        return self.envAndHostRelMap.get(self.cur_env)

    def buildUrl(self, url):
        if self.cur_env != localHost:
            return self.getHost() + url
        for localHostUrl, post in self.localHostPortRelMap.items():
            if (url.startswith(localHostUrl)):
                return self.getHost() + post + url.replace(localHostUrl, "/");
        return self.getHost() + url;

    def refreshPigTenantToken(self):
        headers = {
            'authorization': 'Basic d2ViQXBwOndlYkFwcA==',
            'content-type': 'application/x-www-form-urlencoded'
        }
        params = {
            "grant_type": "password",
            "loginType": "password",
            "username": "13111867801",
            "password": "AwxsbzgJZhnxlPjnfTbHNA==",
            "loginAccountSystem": "PIG_TENANT"
        }
        urlParams = urllib.parse.urlencode(params).encode('utf-8')
        host = pig_tenant_dev
        if (self.cur_env != localHost):
            host = self.getHost()
        response = HttpUtils.post(
            host + "/api-uaa/oauth/token?" + urlParams.decode("utf-8"),
            params,
            headers)
        self.authorization = "Bearer " + json.loads(response.text)['data']['access_token']

    def get(self, url, params):
        return HttpUtils.get(self.buildUrl(url), params, self.buildGetHeaders());

    def post(self, url, params):
        return HttpUtils.post(self.buildUrl(url), params, self.buildPostHeaders());
