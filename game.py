# from tkinter import *
# import random
# from tkinter import messagebox

# BG = 'green'
# FG = 'black'
# GAP = 2
# WIDTH = 50
# HEIGHT = 30
# COUNT = 19    # ستون
# ROWS = 18      # ردیف
# BOMB_COUNT = 30 # تعداد بمب

# CNF_BUTTON = {
#     'bg': BG,
#     'fg': FG,
# }

# root = Tk()
# root.geometry('1000x700')
# root.maxsize(500, 600)

# # تعداد کل خانه‌ها
# total_cells = ROWS * COUNT

# # ساختن بمب‌ها به صورت تصادفی
# bombs = random.sample(range(total_cells), BOMB_COUNT)

# # شمارش خانه‌های سالمی که کاربر باز کرده
# safe_clicked = 0

# # برای اینکه بعداً بتوانیم دکمه‌ها را مدیریت کنیم
# buttons = []

# def click_cell(index, btn):
#     global safe_clicked

#     if index in bombs:
#         btn.config(bg='red', text='BOMB')
#         messagebox.showinfo("Result", "lose")
#         root.destroy()
#     else:
#         btn.config(bg='lightgreen', state='disabled')
#         safe_clicked += 1

#         # اگر همه خانه‌های سالم باز شدند
#         if safe_clicked == total_cells - BOMB_COUNT:
#             messagebox.showinfo("Result", "WIN")
#             root.destroy()

# for row in range(ROWS):
#     for i in range(COUNT):
#         index = row * COUNT + i

#         btn = Button(root, text="", cnf=CNF_BUTTON)
#         btn.place(
#             x=i * (WIDTH + GAP),
#             y=row * (HEIGHT + GAP),
#             width=WIDTH,
#             height=HEIGHT
#         )
#         btn.config(command=lambda i=index, b=btn: click_cell(i, b))
#         buttons.append(btn)

# root.mainloop()












import sys
import random
from collections import deque

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


THEME = {
    "bg": "#0f172a",
    "panel": "#111827",
    "card": "#1e293b",
    "card_alt": "#334155",
    "accent": "#38bdf8",
    "success": "#22c55e",
    "danger": "#ef4444",
    "warning": "#f59e0b",
    "text": "#e5e7eb",
    "muted": "#94a3b8",
    "revealed": "#e2e8f0",
    "revealed_text": "#0f172a",
}


LEVELS = {
    "Easy": (10, 10, 12),
    "Medium": (14, 14, 28),
    "Hard": (18, 19, 45),
}


class CellButton(QPushButton):
    def __init__(self, row, col):
        super().__init__()
        self.row = row
        self.col = col
        self.is_bomb = False
        self.is_revealed = False
        self.is_flagged = False
        self.neighbor_bombs = 0

        self.setFixedSize(34, 34)
        self.setCursor(Qt.PointingHandCursor)
        self.setFont(QFont("Segoe UI", 10, QFont.Bold))
        self.update_style()

    def update_style(self):
        if self.is_revealed:
            if self.is_bomb:
                self.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {THEME["danger"]};
                        color: white;
                        border: 1px solid #b91c1c;
                        border-radius: 10px;
                    }}
                """)
            else:
                self.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {THEME["revealed"]};
                        color: {THEME["revealed_text"]};
                        border: 1px solid #cbd5e1;
                        border-radius: 10px;
                    }}
                """)
        elif self.is_flagged:
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {THEME["warning"]};
                    color: white;
                    border: 1px solid #d97706;
                    border-radius: 10px;
                }}
                QPushButton:hover {{
                    background-color: #fbbf24;
                }}
            """)
        else:
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {THEME["card_alt"]};
                    color: white;
                    border: 1px solid #475569;
                    border-radius: 10px;
                }}
                QPushButton:hover {{
                    background-color: #475569;
                    border: 1px solid {THEME["accent"]};
                }}
                QPushButton:pressed {{
                    background-color: #56657a;
                }}
            """)


