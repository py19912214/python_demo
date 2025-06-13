import datetime
import hashlib
import hmac
import json

from src.zgy import *
from src.zgy.common import HttpUtils


# 其他服务域名
class CommonParent:
    authorization = "Bearer GreQqM2gvN4TYqE8VLUfUcIUEYgy3DApeZzQaRPM4rt66wXkMmXN_xf0jUKGbdXQZIjygbZ_7OJZkpIXWG1rVbpf0difTzJIbZg44thz666VZyXF34gEvuOa5jBjvTSd"
    cur_env = ""
    localHostPortRelMap = {}
    appKey = ""
    appSecret = ""

    def __init__(self, env, localHostPortRelMap, envAndHostRelMap):
        self.cur_env = env
        self.localHostPortRelMap = localHostPortRelMap
        self.envAndHostRelMap = envAndHostRelMap

    def setAppKey(self, appKeyEnvRelMap):
        cur_env_1 = self.cur_env
        if (self.cur_env == localHost):
            cur_env_1 = dev
        self.appKey = appKeyEnvRelMap.get(cur_env_1).get("appKey")
        self.appSecret = appKeyEnvRelMap.get(cur_env_1).get("appSecret")

    def buildApiHeader(self, data):
        now = datetime.datetime.now()
        timestamp_seconds = now.timestamp()
        timestamp_milliseconds = int(timestamp_seconds * 1000)
        signatureMap = {}
        signatureMap["app-key"] = self.appKey
        signatureMap["nonce-str"] = "s0jdIG2w1XFKOdJPFX3iX3DLHtl8Cco4"
        signatureMap["timestamp"] = str(timestamp_milliseconds)
        signatureMap["data"] = data
        # 对字典按键排序
        sorted_data = dict(sorted(signatureMap.items()))
        # 将排序后的字典转换为 JSON 字符串
        data_str = json.dumps(sorted_data, separators=(',', ':'), ensure_ascii=False)
        data_bytes = data_str.encode('utf-8')
        h = hmac.new(self.appSecret.encode('utf-8'), digestmod=hashlib.sha256)
        h.update(data_bytes)
        signatureMap["signature"] = h.hexdigest()
        signatureMap.pop("data")
        return signatureMap

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

    # 走api的形式 需要处理
    def apiPost(self, url, params):
        return HttpUtils.post(self.buildUrl(url), params, self.buildApiHeader(params));

    def checkReqSuccess(self, response):
        return json.loads(response.text)['code'] == 0
