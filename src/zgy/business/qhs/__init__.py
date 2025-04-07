import json
import urllib.parse

from src.zgy.business import *

localHostPortRelMap = {
    "/qhs-platform-cronjob/": "9921",
    "/qhs-platform-cronjo2/": "9921",
}
envAndHostRelMap = {
    localHost: localHost_prefix,
    dev: ycshg_dev,
    test: ycshg_test,
    prod: ycshg_prod
}

__cur_env__ = localHost
__x_platform_source__ = '22'
__corp_id__ = '509600'
__merchant_id__ = '509600'


class PigQhs(CommonParent):
    def __init__(self):
        super().__init__(__cur_env__, localHostPortRelMap, envAndHostRelMap)
        # self.refreshPigTenantToken()

    def buildGetHeaders(self):
        return {
            'Content-Type': 'application/json',
            'x-platform-source': __x_platform_source__,
            'x-corp-id': __corp_id__,
            'x-merchant-id': __merchant_id__,
            'authorization': self.authorization

        }

    def buildPostHeaders(self):
        return {
            'Content-Type': 'application/json',
            'x-platform-source': __x_platform_source__,
            'x-corp-id': __corp_id__,
            'x-merchant-id': __merchant_id__,
            'authorization': self.authorization
        }

    def refreshPigTenantToken(self):
        headers = {
            'x-platform-source': '22',
            'content-type': 'application/x-www-form-urlencoded'
        }
        params = {
            'username': '13688387776',
            'password': 'wzwasGUHMlkisR3m20Q5RQ=='
        }
        urlParams = urllib.parse.urlencode(params).encode('utf-8')
        host = pig_merchant_dev
        if (self.cur_env != localHost):
            host = self.getHost()
        response = HttpUtils.post(
            host + "/sys/login?" + urlParams.decode("utf-8"),
            params,
            headers)
        self.authorization = "Bearer " + json.loads(response.text)['access_token']
