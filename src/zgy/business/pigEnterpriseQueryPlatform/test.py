from src.zgy.common import HttpUtils


class Test:
    def processData(self):
        data = {
            "threadNumList": [1],
            "total": 1,
            "startIndex": 10000000
        }
        response = HttpUtils.post("http://localhost:9944/nk/enterprise/qxy-sync/v1/qps-test", data, {});
        print(response.text)

    def filterData(self):
        data = {
        }
        response = HttpUtils.get("http://localhost:9944/nk/enterprise/qxy-sync/v1/migrate-to-mongodb", data, {});
        print(response.text)

    def startTask(self):
        data = {
            "threads": 1
        }
        response = HttpUtils.get("http://localhost:9944/nk/enterprise/qxy-task/v1/task", data, {});
        print(response.text)


test = Test()
# test.processData()
# test.filterData()
test.startTask()
