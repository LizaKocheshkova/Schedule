import json
import sqlite3
from pprint import pprint


class Schedule:
    def __init__(self):
        self.data = {}
        with open('Data/all_grades.json', "r", encoding='utf-8') as read_file:
            self.data = json.load(read_file)

    def update_schedule(self):
        with open('Data/all_grades.json', "w", encoding='utf-8') as write_file:
            json.dump(self.data, write_file, indent=2)

    def get_schedule_day(self, day, grage):
        return self.data[grage][day]

    def get_schedule_all(self, grage):
        return self.data[grage]

    def get_list_urok(self):
        urok = sqlite3.connect("Data/us1.db")
        cur = urok.cursor()
        lessons = [el[0] for el in cur.execute("""SELECT les FROM Lesson""").fetchall()]
        return ['не выбран'] +  lessons

    def get_list_teacher(self):
        teacher = sqlite3.connect("Data/us1.db")
        cur = teacher.cursor()
        teachers = [el[0] for el in cur.execute("""SELECT teacher FROM Teacher""").fetchall()]
        return [''] + teachers

    def get_list_grate(self):
        grate = sqlite3.connect("Data/us1.db")
        cur = grate.cursor()
        grates = [el[0] for el in cur.execute("""SELECT class FROM Class""").fetchall()]
        return grates

    def print_sch(self, grade):
        pprint(self.data[grade])

    def copy_schedule(self):
        with open('Data/all_grades_copy.json', "w", encoding='utf-8') as write_file:
            json.dump(self.data, write_file, indent=2)

    def clear_schedule(self):
        self.data = {grade: {
            "Понедельник": {
                "les1": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les2": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les3": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les4": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les5": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les6": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les7": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les8": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                }
            },
            "Вторник": {
                "les1": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les2": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les3": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les4": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les5": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les6": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les7": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les8": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
            },
            "Среда": {
                "les1": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les2": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les3": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les4": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les5": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les6": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les7": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les8": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
            },
            "Четверг": {
                "les1": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les2": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les3": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les4": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les5": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les6": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les7": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les8": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                }
            },
            "Пятница": {
                "les1": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les2": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les3": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les4": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les5": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les6": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les7": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les8": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
            },
            "Суббота": {
                "les1": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les2": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les3": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les4": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les5": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les6": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les7": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les8": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
            },
        }
            for grade in (self.get_list_grate())}

    def clear_schedule_grade(self, grade):
        self.data[grade] = {
            "Понедельник": {
                "les1": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les2": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les3": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les4": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les5": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les6": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les7": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les8": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                }
            },
            "Вторник": {
                "les1": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les2": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les3": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les4": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les5": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les6": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les7": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les8": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
            },
            "Среда": {
                "les1": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les2": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les3": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les4": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les5": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les6": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les7": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les8": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
            },
            "Четверг": {
                "les1": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les2": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les3": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les4": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les5": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les6": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les7": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les8": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                }
            },
            "Пятница": {
                "les1": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les2": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les3": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les4": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les5": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les6": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les7": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les8": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
            },
            "Суббота": {
                "les1": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les2": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les3": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les4": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les5": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les6": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les7": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
                "les8": {
                    "urok": "нет урока",
                    "th": "",
                    "auditorium": ""
                },
            },
        }

    def update_in_copy(self):
        with open('Data/all_grades_copy.json', "r", encoding='utf-8') as read_file:
            self.data = json.load(read_file)



