from src.zgy.common import HttpUtils

# 定义URL
localHost = 'http://localhost:10402'
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
__authorization__ = 'Bearer bYJSxib0W9bhqFhlAR5x2xtYPNuApREcGIOE5cz4OwFCFJTzpqm1Sq0fi62cW9Qq_6UJBftmS2eJ-FoYvgrRUOoIU0rJoi4PvwpdQDjO5F6YsIL0STVC_QdKZ3_dkOPC'


class PigErpManagerTenantParent:
    def __init__(self):
        self.message = "This is from the parent class."

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
