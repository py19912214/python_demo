from src.zgy.business import *

localHostPortRelMap = {
    "/pig-tenant/": "10402",
    "/pig-tenant-cronjob/": "10406"
}
envAndHostRelMap = {
    localHost: localHost_prefix,
    dev: pig_tenant_dev,
    test: pig_tenant_test,
    prod: pig_tenant_prod
}

__cur_env__ = localHost
__tenant_id__ = "2702037874442240000"
__tenant_user_id__ = "271433485926400"


class PigErpManagerTenantParent(CommonParent):
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
