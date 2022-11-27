import numpy as np
import pandas as pd
import json


class Student:
    def __init__(self, name, team):
        self.name = name
        if name == "temp":
            self.timeTable = self.createEmptyDF()
            return
        self.getTimeTable()
        self.team = team
        self.leader = False

    def getTeamName(self):
        with open(f"./databases/users.json", encoding='UTF-8') as f:
            users = json.load(f)
        with open(f"./databases/groups.json", encoding='UTF-8') as f:
            groups = json.load(f)
        return groups[users[self.name]["group"]]["name"]

    def getTimeTable(self):
        with open(f"./databases/users.json", encoding='UTF-8') as f:
            users = json.load(f)
        times = users[self.name]["timeTable"]
        self.timeTable = self.createEmptyDF()
        for time in times:
            self.addTime(time)

    def setTimeTable(self, impossibleTime):
        with open(f"./databases/users.json", encoding='UTF-8') as f:
            users = json.load(f)
        users[self.name]["timeTable"] = impossibleTime
        with open(f"./databases/users.json", "w", encoding="utf-8") as f:
            json.dump(users, f, indent=4, ensure_ascii=False)

    def addTime(self, impossibleTime):
        if impossibleTime == '0':
            return
        else:
            impossibleTime = impossibleTime.split()
            impossibleTime[1] = impossibleTime[1].split('~')
            impossibleTime[1][0] = impossibleTime[1][0].strip()
            self.timeTable.loc[impossibleTime[1][0]
                :impossibleTime[3], impossibleTime[0]] = 1
            return self.timeTable

    def createEmptyDF(self):
        myArr = np.zeros((15, 7))
        time = pd.Series(['09:00 ~ 10:00', '10:00 ~ 11:00', '11:00 ~ 12:00', '12:00 ~ 13:00', '13:00 ~ 14:00', '14:00 ~ 15:00', '15:00 ~ 16:00',
                          '16:00 ~ 17:00', '17:00 ~ 18:00', '18:00 ~ 19:00', '19:00 ~ 20:00', '20:00 ~ 21:00', '21:00 ~ 22:00', '22:00 ~ 23:00', '23:00 ~ 24:00'])
        timeTable = pd.DataFrame(
            myArr, columns=['월', '화', '수', '목', '금', '토', '일'])
        timeTable = timeTable.set_index(time)
        return timeTable

    def matchTime(self):
        self.team.timeTable = self.team.createEmptyDF()
        for member in self.team.membersClass:
            self.team.timeTable = self.team.timeTable + member.timeTable


class Professor:
    def __init__(self, name):
        self.name = name
