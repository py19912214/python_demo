from src.zgy import *
from src.zgy.common import HttpUtils


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

    def get(self, url, params):
        return HttpUtils.get(self.buildUrl(url), params, self.buildGetHeaders());

    def post(self, url, params):
        return HttpUtils.post(self.buildUrl(url), params, self.buildPostHeaders());

    def postFile(self, url, files):
        return HttpUtils.postFile(self.buildUrl(url), files, self.buildPostHeaders());
