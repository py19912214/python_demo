from src.zgy.business import *

localHostPortRelMap = {
    "/pig_rpa_gs_task_robot/": "9650"
}
envAndHostRelMap = {
    localHost: localHost_prefix,
    dev: pig_tenant_dev,
    test: pig_tenant_test,
    prod: pig_tenant_prod
}

__cur_env__ = dev
__tenant_id__ = "2702037874442240000"
__tenant_user_id__ = "271433485926400"


class PigRpaGsAnnualReport(CommonParent):
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
