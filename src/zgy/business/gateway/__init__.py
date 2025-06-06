import urllib.parse

from src.zgy.business import *

localHostPortRelMap = {
    "/pig-cloud-gateway/": "19999"
}
envAndHostRelMap = {
    localHost: localHost_prefix,
    dev: dev_ycshg_ai_app_service,
    test: test_ycshg_ai_app_service,
    prod: pig_tenant_prod
}

__cur_env__ = localHost


class BaseParent(CommonParent):
    def __init__(self):
        super().__init__(__cur_env__, localHostPortRelMap, envAndHostRelMap)
        # self.refreshPigTenantToken()

    def buildGetHeaders(self):
        return {
            'Content-Type': 'application/json',
            'authorization': self.authorization
        }

    def buildPostHeaders(self):
        return {
            'authorization': self.authorization
        }

    def refreshPigTenantToken(self):
        headers = {
            'authorization': 'Basic d2ViQXBwOndlYkFwcA==',
            'content-type': 'application/x-www-form-urlencoded'
        }
        params = {
            "grant_type": "password",
            "loginType": "password",
            "username": "13982081834",
            "password": "Ltnn5Hqpu10hkxcn88fMxQ==",
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
