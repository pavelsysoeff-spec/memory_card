#создай приложение для запоминания информации\
from PyQt5.QtCore import Qt
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QRadioButton, QtWidgets, QVBoxLayout, QGroupBox
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint

class Question():
    def __init__(
        self, question, right_answer, 
        wrong1, wrong2, wrong3):
            self.question = question
            self.right_answer = right_answer
            self.wrong1 = wrong1
            self.wrong2 = wrong2
            self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('Memo Card')
main_question = QLabel('Самый сложный вопрос в мире!')
btn = QPushButton('Ответить')

# начало панели вопросов
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Какое самое большое число в мире?')
rbtn_2 = QRadioButton('Какая самая большая цифра?')
rbtn_3 = QRadioButton('Бисконечна ли вселенная?')
rbtn_4 = QRadioButton('Есть ли жизнь на других планетах?')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
# конец панели вопросов

# начало панели результата
AnsGroupBox = QGroupBox('Результат теста')
ans_result = QLabel('Ты прав или нет')
ans_correct = QLabel('Ответ тут')
layout_res = QVBoxLayout()
layout_res.addWidget(ans_result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(ans_correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(main_question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn, stretch = 2)
layout_line3.addStretch(1)

layout_main = QVBoxLayout()
layout_main.addLayout(layout_line1, stretch = 2)
layout_main.addLayout(layout_line2, stretch = 8)
layout_main.addStretch(1)
layout_main.addLayout(layout_line3, stretch = 1)
layout_main.addStretch(1)
layout_main.setSpacing(5)

main_win.setLayout(layout_main)

# начало функции
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn.setText('Следующий вопрос')    

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn.setText('Ответить')    
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)    
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)    
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2) 
    answers[3].setText(q.wrong3)  
    main_question.setText(q.question)
    ans_correct.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
        print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.score)
        print('Рейтинг:', (main_win.score / main_win.total * 100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isСhecked():
            show_correct('Неверно')
            print('Рейтинг:', (main_win.score / main_win.total * 100), '%')

def show_correct(res):
    ans_result.setText(res)
    show_result()

def next_question():
    main_win.total += 1
    main_win.cur_question += 1
    print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.score)
    if main_win.cur_question >= len(questions_list):
        main_win.cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[main_win.cur_question]
    ask(q)

def click_ok():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()

questions_list = []
questions_list.append(Question('Самый сложный вопрос в мире!', 'Какое самое большое число в мире?',
'Какая самая большая цифра?', 'Бисконечна ли вселенная?', 'Есть ли жизнь на других планетах?')) 
questions_list.append(Question('В каком клубе играет Роналдо', 'Аль-Наср', 'Манчестер Юнайтед',
 'Ливерпуль', 'Челси'))
questions_list.append(Question('Кто самый богатый человек в мире?', 'Илон Маск', 'Билл Гейтс',
 'Джефф Безос', 'Марк Цукерберг'))

main_win.score = 0
main_win.total = 0
main_win.cur_question = -1
btn.clicked.connect(click_ok)
next_question()
main_win.resize(400, 300)
main_win.show()
app.exec_()
