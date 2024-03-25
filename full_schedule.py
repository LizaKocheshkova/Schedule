import sys

from PyQt5.QtGui import QIcon
from Data.CRUD_json import Schedule
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QInputDialog, QMessageBox
from PyQt5.QtWidgets import QPushButton, QLabel, QComboBox, QLineEdit
from form_day import Ui_Schedule_for_the_day


class MainWindow(QMainWindow):
    bttnStyle = '''color: black; background-color: {};'''

    def __init__(self):
        super().__init__()
        self.grade = '9г4'
        self.setWindowTitle(f"Расписание группы {self.grade} на неделю")
        self.setWindowIcon(QIcon('logo.png'))
        self.setFixedSize(1200, 750)
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(background.jpg)}")
        self.schedule = Schedule()
        self.schedule_1 = self.get_schel(self.grade)
        self.dict_widget = dict()
        self.group_bttn_class = list()
        self.btn_admin = QPushButton("Редактировать", self)
        self.btn_admin.resize(100, 30)
        self.btn_admin.move(1100, 10)
        self.btn_admin.clicked.connect(self.open_adminwind)

        for i, grade in enumerate(self.schedule.get_list_grate()):
            self.group_bttn_class.append(QPushButton(grade, self))
            self.group_bttn_class[i].resize(45, 30)
            self.group_bttn_class[i].move(5 + i * 45, 10)
            if self.grade == grade:
                # изменить цвет кнопки
                self.group_bttn_class[i].setStyleSheet(self.bttnStyle.format('red'))
            self.group_bttn_class[i].clicked.connect(self.choise_grade)

        for i in range(3):
            for j in range(2):
                self.dict_widget[i + j * 3] = [
                    QPushButton(self.schedule_1[i + j * 3][0], self),
                    [[QLabel(f'урок{k + 1}:', self),
                      QLabel(self)]for k in range(8)]
                ]
                self.dict_widget[i + j * 3][0].move(125 + i * 400, 45 + j * 360)
                self.dict_widget[i + j * 3][0].clicked.connect(self.open_day)
                for n, el in enumerate(self.dict_widget[i + j * 3][1]):
                    el[0].resize(50, 15)
                    el[0].move(100 + i * 400, 85 + j * 370 + 35 * n)
                    el[1].resize(250, 15)
                    el[1].move(140 + i * 400, 85 + j * 370 + 35 * n)
        self.update_centr_aria()

    def update_centr_aria(self):
        for i in range(3):
            for j in range(2):
                for n, el in enumerate(self.dict_widget[i + j * 3][1]):
                    el[1].setText(self.schedule_1[i + j * 3][1][n])

    def get_schel(self, grade):
        sch = self.schedule.get_schedule_all(grade)
        temp = {i: [key,
                    [sch[key][les]['urok'] for les in sch[key]]]
                for i, key in enumerate(sch.keys())}
        return temp

    def open_adminwind(self):
        password, ok_pressed = QInputDialog.getText(self, "Редактирование", "Введите пароль")
        if ok_pressed:
            if password == '0000':
                self.adm = AdminWindow(self.schedule, self.grade)
                self.adm.show()
                self.hide()
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setWindowTitle("Неверный пароль!!!")
                msgBox.setText("Неверный пароль!!!")
                msgBox.exec()

    def open_day(self):
        self.v = Day(self.schedule, self.grade, self.sender().text())
        self.v.show()

    def choise_grade(self):
        for bttn in self.group_bttn_class:
            bttn.setStyleSheet(self.bttnStyle)
        self.grade = self.sender().text()
        self.setWindowTitle(f"Расписание группы {self.grade} на неделю")
        self.sender().setStyleSheet(self.bttnStyle.format('red'))
        self.schedule_1 = self.get_schel(self.grade)
        self.update_centr_aria()


