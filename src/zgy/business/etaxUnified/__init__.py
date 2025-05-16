from src.zgy.business import *

localHostPortRelMap = {
    "/invoice-cloud-platform/": "9715",
    "/pig-tax-platform/": "10188",
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
    dev: etax_unified_dex,
    test: etax_unified_text,
    prod: ycshg_prod
}

__cur_env__ = dev


class SignalService(CommonParent):
    def __init__(self):
        super().__init__(__cur_env__, localHostPortRelMap, envAndHostRelMap)
        super().setAppKey(appKeyEnvRelMap)

    def buildGetHeaders(self):
        return {
            'Content-Type': 'application/json',
        }

    def buildPostHeaders(self):
        return {
            'Content-Type': 'application/json',
        }
