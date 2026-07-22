import sys
import math
import pyperclip
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QGridLayout, QTextEdit, QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class AccountingCalc(QWidget):
    def __init__(self):
        super().__init__()
        self.mode_2nd = False
        self.initUI()

    def initUI(self):
        # تنظیمات اصلی پنجره
        self.setWindowTitle('حسابدار هوشمند | Smart Accountant')
        self.setMinimumSize(850, 500)
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2e;
                color: #ffffff;
                font-family: 'Segoe UI', Arial;
            }
            QLineEdit {
                background-color: #313244;
                border: 2px solid #45475a;
                border-radius: 10px;
                padding: 15px;
                font-size: 28px;
                color: #f5e0dc;
                margin-bottom: 10px;
            }
            QPushButton {
                background-color: #45475a;
                border-radius: 8px;
                padding: 15px;
                font-size: 18px;
                min-width: 60px;
            }
            QPushButton:hover {
                background-color: #585b70;
            }
            QPushButton#op_btn {
                background-color: #fab387;
                color: #11111b;
                font-weight: bold;
            }
            QPushButton#equal_btn {
                background-color: #a6e3a1;
                color: #11111b;
                font-weight: bold;
            }
            QPushButton#special_btn {
                background-color: #89b4fa;
                color: #11111b;
            }
            QTextEdit {
                background-color: #181825;
                border-radius: 10px;
                border: 1px solid #45475a;
                color: #bac2de;
                font-size: 14px;
            }
        """)

        # لایه اصلی (افقی برای جدا کردن ماشین حساب و تاریخچه)
        main_layout = QHBoxLayout()

        # بخش سمت چپ: ماشین حساب
        calc_layout = QVBoxLayout()
        
        self.entry = QLineEdit()
        self.entry.setAlignment(Qt.AlignRight)
        calc_layout.addWidget(self.entry)

        grid = QGridLayout()
        grid.setSpacing(8)

        # دکمه‌های خاص
        buttons = [
            ('Copy', self.copy_val, 0, 0), ('Clear', self.clear_all, 0, 1), 
            ('←', self.backspace, 0, 2), ('2nd', self.toggle_mode, 0, 3),
            ('/', lambda: self.append_text('/'), 0, 4),
            
            ('|x|', self.abs_sin, 1, 0), ('1/x', self.rev_cos, 1, 1),
            ('√x', self.sqrt_tan, 1, 2), ('x²', self.pow_log, 1, 3),
            ('*', lambda: self.append_text('*'), 1, 4),
            
            ('7', lambda: self.append_text('7'), 2, 0), ('8', lambda: self.append_text('8'), 2, 1),
            ('9', lambda: self.append_text('9'), 2, 2), ('(', lambda: self.append_text('('), 2, 3),
            ('-', lambda: self.append_text('-'), 2, 4),
            
            ('4', lambda: self.append_text('4'), 3, 0), ('5', lambda: self.append_text('5'), 3, 1),
            ('6', lambda: self.append_text('6'), 3, 2), (')', lambda: self.append_text(')'), 3, 3),
            ('+', lambda: self.append_text('+'), 3, 4),
            
            ('1', lambda: self.append_text('1'), 4, 0), ('2', lambda: self.append_text('2'), 4, 1),
            ('3', lambda: self.append_text('3'), 4, 2), ('000', lambda: self.append_text('000'), 4, 3),
            ('=', self.calculate, 4, 4, 2, 1) # دکمه مساوی بزرگ
        ]

        self.btn_objects = {} # برای تغییر متن دکمه‌ها در حالت 2nd

        for btn_data in buttons:
            text = btn_data[0]
            callback = btn_data[1]
            row, col = btn_data[2], btn_data[3]
            
            btn = QPushButton(text)
            btn.clicked.connect(callback)
            
            # استایل‌دهی اختصاصی
            if text in ['+', '-', '*', '/', '←']: btn.setObjectName("op_btn")
            elif text == '=': btn.setObjectName("equal_btn")
            elif text in ['2nd', 'Copy', 'Clear']: btn.setObjectName("special_btn")
            
            if len(btn_data) == 5: # دکمه‌های دو ردیفه
                grid.addWidget(btn, row, col, btn_data[4], 1)
            else:
                grid.addWidget(btn, row, col)
            
            self.btn_objects[text] = btn

        # اضافه کردن 0 و نقطه
        btn_zero = QPushButton("0")
        btn_zero.clicked.connect(lambda: self.append_text('0'))
        grid.addWidget(btn_zero, 5, 0, 1, 2)
        
        btn_dot = QPushButton(".")
        btn_dot.clicked.connect(lambda: self.append_text('.'))
        grid.addWidget(btn_dot, 5, 2)

        calc_layout.addLayout(grid)
        main_layout.addLayout(calc_layout, stretch=2)

        # بخش سمت راست: تاریخچه حسابداری
        history_panel = QVBoxLayout()
        history_panel.addWidget(QLabel("تاریخچه محاسبات"))
        self.history_txt = QTextEdit()
        self.history_txt.setReadOnly(True)
        history_panel.addWidget(self.history_txt)
        
        clear_hist_btn = QPushButton("پاک کردن تاریخچه")
        clear_hist_btn.clicked.connect(lambda: self.history_txt.clear())
        history_panel.addWidget(clear_hist_btn)
        
        main_layout.addLayout(history_panel, stretch=1)

        self.setLayout(main_layout)

    # توابع منطقی
    def append_text(self, char):
        self.entry.setText(self.entry.text() + str(char))

    def clear_all(self):
        self.entry.clear()

    def backspace(self):
        self.entry.setText(self.entry.text()[:-1])

    def copy_val(self):
        pyperclip.copy(self.entry.text())

    def toggle_mode(self):
        self.mode_2nd = not self.mode_2nd
        if self.mode_2nd:
            self.btn_objects['|x|'].setText('sin')
            self.btn_objects['1/x'].setText('cos')
            self.btn_objects['√x'].setText('tan')
            self.btn_objects['x²'].setText('log')
        else:
            self.btn_objects['|x|'].setText('|x|')
            self.btn_objects['1/x'].setText('1/x')
            self.btn_objects['√x'].setText('√x')
            self.btn_objects['x²'].setText('x²')

    def calculate(self):
        try:
            expression = self.entry.text()
            result = eval(expression)
            self.entry.setText(str(result))
            self.history_txt.append(f"{expression} = {result}\n{'-'*20}")
        except:
            self.entry.setText("Error")

    def abs_sin(self):
        try:
            val = float(eval(self.entry.text()))
            res = math.sin(math.radians(val)) if self.mode_2nd else abs(val)
            self.entry.setText(str(res))
        except: self.entry.setText("Error")

    def rev_cos(self):
        try:
            val = float(eval(self.entry.text()))
            res = math.cos(math.radians(val)) if self.mode_2nd else 1/val
            self.entry.setText(str(res))
        except: self.entry.setText("Error")

    def sqrt_tan(self):
        try:
            val = float(eval(self.entry.text()))
            res = math.tan(math.radians(val)) if self.mode_2nd else math.sqrt(val)
            self.entry.setText(str(res))
        except: self.entry.setText("Error")

    def pow_log(self):
        try:
            val = float(eval(self.entry.text()))
            res = math.log10(val) if self.mode_2nd else val**2
            self.entry.setText(str(res))
        except: self.entry.setText("Error")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AccountingCalc()
    ex.show()
    sys.exit(app.exec_())