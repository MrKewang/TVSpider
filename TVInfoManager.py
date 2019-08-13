import request
import re
from TVInfo import TVInfoModel

class TVInfoManager(request.RequestDelegate):
    def __init__(self):
        self.__request = request.Request(self)

    def download(self, url):
        self.__request.request(url)

    def receive_data(self, data):
        self.analyze_data(data)

    def analyze_data(self, data):
        info = TVInfoModel()

        patten = '"name": "(.*)",\\n  "url":'
        ret = re.search(patten, data)
        info.set__name(str(ret.group(1)))

        patten = '"director":(.*)"author":'
        ret = re.search(patten, data, re.S)
        ls = ret.group(1).split("}")
        for i in ls[:-1]:
            patten = '"name": "(.*)"'
            ret = re.search(patten, i, re.S)
            info.add__director(ret.group(1))

        patten = '"actor":(.*)"datePublished":'
        ret = re.search(patten, data, re.S)
        ls = ret.group(1).split("}")
        for i in ls[:-1]:
            patten = '"name": "(.*)"'
            ret = re.search(patten, i, re.S)
            info.add__actor(ret.group(1))

        patten = '"ratingValue": "(.*)"'
        ret = re.search(patten, data)
        info.set__score(float(ret.group(1)))

        patten = '"description": "(.*)",\\n  "@type": "TVSeries",'
        ret = re.search(patten, data)
        info.set__sortInfo(str(ret.group(1)))

        print(info)

path = "https://movie.douban.com/subject/27052168/"
mim = TVInfoManager()
mim.download(path)

