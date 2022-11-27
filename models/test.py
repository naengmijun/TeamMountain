import pandas as pd
import numpy as np


def createTodoList():
    global todoList
    todoList = pd.DataFrame(columns=['todo', '중요도', '사람', '완료여부'])
    todoList.index = todoList.index + 1


def addTodoList(todo, importance):
    global todoList
    record = pd.Series(
        {'todo': todo, '중요도': importance, '사람': None, '완료여부': 'X'})
    todoList = todoList.append(record, ignore_index=True)


createTodoList()
addTodoList('먹기', 3)
addTodoList('자기', 2)
addTodoList('과제', 4)
print(todoList)