class InfoCard(QFrame):
    def __init__(self, title, value):
        super().__init__()
        self.setStyleSheet(f"""
            QFrame {{
                background-color: {THEME["card"]};
                border: 1px solid #334155;
                border-radius: 16px;
            }}
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(14, 10, 14, 10)
        layout.setSpacing(2)

        self.title_label = QLabel(title)
        self.title_label.setStyleSheet(f"color: {THEME['muted']}; font-size: 11px;")
        self.value_label = QLabel(value)
        self.value_label.setStyleSheet(f"color: {THEME['text']}; font-size: 18px; font-weight: 700;")

        layout.addWidget(self.title_label)
        layout.addWidget(self.value_label)
        self.setLayout(layout)

    def set_value(self, value):
        self.value_label.setText(value)


class MinesweeperWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.rows = 0
        self.cols = 0
        self.bomb_count = 0

        self.buttons = []
        self.bomb_positions = set()
        self.revealed_safe_cells = 0
        self.flag_count = 0
        self.game_over = False
        self.elapsed_seconds = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.setWindowTitle("Minesweeper Deluxe")
        self.setMinimumSize(920, 820)

        self.init_ui()
        self.apply_level()
        self.start_new_game()

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        root_layout = QVBoxLayout()
        root_layout.setContentsMargins(20, 20, 20, 20)
        root_layout.setSpacing(16)

        title = QLabel("Minesweeper Deluxe")
        title.setFont(QFont("Segoe UI", 22, QFont.Bold))
        title.setStyleSheet(f"color: {THEME['text']};")

        subtitle = QLabel("A polished PyQt version with a cleaner, client-friendly design")
        subtitle.setStyleSheet(f"color: {THEME['muted']}; font-size: 12px;")

        top_text = QVBoxLayout()
        top_text.setSpacing(0)
        top_text.addWidget(title)
        top_text.addWidget(subtitle)

        self.level_combo = QComboBox()
        self.level_combo.addItems(LEVELS.keys())
        self.level_combo.setCurrentText("Medium")
        self.level_combo.setFixedHeight(38)
        self.level_combo.setStyleSheet(f"""
            QComboBox {{
                background-color: {THEME["card"]};
                color: {THEME["text"]};
                border: 1px solid #334155;
                border-radius: 10px;
                padding: 8px 12px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {THEME["card"]};
                color: {THEME["text"]};
                selection-background-color: {THEME["accent"]};
                border: 1px solid #334155;
            }}
        """)

        self.level_combo.currentTextChanged.connect(self.on_level_change)

        self.new_game_btn = QPushButton("New Game")
        self.new_game_btn.setFixedHeight(38)
        self.new_game_btn.setCursor(Qt.PointingHandCursor)
        self.new_game_btn.clicked.connect(self.start_new_game)
        self.new_game_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {THEME["accent"]};
                color: #082f49;
                border: none;
                border-radius: 10px;
                padding: 8px 16px;
                font-weight: 700;
            }}
            QPushButton:hover {{
                background-color: #7dd3fc;
            }}
            QPushButton:pressed {{
                background-color: #0ea5e9;
                color: white;
            }}
        """)

        top_bar = QHBoxLayout()
        top_bar.addLayout(top_text)
        top_bar.addStretch()
        top_bar.addWidget(self.level_combo)
        top_bar.addWidget(self.new_game_btn)

        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(12)

        self.status_card = InfoCard("Status", "Ready")
        self.bombs_card = InfoCard("Bombs Left", "0")
        self.timer_card = InfoCard("Time", "0s")

        cards_layout.addWidget(self.status_card)
        cards_layout.addWidget(self.bombs_card)
        cards_layout.addWidget(self.timer_card)

        self.board_frame = QFrame()
        self.board_frame.setStyleSheet(f"""
            QFrame {{
                background-color: {THEME["panel"]};
                border: 1px solid #334155;
                border-radius: 20px;
            }}
        """)

        self.grid_layout = QGridLayout()
        self.grid_layout.setContentsMargins(18, 18, 18, 18)
        self.grid_layout.setSpacing(6)
        self.board_frame.setLayout(self.grid_layout)

        hint = QLabel("Left click: reveal   |   Right click: flag")
        hint.setAlignment(Qt.AlignCenter)
        hint.setStyleSheet(f"color: {THEME['muted']}; font-size: 12px;")

        root_layout.addLayout(top_bar)
        root_layout.addLayout(cards_layout)
        root_layout.addWidget(self.board_frame)
        root_layout.addWidget(hint)

        central.setLayout(root_layout)

        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {THEME["bg"]};
            }}
        """)

    def apply_level(self):
        level_name = self.level_combo.currentText()
        self.rows, self.cols, self.bomb_count = LEVELS[level_name]

    def on_level_change(self):
        self.apply_level()
        self.start_new_game()

    def start_new_game(self):
        self.timer.stop()
        self.elapsed_seconds = 0
        self.timer_card.set_value("0s")

        self.game_over = False
        self.revealed_safe_cells = 0
        self.flag_count = 0
        self.bomb_positions.clear()
        self.buttons.clear()

        self.status_card.set_value("Ready")

        while self.grid_layout.count():
            item = self.grid_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        self.create_board()
        self.place_bombs()
        self.calculate_neighbors()
        self.update_bomb_counter()
        self.adjustSize()

    def create_board(self):
        for row in range(self.rows):
            row_buttons = []
            for col in range(self.cols):
                button = CellButton(row, col)
                button.clicked.connect(
                    lambda checked=False, r=row, c=col: self.handle_left_click(r, c)
                )
                button.mousePressEvent = self.build_mouse_handler(button)
                self.grid_layout.addWidget(button, row, col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def build_mouse_handler(self, button):
        def handler(event):
            if self.game_over:
                return

            if event.button() == Qt.RightButton:
                self.handle_right_click(button.row, button.col)
            elif event.button() == Qt.LeftButton:
                self.handle_left_click(button.row, button.col)
        return handler

    def place_bombs(self):
        all_positions = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        self.bomb_positions = set(random.sample(all_positions, self.bomb_count))
        for row, col in self.bomb_positions:
            self.buttons[row][col].is_bomb = True

    def calculate_neighbors(self):
        for row in range(self.rows):
            for col in range(self.cols):
                button = self.buttons[row][col]
                if button.is_bomb:
                    continue
                button.neighbor_bombs = self.count_neighbor_bombs(row, col)

    def count_neighbor_bombs(self, row, col):
        count = 0
        for nr, nc in self.get_neighbors(row, col):
            if self.buttons[nr][nc].is_bomb:
                count += 1
        return count

    def get_neighbors(self, row, col):
        neighbors = []
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr = row + dr
                nc = col + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    neighbors.append((nr, nc))
        return neighbors

    def handle_left_click(self, row, col):
        if self.game_over:
            return

        button = self.buttons[row][col]

        if button.is_revealed or button.is_flagged:
            return

        if self.elapsed_seconds == 0 and not self.timer.isActive():
            self.timer.start(1000)
            self.status_card.set_value("Playing")

        if button.is_bomb:
            self.reveal_bomb(button)
            self.reveal_all_bombs()
            self.game_over = True
            self.timer.stop()
            self.status_card.set_value("Lost")
            QMessageBox.information(self, "Game Over", "Boom! You hit a bomb.")
            return

        self.reveal_safe_area(row, col)
        self.check_win()

    def handle_right_click(self, row, col):
        if self.game_over:
            return

        button = self.buttons[row][col]

        if button.is_revealed:
            return

        button.is_flagged = not button.is_flagged
        button.setText("🚩" if button.is_flagged else "")

        if button.is_flagged:
            self.flag_count += 1
        else:
            self.flag_count -= 1

        button.update_style()
        self.update_bomb_counter()

    def reveal_bomb(self, button):
        button.is_revealed = True
        button.setText("💣")
        button.update_style()
        button.setEnabled(False)

    def reveal_safe_area(self, start_row, start_col):
        queue = deque([(start_row, start_col)])
        visited = set()

        while queue:
            row, col = queue.popleft()
            if (row, col) in visited:
                continue
            visited.add((row, col))

            button = self.buttons[row][col]

            if button.is_revealed or button.is_flagged or button.is_bomb:
                continue

            button.is_revealed = True
            button.setEnabled(False)
            self.revealed_safe_cells += 1

            if button.neighbor_bombs == 0:
                button.setText("")
            else:
                button.setText(str(button.neighbor_bombs))

            button.update_style()

            if button.neighbor_bombs == 0:
                for nr, nc in self.get_neighbors(row, col):
                    neighbor = self.buttons[nr][nc]
                    if not neighbor.is_revealed and not neighbor.is_bomb:
                        queue.append((nr, nc))

    def reveal_all_bombs(self):
        for row, col in self.bomb_positions:
            button = self.buttons[row][col]
            if not button.is_revealed:
                self.reveal_bomb(button)

    def update_bomb_counter(self):
        remaining = self.bomb_count - self.flag_count
        self.bombs_card.set_value(str(remaining))

    def update_timer(self):
        self.elapsed_seconds += 1
        self.timer_card.set_value(f"{self.elapsed_seconds}s")

    def check_win(self):
        total_safe_cells = (self.rows * self.cols) - self.bomb_count
        if self.revealed_safe_cells == total_safe_cells:
            self.game_over = True
            self.timer.stop()
            self.status_card.set_value("Won")
            QMessageBox.information(self, "Victory", "Congratulations! You won the game.")
            for row in range(self.rows):
                for col in range(self.cols):
                    self.buttons[row][col].setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 10))
    window = MinesweeperWindow()
    window.show()
    sys.exit(app.exec_())