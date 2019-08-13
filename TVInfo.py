class TVInfoModel:
    def __init__(self):
        self.__name = None
        self.__director_list = []
        self.__actor_list = []
        self.__score = 0
        self.__sortInfo = None

    def set__name(self,name):
        self.__name = name

    def add__director(self, director):
        self.__director_list.append(director)

    def add__actor(self, actor):
        self.__actor_list.append(actor)

    def set__score(self, score):
        self.__score = score

    def set__sortInfo(self, sortInfo):
        self.__sortInfo = sortInfo

    def __repr__(self):
        director_list = "/".join(self.__director_list)
        actor_list = "/".join(self.__actor_list)

        s = "剧名：{}\n导演：{}\n主演：{}\n评分：{}\n简介：{}\n".format(self.__name, self.__director_list, self.__actor_list,
                                                self.__score, self.__sortInfo)

        return s