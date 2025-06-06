import json
import urllib.parse

from src.zgy.business import *

localHostPortRelMap = {
    "/qhs-platform-cronjob/": "9921",
    "/qhs-platform-manage/": "9922",
}
envAndHostRelMap = {
    localHost: localHost_prefix,
    dev: qhs_platform_dev,
    test: qhs_platform_test,
    prod: ycshg_prod
}

__cur_env__ = test
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
            'authorization': 'Basic cWhzTWFuYWdlV2ViQXBwOnFoc01hbmFnZVdlYkFwcA==',
            'content-type': 'application/x-www-form-urlencoded'
        }
        params = {
            "grant_type": "password",
            "loginType": "password",
            "username": "13982081834",
            "password": "Ltnn5Hqpu10hkxcn88fMxQ==",
            "loginAccountSystem": "QHS_MANAGE"
        }
        urlParams = urllib.parse.urlencode(params).encode('utf-8')
        host = qhs_platform_test
        if (self.cur_env != localHost):
            host = self.getHost()
        response = HttpUtils.post(
            host + "/api-uaa/oauth/token?" + urlParams.decode("utf-8"),
            params,
            headers)
        self.authorization = "Bearer " + json.loads(response.text)['data']['access`_token']
