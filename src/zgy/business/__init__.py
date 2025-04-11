import datetime
import hashlib
import hmac
import json

from src.zgy import *
from src.zgy.common import HttpUtils


# 其他服务域名
class CommonParent:
    authorization = "Bearer Eo6YSMXJiiZTXmPASdVZmqZGWAH81c6HsyzBOJC_TlD-ttJW1uK9otV2uxeRfF5X79h84Sft09Wf-_98rVbksX2Vhak-CISaxDzbWAkWcDwY-mKsJwsAVfUYsPBKWvgf"
    cur_env = ""
    localHostPortRelMap = {}
    appKey = ""
    appSecret = ""

    def __init__(self, env, localHostPortRelMap, envAndHostRelMap):
        self.cur_env = env
        self.localHostPortRelMap = localHostPortRelMap
        self.envAndHostRelMap = envAndHostRelMap

    def setAppKey(self, appKeyEnvRelMap):
        self.appKey = appKeyEnvRelMap.get(self.cur_env).get("appKey")
        self.appSecret = appKeyEnvRelMap.get(self.cur_env).get("appSecret")

    def buildApiHeader(self, data):
        now = datetime.datetime.now()
        timestamp_seconds = now.timestamp()
        timestamp_milliseconds = int(timestamp_seconds * 1000)
        signatureMap = {}
        signatureMap["app-key"] = self.appKey
        signatureMap["nonce-str"] = "aQXvVBK37CWRX19NjVsJ8pQuYihjuhZv"
        signatureMap["timestamp"] = str(timestamp_milliseconds)
        signatureMap["data"] = data
        # 对字典按键排序
        sorted_data = dict(sorted(signatureMap.items()))
        # 将排序后的字典转换为 JSON 字符串
        data_str = json.dumps(sorted_data, separators=(',', ':'))
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