class AdminWindow(QWidget):
    def __init__(self, sch, grade):
        super().__init__()
        self.grade = grade
        self.list_days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота")
        self.setWindowTitle(f"Изменить расписание на неделю для группы {self.grade}")
        self.setGeometry(100, 100, 1200, 850)
        self.setWindowIcon(QIcon('logo.png'))
        self.setObjectName("AdminWindow")
        self.setStyleSheet("#AdminWindow{border-image:url(background.jpg)}")
        self.schedule = sch
        self.schedule_1 = self.schedule.get_schedule_all(grade)
        self.dict_widget = dict()
        self.list_class = self.schedule.get_list_grate()
        self.list_urok = self.schedule.get_list_urok()
        self.list_teather = self.schedule.get_list_teacher()
        self.initUi()
        self.create_centr_aria()
        self.update_schedule()

    def initUi(self):
        self.grate_selection = QLabel("Выберите\nкласс", self)
        self.grate_selection.move(40, 775)
        self.grates = QComboBox(self)
        self.grates.resize(75, 25)
        self.grates.move(100, 775)
        self.btn_choise = QPushButton("Выбрать", self)
        self.btn_choise.resize(70, 25)
        self.btn_choise.move(175, 775)
        self.clear_grade = QPushButton("Очистить рассписание\nгруппы", self)
        self.clear_grade.resize(150, 50)
        self.clear_grade.move(250, 775)
        self.clear_all = QPushButton("Очистить все", self)
        self.clear_all.resize(150, 50)
        self.clear_all.move(405, 775)
        self.create_copy = QPushButton("Создать резервную\nкопию", self)
        self.create_copy.resize(150, 50)
        self.create_copy.move(560, 775)
        self.download = QPushButton("Загрузить из\nрезервной копии", self)
        self.download.resize(150, 50)
        self.download.move(715, 775)
        self.save = QPushButton("Сохранить", self)
        self.save.resize(150, 50)
        self.save.move(870, 775)
        self.cansel = QPushButton("Отмена", self)
        self.cansel.resize(150, 50)
        self.cansel.move(1025, 775)
        self.grates.addItems(self.list_class)
        self.grates.setCurrentText(self.grade)
        self.cansel.clicked.connect(self.open_full_schedule)
        self.save.clicked.connect(self.save_schedule)
        self.btn_choise.clicked.connect(self.choise_grade)
        self.create_copy.clicked.connect(self.create_copy_shl)
        self.clear_grade.clicked.connect(self.clear_grade_shl)
        self.clear_all.clicked.connect(self.clear_all_shl)

    def create_centr_aria(self):
        for i in range(3):
            for j in range(2):
                self.dict_widget[i + j * 3] = [
                    QLabel(self.list_days[i + j * 3], self),
                    [[QLabel(f'урок{k + 1}:', self),
                      QComboBox(self),
                      QComboBox(self),
                      QLineEdit(self)] for k in range(8)]
                ]
                self.dict_widget[i + j * 3][0].move(200 + i * 400, 25 + j * 360)
                for n, el in enumerate(self.dict_widget[i + j * 3][1]):
                    el[0].move(100 + i * 400, 45 + j * 370 + 40 * n)
                    el[1].resize(200, 20)
                    el[1].move(140 + i * 400, 45 + j * 370 + 40 * n)
                    el[1].addItems(self.list_urok)
                    el[2].resize(200, 20)
                    el[2].move(140 + i * 400, 65 + j * 370 + 40 * n)
                    el[2].addItems(self.list_teather)
                    el[3].resize(40, 40)
                    el[3].move(340 + i * 400, 45 + j * 370 + 40 * n)

    def update_schedule(self):
        self.schedule_1 = self.schedule.get_schedule_all(self.grade)
        list_les = ['les1', 'les2', 'les3', 'les4', 'les5', 'les6', 'les7', 'les8', ]
        for i_day in self.dict_widget:
            for i_les in range(8):
                self.dict_widget[i_day][1][i_les][1].setCurrentText(self.schedule_1[self.list_days[i_day]][list_les[i_les]]["urok"])
                self.dict_widget[i_day][1][i_les][2].setCurrentText(self.schedule_1[self.list_days[i_day]][list_les[i_les]]["th"])
                self.dict_widget[i_day][1][i_les][3].setText(self.schedule_1[self.list_days[i_day]][list_les[i_les]]["auditorium"])

    def open_full_schedule(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Закончить редактирование")
        msg.setText("Вы действительно хотите уйти?\n Не сохраненные изменения будут утеряны!")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if msg.exec() == 1024:
            self.full_schedule = MainWindow()
            self.full_schedule.show()
            self.hide()

    def choise_grade(self):
        self.grade = self.grates.currentText()
        self.setWindowTitle(f"Изменить расписание на неделю для группы {self.grade}")
        self.update_schedule()

    def save_schedule(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Закончить редактирование")
        msg.setText("Вы действительно сохранить изменения?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        if msg.exec() == 1024:
            for i_day in self.dict_widget:
                for i in range(8):
                    self.schedule_1[self.list_days[i_day]][f"les{i + 1}"]["urok"] = self.dict_widget[i_day][1][i][1].currentText()
                    self.schedule_1[self.list_days[i_day]][f"les{i + 1}"]["th"] = self.dict_widget[i_day][1][i][2].currentText()
                    self.schedule_1[self.list_days[i_day]][f"les{i + 1}"]["auditorium"] = self.dict_widget[i_day][1][i][3].text()
            self.schedule.update_schedule()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Изменения небыли сохранены!")
            msg.exec()

    def create_copy_shl(self):
        self.schedule.copy_schedule()

    def clear_grade_shl(self):
        self.schedule.clear_schedule_grade(self.grade)
        self.update_schedule()

    def clear_all_shl(self):
        self.schedule.clear_schedule()
        self.update_schedule()


class Day(QWidget, Ui_Schedule_for_the_day):
    def __init__(self, sch, grade, day: str):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('logo.png'))
        self.grade = grade
        self.day = day
        self.schedule = sch
        self.schedule_day = self.schedule.get_schedule_day(day, grade)
        self.initUI(day)

    def initUI(self, day: str):
        self.setWindowTitle(f"{day} {self.grade}")
        self.day_week.setText(day)
        self.lesson_1.setText(self.schedule_day["les1"]["urok"])
        self.Teacher_1.setText(self.schedule_day["les1"]["th"])
        self.num_class_1.setText(self.schedule_day["les1"]["auditorium"])
        self.lesson_2.setText(self.schedule_day["les2"]["urok"])
        self.Teacher_2.setText(self.schedule_day["les2"]["th"])
        self.num_class_2.setText(self.schedule_day["les2"]["auditorium"])
        self.lesson_3.setText(self.schedule_day["les3"]["urok"])
        self.Teacher_3.setText(self.schedule_day["les3"]["th"])
        self.num_class_3.setText(self.schedule_day["les3"]["auditorium"])
        self.lesson_4.setText(self.schedule_day["les4"]["urok"])
        self.Teacher_4.setText(self.schedule_day["les4"]["th"])
        self.num_class_4.setText(self.schedule_day["les4"]["auditorium"])
        self.lesson_5.setText(self.schedule_day["les5"]["urok"])
        self.Teacher_5.setText(self.schedule_day["les5"]["th"])
        self.num_class_5.setText(self.schedule_day["les5"]["auditorium"])
        self.lesson_6.setText(self.schedule_day["les6"]["urok"])
        self.Teacher_6.setText(self.schedule_day["les6"]["th"])
        self.num_class_6.setText(self.schedule_day["les6"]["auditorium"])
        self.lesson_7.setText(self.schedule_day["les7"]["urok"])
        self.Teacher_7.setText(self.schedule_day["les7"]["th"])
        self.num_class_7.setText(self.schedule_day["les7"]["auditorium"])
        self.lesson_8.setText(self.schedule_day["les8"]["urok"])
        self.Teacher_8.setText(self.schedule_day["les8"]["th"])
        self.num_class_8.setText(self.schedule_day["les8"]["auditorium"])
        self.Button_Back.clicked.connect(self.full_schedule)

    def full_schedule(self):
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
