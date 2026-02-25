# ==========================================
# Smart Disaster Relief Management System
# Modern UI using PyQt6
# ==========================================

import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout,
    QComboBox, QMessageBox, QGroupBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


# ---------------- CAMP CLASS ----------------
class Camp:
    def __init__(self, camp_id, location, max_capacity, food, medical, volunteers):
        self.camp_id = camp_id
        self.location = location
        self.max_capacity = int(max_capacity)
        self.current_occupancy = 0
        self.available_food = int(food)
        self.available_medical = int(medical)
        self.volunteers = int(volunteers)
        self.total_food_distributed = 0
        self.total_medical_distributed = 0



# ---------------- VICTIM CLASS ----------------
class Victim:
    def __init__(self, victim_id, name, age, health_condition, camp_id):
        self.victim_id = victim_id
        self.name = name
        self.age = int(age)
        self.health_condition = health_condition
        self.camp_id = camp_id
        self.food_received = 0
        self.medical_received = 0


# ---------------- MAIN WINDOW ----------------
class DisasterApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Disaster Relief System")
        self.setGeometry(200, 100, 900, 700)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        title = QLabel("Smart Disaster Relief Resource Management System")
        title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        # -------- CAMP SECTION --------
        camp_group = QGroupBox("Camp Registration")
        camp_layout = QVBoxLayout()

        self.camp_id = QLineEdit()
        self.camp_id.setPlaceholderText("Camp ID")

        self.location = QLineEdit()
        self.location.setPlaceholderText("Location")

        self.capacity = QLineEdit()
        self.capacity.setPlaceholderText("Maximum Capacity")

        self.food = QLineEdit()
        self.food.setPlaceholderText("Available Food Packets")

        self.medical = QLineEdit()
        self.medical.setPlaceholderText("Available Medical Kits")

        self.volunteers = QLineEdit()
        self.volunteers.setPlaceholderText("Number of Volunteers")

        add_camp_btn = QPushButton("Add Camp")
        add_camp_btn.clicked.connect(self.add_camp)

        for widget in [self.camp_id, self.location, self.capacity,
                       self.food, self.medical, self.volunteers, add_camp_btn]:
            camp_layout.addWidget(widget)

        camp_group.setLayout(camp_layout)
        main_layout.addWidget(camp_group)

        # -------- VICTIM SECTION --------
        victim_group = QGroupBox("Victim Registration")
        victim_layout = QVBoxLayout()

        self.victim_id = QLineEdit()
        self.victim_id.setPlaceholderText("Victim ID")

        self.victim_name = QLineEdit()
        self.victim_name.setPlaceholderText("Victim Name")

        self.age = QLineEdit()
        self.age.setPlaceholderText("Age")

        self.assign_camp = QLineEdit()
        self.assign_camp.setPlaceholderText("Assign Camp ID")

        self.health = QComboBox()
        self.health.addItems(["normal", "critical"])

        register_btn = QPushButton("Register Victim")
        register_btn.clicked.connect(self.register_victim)

        for widget in [self.victim_id, self.victim_name,
                       self.age, self.assign_camp,
                       self.health, register_btn]:
            victim_layout.addWidget(widget)

        victim_group.setLayout(victim_layout)
        main_layout.addWidget(victim_group)

        # -------- REPORT BUTTON --------
        report_btn = QPushButton("Generate Analytical Report")
        report_btn.clicked.connect(self.generate_report)
        main_layout.addWidget(report_btn)

        self.setLayout(main_layout)

        # -------- STYLING --------
        self.setStyleSheet("""
            QWidget {
                background-color: #2e2e2e;
                color: white;
                font-size: 14px;
            }
            QLineEdit, QComboBox {
                background-color: #3e3e3e;
                padding: 8px;
                border-radius: 6px;
            }
            QPushButton {
                background-color: #0078d7;
                padding: 10px;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #555;
                border-radius: 10px;
                margin-top: 10px;
                padding: 10px;
            }
        """)

    # ---------------- LOGIC ----------------
    def add_camp(self):
        try:
            camp = Camp(
                self.camp_id.text(),
                self.location.text(),
                self.capacity.text(),
                self.food.text(),
                self.medical.text(),
                self.volunteers.text()
            )

            with open("camps.txt", "a") as f:
                f.write(f"{camp.camp_id},{camp.location},{camp.max_capacity},"
                        f"{camp.current_occupancy},{camp.available_food},"
                        f"{camp.available_medical},{camp.volunteers},"
                        f"{camp.total_food_distributed},{camp.total_medical_distributed}\n")

            QMessageBox.information(self, "Success", "Camp Added Successfully!")

        except:
            QMessageBox.warning(self, "Error", "Invalid Input!")

    def register_victim(self):
        QMessageBox.information(self, "Info", "Victim registration logic implemented here.")

    def generate_report(self):
        QMessageBox.information(self, "Report", "Analytical report logic implemented here.")


# ---------------- RUN APP ----------------
app = QApplication(sys.argv)
window = DisasterApp()
window.show()
sys.exit(app.exec())