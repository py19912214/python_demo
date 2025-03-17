import json
import urllib.parse

from src.zgy.business import *

localHostPortRelMap = {
    "/pig-tenant/": "10402",
    "/pig-tenant-cronjob/": "10406"
}
envAndHostRelMap = {
    localHost: localHost_prefix,
    dev: pig_merchant_dev,
    test: pig_merchant_test,
    prod: pig_merchant_prod
}

__cur_env__ = test
__x_platform_source__ = '22'
__corp_id__ = '509600'
__merchant_id__ = '509600'


class PigKjsc(CommonParent):
    def __init__(self):
        super().__init__(__cur_env__, localHostPortRelMap, envAndHostRelMap)
        self.refreshPigTenantToken()

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
