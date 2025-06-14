import json
import urllib.parse
from urllib.parse import quote

from src.zgy.business import *

localHostPortRelMap = {
    "/ycshg-ai-platform-produce-hgdz-biz/": "9701",
    "/ycshg-ai-platform-produce-hgdz-cronjob/": "9702",
}
envAndHostRelMap = {
    localHost: localHost_prefix,
    dev: hgdz_dev,
    test: hgdz_test,
    prod: hgdz_prod
}

__cur_env__ = test
# test
# __tenant_id__ = '3286941137960960000'
# __tenant_user_id__ = '335072798457856'
# dev
__tenant_id__ = '3211194104545280000'
__tenant_user_id__ = '329774038007808'
__tenant_user_name__ = quote(str('小潘同学123'), encoding='UTF-8')


class PigYcshgAi(CommonParent):
    def __init__(self):
        super().__init__(__cur_env__, localHostPortRelMap, envAndHostRelMap)
        self.refreshPigTenantToken()

    def buildGetHeaders(self):
        return {
            'Content-Type': 'application/json',
            'x-tenant-Id': __tenant_id__,
            'x-tenant-user-id': __tenant_user_id__,
            'x-tenant-user-name': __tenant_user_name__,
            'authorization': self.authorization

        }

    def buildPostHeaders(self):
        return {
            'Content-Type': 'application/json',
            'x-tenant-Id': __tenant_id__,
            'x-tenant-user-name': __tenant_user_name__,
            'x-tenant-user-id': __tenant_user_id__,
            'authorization': self.authorization
        }

    def refreshPigTenantToken(self):
        headers = {
            'x-platform-source': '22',
            'content-type': 'application/x-www-form-urlencoded'
        }
        username = 18482181542
        password = "hXnZTLq0U7Ntz54qI4QItQ=="
        if (self.cur_env == test):
            username = 13982081834
            password = "Ltnn5Hqpu10hkxcn88fMxQ=="
        params = {
            'grant_type': 'password',
            'loginType': 'password',
            'username': username,
            'password': password
        }
        urlParams = urllib.parse.urlencode(params).encode('utf-8')
        host = hgdz_dev
        if (self.cur_env != localHost):
            host = self.getHost()
        response = HttpUtils.post(
            host + "/ycshg-ai-service-provider/nk/tokens/get-token?" + urlParams.decode("utf-8"),
            params,
            headers)
        if (response.status_code != 200):
            print("登录失败，无法获取的token")
            return None
        if (json.loads(response.text)["code"] != 0):
            print("登录失败，无法获取的token:" + json.loads(response.text)["message"])
            return None
        self.authorization = "Bearer " + json.loads(response.text)["data"]["access_token"]
