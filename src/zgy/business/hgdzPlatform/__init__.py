import json
import urllib.parse

from src.zgy.business import *

localHostPortRelMap = {
    "/ycshg-ai-service-provider/": "9942"
}
envAndHostRelMap = {
    localHost: localHost_prefix,
    dev: dev_ycshg_ai_service_produce,
    test: test_ycshg_ai_service_produce,
    prod: pig_tenant_prod
}

__cur_env__ = test
# dev
# __tenant_id__ = "3211194104545280000"
# __tenant_user_id__ = "329774037827584"
# test
__tenant_id__ = "3312283985510400000"
__tenant_user_id__ = "342512550313984"


class BaseParent(CommonParent):
    def __init__(self):
        super().__init__(__cur_env__, localHostPortRelMap, envAndHostRelMap)
        self.refreshPigTenantToken()

    def buildGetHeaders(self):
        return {
            'Content-Type': 'application/json',
            'x-tenant-id': __tenant_id__,
            'x-tenant-user-id': __tenant_user_id__,
            'authorization': self.authorization
        }

    def buildPostHeaders(self):
        return {
            'x-tenant-id': __tenant_id__,
            'x-tenant-user-id': __tenant_user_id__,
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
            "loginAccountSystem": "PIG_YCSHG_AI_PLATFORM"
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
