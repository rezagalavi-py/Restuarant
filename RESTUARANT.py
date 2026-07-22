import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QVBoxLayout, QHBoxLayout, QGridLayout, QTabWidget, QFrame, QScrollArea
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt


IMAGE_DIR = r"C:/Users/KMCC/Desktop/foods"

class RestaurantApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("سیستم سفارش‌گیر رستوران")
        self.setGeometry(100, 50, 1100, 850)
        
        # استایل کلی پنجره (تم تاریک و مدرن با تم رنگی نارنجی)
        self.setStyleSheet("""
            QWidget {
                background-color: #262626;
                color: #FFFFFF;
                font-family: "Lalezar", "Segoe UI", Arial;
            }
            QTabWidget::pane {
                border: 2px solid #333333;
                background-color: #2b2b2b;
                border-radius: 10px;
            }
            QTabBar::tab {
                background: #333333;
                color: #FFA500;
                border: 1px solid #444;
                padding: 12px 30px;
                font-size: 16px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                margin-right: 4px;
            }
            QTabBar::tab:selected {
                background: #FFA500;
                color: #1a1a1a;
                font-weight: bold;
            }
            QScrollBar:vertical {
                border: none;
                background: #2b2b2b;
                width: 10px;
            }
            QScrollBar::handle:vertical {
                background: #555;
                border-radius: 5px;
            }
        """)
        
        self.orders = {} # ذخیره تعداد سفارشات هر غذا
        
        # اطلاعات منو منطبق با کدهای اصلی شما و فایل‌های ارسالی
        self.menu_data = {
            "🍕 پیتزاها": [
                ("پیتزا پپرونی", 500000, "image1.jpg"),
                ("پیتزا مرغ", 630000, "image2.jpg"),
                ("پیتزا گوشت و قارچ", 1000000, "image3.jpg"),
                ("پیتزا مخصوص", 600000, "image4.jpg"),
            ],
            "🍔 غذاهای اصلی و فرعی": [
                ("پاستا آلفردو", 700000, "image5.jpg"),
                ("استرامبولی", 500000, "images.jpg"),
                ("همبرگر مخصوص", 570000, "479-4798191_burger-and-fries-png-gourmet-burger-and-chips.jpg"),
                ("سیب زمینی سرخ شده", 300000, "images7.jpg"),
            ],
            "🥤 نوشیدنی و پیش‌غذا": [
                ("سوپ داغ", 198000, "images11.jpg"),
                ("نوشابه خنک", 110000, "images13.jpg"),
                ("دوغ سنتی", 80000, "images9.jpg"),
                ("دلستر لیمویی", 90000, "images10.jpg"),
            ]
        }
#   اینجا تابع ساخت رابط گرافیکی اجرا میشود
        self.init_ui()   


