from src.zgy.business import *


class ProcessService():

    def get_provider_token(self):
        data = {
            "corpid": "wwb06f093b2f0cb1db",
            "provider_secret": "0EIT9p_b1APDWpdAoDc8hUWfj2WepwP6S3gOtAIn8Lp4h_4hkOhUY7TfhNFVtgv_"
        }
        response = HttpUtils.post('https://qyapi.weixin.qq.com/cgi-bin/service/get_provider_token', data, {});

        print(response.text)

    def corpid_to_opencorpid(self, token):
        data = {
            "corpid": "wwb06f093b2f0cb1db"
        }
        response = HttpUtils.post(
            'https://qyapi.weixin.qq.com/cgi-bin/service/corpid_to_opencorpid?provider_access_token=' + token
            , data, {});

        print(response.text)

    def gettoken(self):
        # 测试环境需要用这个
        corpid = "ww52b10d6f0764aabb"
        provider_secret = "6D98KGJ7QLwwBefEBUQVzq2ssL9s2tGuXm0yxphJv7M"
        data = {
        }
        response = HttpUtils.post(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + provider_secret
            , data, {});

        print(response.text)

    def get_suite_token(self):
        # 测试环境需要用这个
        data = {
            "suite_id": "dkd49c12207bd1a5b4",
            "suite_secret": "iJzZ-rknsQ8mEYKwi8CE-V18xnDCBH0gmsh3_2JsEJg",
            "suite_ticket": "KRLki0IpI8fO3wfL6vCQF1s2BTeU0MubZpVPaqW7XeMQYZ2HYYAkFucg7T_bVHyD"
        }
        # suite_ticket 是从redis里面取得 ycs:webchat:qywx:corpId:suite:ticket
        response = HttpUtils.post(
            'https://qyapi.weixin.qq.com/cgi-bin/service/get_suite_token'
            , data, {});

        print(response.text)

    def get_pre_auth_code(self, suite_access_token):
        # 测试环境需要用这个
        data = {
        }
        response = HttpUtils.get(
            'https://qyapi.weixin.qq.com/cgi-bin/service/get_pre_auth_code?suite_access_token=' + suite_access_token
            , data, {});

        print(response.text)

    def get_permanent_code(self, suite_access_token):
        data = {
            "auth_code": "临时授权码"
        }
        response = HttpUtils.get(
            ' https://qyapi.weixin.qq.com/cgi-bin/service/v2/get_permanent_code?suite_access_token=' + suite_access_token
            , data, {});

        print(response.text)

    def getuserid(self, access_token):
        data = {
            "mobile": "13982081834"
        }
        response = HttpUtils.get(
            'https://qyapi.weixin.qq.com/cgi-bin/service/v2/get_permanent_code?access_token=' + access_token
            , data, {});

        print(response.text)

    def get_corp_token(self, suite_access_token):
        data = {
            "auth_corpid": "ww52b10d6f0764aabb",
            "permanent_code": "5cGk-TliyWOjaLxHXpLo8kfiMz30LRql7TUiGnh38MM"
        }
        response = HttpUtils.get(
            'https://qyapi.weixin.qq.com/cgi-bin/service/get_corp_token?suite_access_token=?suite_access_token=' + suite_access_token
            , data
            , {});

        print(response)
        print(response.text)


processService = ProcessService()
# processService.get_provider_token()
# token = "QWaly0blbTvVLmH1B1exuFLr-u2pp94f6-W0ChwclD1wbjjTIE5bcCfjiJFe-QFo7rYqpw2koJCvUmB5mBzSakfK06GpSUC6UOq0YQoIjpeLygzfCwwjfcTsbtnyIgV8";
# processService.corpid_to_opencorpid(token)
# 获取token信息
# processService.gettoken()
# 获取第三方应用凭证
# processService.get_suite_token()
# 获取预售码 get_suite_token 返回的
suite_access_token = "WmI5uCo2mNasWx3k1vSTg3b0Onz-Ea4vR5Hm_exKSqjEK_631ZAQ2JAQEoy66rOGzAQWYRLYbBSzl4ruO7vnKgMLe2KNKxkl6nMGYewQmgnnygeFHesYz7lR-x_G6ze3"
# 获取临时授权码  现在接口时调不通的
# processService.get_pre_auth_code(suite_access_token)
# 获取永久授权码
# processService.get_permanent_code(suite_access_token)
# 获取用户userId
# processService.getuserid(suite_access_token)
# 获取企业得token
processService.get_corp_token(suite_access_token)
