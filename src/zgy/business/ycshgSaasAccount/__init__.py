import urllib.parse

from src.zgy.business import *

localHostPortRelMap = {
    "/hgdz-account-book-external/": "9708",
}

appKeyEnvRelMap = {
    "dev": {
        "appKey": "4awSsox7",
        "appSecret": "48c79557c35ef8c772b035afa860bdf9a365ab24"
    },
    "test": {
        "appKey": "4awSsox7",
        "appSecret": "48c79557c35ef8c772b035afa860bdf9a365ab24"
    }
}

envAndHostRelMap = {
    localHost: localHost_prefix,
    dev: ycshg_jzgj_dev,
    test: ycshg_jzgj_test,
    prod: ycshg_prod
}

__cur_env__ = dev
__x_platform_source__ = '22'
__tenant_id__ = '3265317069619200000'
__tenant_user_id__ = '326531707174917'
__tenant_user_name__ = '123123'


class PigYcshgSaasAccount(CommonParent):
    def __init__(self):
        super().__init__(__cur_env__, localHostPortRelMap, envAndHostRelMap)
        super().setAppKey(appKeyEnvRelMap)

    def buildGetHeaders(self):
        return {
            'Content-Type': 'application/json',
            'x-tenant-Id': __tenant_id__,
            'x-tenant-user-id': __tenant_user_id__,
            "merchantId": "1",
            'token': 'COMPANY_JWT_CT_eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiJDT01QQU5ZX0pXVDMyOTc3NDAzODAwNzgwOCIsInVzZXJJZCI6MzI5Nzc0MDM4MDA3ODA4LCJ1c2VyTmFtZSI6Iua9mOaciCIsImNvbXBhbnlJZCI6MzMxMDU5MzA1NTk0ODgyLCJjb21wYW55TmFtZSI6IuayoeacieeUn-S6p-e7j-iQpeeahOS8geS4miIsImFjY2Vzc01vZGUiOiJDT01NT04iLCJuYXR1cmVUYXhDb2RlIjowLCJuYXR1cmVUYXhOYW1lIjoi5bCP6KeE5qih57qz56iO5Lq6IiwiZXhwIjoxNzQ0MjY4ODMxLCJuYmYiOjE3NDQxODI0MzF9.T1VJxMmQUM7hM0Mrfr5gSi66cYKU0aJy-p7qteBIgrY',
            # 'x-tenant-user-name': __tenant_user_name__,
            'authorization': self.authorization

        }

    def buildPostHeaders(self):
        return {
            'Content-Type': 'application/json',
            'x-tenant-Id': __tenant_id__,
            'x-tenant-user-name': __tenant_user_name__,
            'x-tenant-user-id': __tenant_user_id__,
            "merchantId": "1",
            'token': 'COMPANY_JWT_CT_eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiJDT01QQU5ZX0pXVDMyOTc3NDAzODAwNzgwOCIsInVzZXJJZCI6MzI5Nzc0MDM4MDA3ODA4LCJ1c2VyTmFtZSI6Iua9mOaciCIsImNvbXBhbnlJZCI6MzMxMDU5MzA1NTk0ODgyLCJjb21wYW55TmFtZSI6IuayoeacieeUn-S6p-e7j-iQpeeahOS8geS4miIsImFjY2Vzc01vZGUiOiJDT01NT04iLCJuYXR1cmVUYXhDb2RlIjowLCJuYXR1cmVUYXhOYW1lIjoi5bCP6KeE5qih57qz56iO5Lq6IiwiZXhwIjoxNzQ0MjY4ODMxLCJuYmYiOjE3NDQxODI0MzF9.T1VJxMmQUM7hM0Mrfr5gSi66cYKU0aJy-p7qteBIgrY',
            'authorization': self.authorization
        }

    def refreshPigTenantToken(self):
        headers = {
            'x-platform-source': '22',
            'content-type': 'application/x-www-form-urlencoded'
        }
        params = {
            'grant_type': 'password',
            'loginType': 'password',
            'username': '18482181542',
            'password': 'hXnZTLq0U7Ntz54qI4QItQ=='
        }
        urlParams = urllib.parse.urlencode(params).encode('utf-8')
        host = ycshg_dev
        if (self.cur_env != localHost):
            host = self.getHost()
        response = HttpUtils.post(
            host + "/ycshg-ai-service-provider/nk/tokens/get-token?" + urlParams.decode("utf-8"),
            params,
            headers)
        if (json.loads(response.text)["code"] != 0):
            print("登录失败，无法获取的token:" + json.loads(response.text)["message"])
            return None
        self.authorization = "Bearer " + json.loads(response.text)["data"]["access_token"]
