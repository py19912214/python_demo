import urllib.parse
from urllib.parse import quote

from src.zgy.business import *

localHostPortRelMap = {
    "/ycshg-saas-individual-tax-cronjob/": "9704",
}
appKeyEnvRelMap = {
    "dev": {
        "appKey": "v2DWgfMY",
        "appSecret": "3ac02ac2ceb3a09cfd1f24f85d8ef1cfc45442c1"
    },
    "test": {
        "appKey": "v2DWgfMY",
        "appSecret": "3ac02ac2ceb3a09cfd1f24f85d8ef1cfc45442c1"
    }
}
envAndHostRelMap = {
    localHost: localHost_prefix,
    dev: ycshg_gsgj_dev,
    test: ycshg_gsgj_test,
    prod: ycshg_prod
}

__cur_env__ = localHost
__x_platform_source__ = '22'
__tenant_id__ = '3265317069619200000'
__tenant_user_id__ = '326531707174917'
__tenant_user_name__ = quote(str('小潘同学123'), encoding='UTF-8')


class PigYcshgSaasIndividualBiz(CommonParent):
    def __init__(self):
        super().__init__(__cur_env__, localHostPortRelMap, envAndHostRelMap)
        super().setAppKey(appKeyEnvRelMap)


class PigYcshgSaasIndividualCronJob(CommonParent):
    def __init__(self):
        super().__init__(__cur_env__, localHostPortRelMap, envAndHostRelMap)
        # super().setAppKey(appKeyEnvRelMap)
        self.refreshPigTenantToken()

    def buildGetHeaders(self):
        return {
            'Content-Type': 'application/json',
            "merchantId": "1",
            'token': 'COMPANY_JWT_CT_eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiJDT01QQU5ZX0pXVDMyOTc3NDAzODAwNzgwOCIsInVzZXJJZCI6MzI5Nzc0MDM4MDA3ODA4LCJ1c2VyTmFtZSI6Iua9mOaciCIsImNvbXBhbnlJZCI6MzMxMDU5MzA1NTk0ODgyLCJjb21wYW55TmFtZSI6IuayoeacieeUn-S6p-e7j-iQpeeahOS8geS4miIsImFjY2Vzc01vZGUiOiJDT01NT04iLCJuYXR1cmVUYXhDb2RlIjowLCJuYXR1cmVUYXhOYW1lIjoi5bCP6KeE5qih57qz56iO5Lq6IiwiZXhwIjoxNzQ0MjY4ODMxLCJuYmYiOjE3NDQxODI0MzF9.T1VJxMmQUM7hM0Mrfr5gSi66cYKU0aJy-p7qteBIgrY',
            'authorization': self.authorization
        }

    def buildPostHeaders(self):
        return {
            'Content-Type': 'application/json',
            "merchantId": "1",
            'token': 'COMPANY_JWT_CT_eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiJDT01QQU5ZX0pXVDMyOTc3NDAzODAwNzgwOCIsInVzZXJJZCI6MzI5Nzc0MDM4MDA3ODA4LCJ1c2VyTmFtZSI6Iua9mOaciCIsImNvbXBhbnlJZCI6MzMxMDU5MzA1NTk0ODgyLCJjb21wYW55TmFtZSI6IuayoeacieeUn-S6p-e7j-iQpeeahOS8geS4miIsImFjY2Vzc01vZGUiOiJDT01NT04iLCJuYXR1cmVUYXhDb2RlIjowLCJuYXR1cmVUYXhOYW1lIjoi5bCP6KeE5qih57qz56iO5Lq6IiwiZXhwIjoxNzQ0MjY4ODMxLCJuYmYiOjE3NDQxODI0MzF9.T1VJxMmQUM7hM0Mrfr5gSi66cYKU0aJy-p7qteBIgrY',
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
        host = ycshg_dev
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
