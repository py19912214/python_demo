import datetime


class CommonUtils():
    def createTaxNo(self):
        now = datetime.datetime.now()
        print("当前日期和时间:", now)
        formatted_now = now.strftime("%Y%m%d%H%M%S")
        print("格式化后的当前日期和时间:", formatted_now)
        return '9131' + formatted_now + 'T';

    def createEnterpriseName(self):
        now = datetime.datetime.now()
        print("当前日期和时间:", now)
        formatted_now = now.strftime("%Y%m%d%H%M")
        print("格式化后的当前日期和时间:", formatted_now)
        return '小潘测试(' + formatted_now + '001)';


# utils = CommonUtils()
# # print(utils.createTaxNo())
# print(utils.createEnterpriseName())
