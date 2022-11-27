import numpy as np
import pandas as pd
import json

from models.User import Student


class Team:
    def __init__(self, teamNum):
        with open(f"./databases/groups.json", encoding='UTF-8') as f:
            groups = json.load(f)

        self.teamNum = teamNum
        self.name = groups[teamNum]["name"]
        self.membersName = groups[teamNum]["members"]
        self.membersClass = []
        self.score = groups[teamNum]["score"]
        self.timeTable = self.createEmptyDF()
        self.todoList = []

    def createEmptyDF(self):
        myArr = np.zeros((15, 7))
        time = pd.Series(['09:00 ~ 10:00', '10:00 ~ 11:00', '11:00 ~ 12:00', '12:00 ~ 13:00', '13:00 ~ 14:00', '14:00 ~ 15:00', '15:00 ~ 16:00',
                          '16:00 ~ 17:00', '17:00 ~ 18:00', '18:00 ~ 19:00', '19:00 ~ 20:00', '20:00 ~ 21:00', '21:00 ~ 22:00', '22:00 ~ 23:00', '23:00 ~ 24:00'])
        timeTable = pd.DataFrame(
            myArr, columns=['월', '화', '수', '목', '금', '토', '일'])
        timeTable = timeTable.set_index(time)
        return timeTable

    def addTime(self, impossibleTime):
        if impossibleTime == '0':
            return
        else:
            impossibleTime = impossibleTime.split()
            impossibleTime[1] = impossibleTime[1].split('~')
            impossibleTime[1][0] = impossibleTime[1][0].strip()
            self.timeTable.loc[impossibleTime[1][0]                               :impossibleTime[3], impossibleTime[0]] = 1
            return self.timeTable

    def addMemberClass(self):
        for name in self.membersName:
            self.membersClass.append(Student(name, self))

    def matchTime(self):
        self.timeTable = self.createEmptyDF()
        for member in self.membersClass:
            self.timeTable += member.timeTable
        print(self.timeTable)

    def createTodoList(self):
        self.todoList = pd.DataFrame(columns=['todo', '중요도', '사람', '완료여부'])
        self.todoList.index = self.todoList.index + 1

    def addTodoList(self, todo, importance):
        record = pd.Series(
            {'todo': todo, '중요도': importance, '사람': None, '완료여부': 'X'})
        self.todoList = self.todoList.append(record, ignore_index=True)

    def completeTodoList(self, todo):
        self.todoList.loc[todo, '완료여부'] = 'O'