# این تابع مسئول ساخت کل رابط گرافیکی برنامه است.
    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 15, 15, 15)
        
        # هدر اصلی برنامه
        header_lbl = QLabel("🍕 منوی هوشمند سفارش غذا 🍕")
        header_lbl.setFont(QFont("Lalezar", 26))
        header_lbl.setAlignment(Qt.AlignCenter)
        header_lbl.setStyleSheet("color: #FFA500; margin-bottom: 10px;")
        main_layout.addWidget(header_lbl)

        # ایجاد سیستم تب‌بندی
        self.tabs = QTabWidget()
        
        for category, items in self.menu_data.items():
            self.tabs.addTab(self.create_menu_tab(items), category)
            
        main_layout.addWidget(self.tabs)

        # بخش نمایش فاکتور و جمع کل در پایین صفحه
        footer_frame = QFrame()
        footer_frame.setStyleSheet("""
            QFrame {
                background-color: #1a1a1a;
                border: 2px solid #FFA500;
                border-radius: 12px;
                margin-top: 15px;
            }
        """)
        footer_layout = QHBoxLayout(footer_frame)
        footer_layout.setContentsMargins(20, 15, 20, 15)
        
        self.total_label = QLabel("جمع کل سفارشات: 0 تومان")
        self.total_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.total_label.setStyleSheet("color: #00FF66; border: none;")
        
        # دکمه پاک کردن کل سفارشات
        reset_btn = QPushButton("ریست منو")
        reset_btn.setFont(QFont("Arial", 12, QFont.Bold))
        reset_btn.setFixedSize(120, 45)
        reset_btn.setStyleSheet("""
            QPushButton {
                background-color: #d9534f;
                color: white;
                border-radius: 8px;
                border: none;
            }
            QPushButton:hover {
                background-color: #c9302c;
            }
        """)
        reset_btn.clicked.connect(self.reset_all_orders)

        footer_layout.addWidget(reset_btn)
        footer_layout.addStretch()
        footer_layout.addWidget(self.total_label)
        
        main_layout.addWidget(footer_frame)
        self.setLayout(main_layout)

    def create_menu_tab(self, items):
        # استفاده از ScrollArea برای اینکه در مانیتورهای کوچک اسکرول بخورد
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("border: none; background-color: transparent;")
        
        container = QWidget()
        container.setStyleSheet("background-color: transparent;")
        grid = QGridLayout(container)
        grid.setSpacing(15)
        
        row, col = 0, 0
        for name, price, img_name in items:
            item_card = self.create_food_card(name, price, img_name)
            grid.addWidget(item_card, row, col)
            
            col += 1
            if col > 1: # چیدمان در ۲ ستون منظم
                col = 0
                row += 1
                
        scroll.setWidget(container)
        return scroll

    def create_food_card(self, name, price, img_name):
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: #333333;
                border: 1px solid #444444;
                border-radius: 12px;
            }
            QFrame:hover {
                border: 1px solid #FFA500;
                background-color: #3a3a3a;
            }
        """)
        
        card_layout = QHBoxLayout(card)
        card_layout.setContentsMargins(10, 10, 10, 10)

        # لود کردن تصویر غذا
        img_label = QLabel()
        img_label.setFixedSize(150, 150)
        img_label.setStyleSheet("border: none; background-color: #222; border-radius: 8px;")
        img_label.setAlignment(Qt.AlignCenter)
        
        full_img_path = os.path.join(IMAGE_DIR, img_name)
        
        pixmap = QPixmap(full_img_path)
        if not pixmap.isNull():
            img_label.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            # اگر عکسی پیدا نشد، یک آیکون متنی یا نام غذا نمایش داده شود
            img_label.setText("🖼️\nبدون عکس")
            img_label.setStyleSheet("color: #777; font-size: 14px; border: 1px dashed #555;")

        # جزییات متن غذا (نام به صورت راست‌چین فارسی و قیمت منظم)
        details_layout = QVBoxLayout()
        details_layout.setAlignment(Qt.AlignVCenter)
        
        name_lbl = QLabel(name)
        name_lbl.setFont(QFont("Arial", 16, QFont.Bold))
        name_lbl.setStyleSheet("color: #FFA500; border: none;")
        name_lbl.setAlignment(Qt.AlignRight)
        
        price_lbl = QLabel(f"{price:,} تومان")
        price_lbl.setFont(QFont("Arial", 13))
        price_lbl.setStyleSheet("color: #CCCCCC; border: none;")
        price_lbl.setAlignment(Qt.AlignRight)
        
        details_layout.addWidget(name_lbl)
        details_layout.addWidget(price_lbl)

        # بخش افزایش/کاهش تعداد سفارش (دکمه‌های مثبت و منفی و شمارنده)
        counter_layout = QHBoxLayout()
        counter_layout.setSpacing(8)
        
        btn_minus = QPushButton("-")
        btn_plus = QPushButton("+")
        count_lbl = QLabel("0")
        
        count_lbl.setFont(QFont("Arial", 16, QFont.Bold))
        count_lbl.setFixedWidth(40)
        count_lbl.setAlignment(Qt.AlignCenter)
        count_lbl.setStyleSheet("color: white; border: none; background-color: #222; border-radius: 5px; padding: 4px;")

        btn_style = """
            QPushButton {
                background-color: #444444;
                color: #FFA500;
                font-size: 20px;
                font-weight: bold;
                border-radius: 6px;
                border: none;
            }
            QPushButton:hover {
                background-color: #FFA500;
                color: black;
            }
            QPushButton:pressed {
                background-color: #cc8400;
            }
        """
        btn_minus.setStyleSheet(btn_style)
        btn_plus.setStyleSheet(btn_style)
        btn_minus.setFixedSize(40, 40)
        btn_plus.setFixedSize(40, 40)

        # ثبت اطلاعات هر آیتم در دیکشنری کلی جهت دسترسی سریع زمان آپدیت
        self.orders[name] = {
            "label": count_lbl,
            "price": price,
            "count": 0
        }

        btn_plus.clicked.connect(lambda _, n=name: self.change_quantity(n, 1))
        btn_minus.clicked.connect(lambda _, n=name: self.change_quantity(n, -1))

        counter_layout.addWidget(btn_minus)
        counter_layout.addWidget(count_lbl)
        counter_layout.addWidget(btn_plus)

        # سرهم‌بندی المان‌ها در کارت محصول
        card_layout.addWidget(img_label)
        card_layout.addLayout(details_layout)
        card_layout.addStretch()
        card_layout.addLayout(counter_layout)

        return card

    def change_quantity(self, name, amount):
        item = self.orders[name]
        new_count = max(0, item["count"] + amount)
        item["count"] = new_count
        item["label"].setText(str(new_count))
        self.update_total_price()

    def update_total_price(self):
        total = 0
        for item in self.orders.values():
            total += item["count"] * item["price"]
        self.total_label.setText(f"جمع کل سفارشات: {total:,} تومان")

    def reset_all_orders(self):
        for item in self.orders.values():
            item["count"] = 0
            item["label"].setText("0")
        self.update_total_price()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RestaurantApp()
    window.show()
    sys.exit(app.exec_())