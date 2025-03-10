from src.zgy.common import HttpUtils
import urllib.parse
import json

# 定义URL
localHost = 'http://localhost:'
dev = 'http://dev-erp.joolgo.cn/api'
test = 'http://test-erp.joolgo.cn/api'
prod = 'http://dev-erp.joolgo.cn/api'

__localHost__ = 'local'
__dev__ = 'dev'
__test__ = 'test'
__prod__ = 'prod'

__cur_env__ = __dev__

__tenant_id__ = "2600908777226240000"
__tenant_user_id__ = "275644734783493"
__authorization__ = 'Bearer ECO5dYq5ULU2t5SGbRLJgrXh4oz3cm23twUjhnIMZ9CCI1P8zmW5UbhW9gLsb7yMivd-239E1hgmpHrUOnENCyOXdO-vh8crVgZ0lSA6-17WCSjrlLe-vPdRWfXTqItW'


class PigErpManagerTenantParent:
    def __init__(self):
        self.message = "This is from the parent class."
        self.refreshToken();

    def refreshToken(self):
        headers = {
            'authorization': 'Basic d2ViQXBwOndlYkFwcA==',
            'content-type': 'application/x-www-form-urlencoded'
        }
        params = {
            "grant_type": "password",
            "loginType": "password",
            "username": "13111867801",
            "password": "AwxsbzgJZhnxlPjnfTbHNA==",
            "loginAccountSystem": "PIG_TENANT"
        }
        urlParams = urllib.parse.urlencode(params).encode('utf-8')
        response = HttpUtils.post(
            "http://dev-erp.joolgo.cn/api/api-uaa/oauth/token?" + urlParams.decode("utf-8"),
            params,
            headers)
        __authorization__ = "Bearer " + json.loads(response.text)['data']['access_token']

    def getHost(self):
        if __cur_env__ == __localHost__:
            return localHost;
        if __cur_env__ == __prod__:
            return prod;
        elif __cur_env__ == __test__:
            return test;
        else:
            return dev;

    def buildUrl(self, url):
        if __cur_env__ == __localHost__:
            if url.startswith('/pig-tenant-cronjob'):
                url = "10406" + url.replace("/pig-tenant-cronjob", "")
            if url.startswith('/pig-tenant'):
                url = "10402" + url.replace("/pig-tenant", "")
        return self.getHost() + url;

    def get(self, url, params):
        headers = {
            'x-tenant-id': __tenant_id__,
            'x-tenant-user-id': __tenant_user_id__,
            'authorization': __authorization__
        }
        return HttpUtils.get(self.buildUrl(url), params, headers);

    def post(self, url, params):
        headers = {
            'Content-Type': 'application/json',
            'x-tenant-id': __tenant_id__,
            'x-tenant-user-id': __tenant_user_id__,
            'authorization': __authorization__
        }
        return HttpUtils.post(self.buildUrl(url), params, headers);
