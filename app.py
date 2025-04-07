import sys
import pyperclip
from PySide6 import QtCore, QtWidgets, QtGui
from password import Password

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.BTN_TEXT_WEAK: str = 'WEAK'
        self.BTN_TEXT_MEDIUM: str = 'MEDIUM'
        self.BTN_TEXT_STRONG: str = 'STRONG'
        self.password_strength: str = self.BTN_TEXT_WEAK
        self.setWindowTitle('Password Generator')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setup_ui()
        self.setup_connection()
        self.setup_ui_style()

    def setup_ui(self):
        # mise en place des éléments de l'interface
        self.setFixedHeight(400)
        self.setFixedWidth(800)
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.strength_definition_layout = QtWidgets.QHBoxLayout(self)
        self.action_layout = QtWidgets.QHBoxLayout(self)
        self.btn_weak = QtWidgets.QPushButton(self.BTN_TEXT_WEAK)
        self.btn_medium = QtWidgets.QPushButton(self.BTN_TEXT_MEDIUM)
        self.btn_strong = QtWidgets.QPushButton(self.BTN_TEXT_STRONG)
        self.btn_generate_password = QtWidgets.QPushButton('Generate Password')
        self.btn_copy_password = QtWidgets.QPushButton('Copy Password')
        self.lb_password = QtWidgets.QLabel('')
        self.lb_password.setTextFormat(QtCore.Qt.TextFormat.PlainText)

        self.strength_definition_layout.addWidget(self.btn_weak)
        self.strength_definition_layout.addWidget(self.btn_medium)
        self.strength_definition_layout.addWidget(self.btn_strong)

        self.action_layout.addWidget(self.btn_generate_password)
        self.action_layout.addWidget(self.lb_password)
        self.action_layout.addWidget(self.btn_copy_password)

        self.main_layout.addLayout(self.strength_definition_layout)
        self.main_layout.addLayout(self.action_layout)
        pass


    def setup_connection(self):
        # Relie les boutons à une method
        self.btn_weak.clicked.connect(lambda: self.set_password_strength(button=self.BTN_TEXT_WEAK))
        self.btn_medium.clicked.connect(lambda: self.set_password_strength(button=self.BTN_TEXT_MEDIUM))
        self.btn_strong.clicked.connect(lambda: self.set_password_strength(button=self.BTN_TEXT_STRONG))

        self.btn_generate_password.clicked.connect(self.generate_password)
        self.btn_copy_password.clicked.connect(self.copy_password)

    def setup_ui_style(self):
        # Permet de remanier le design de l'UI
        self.setStyleSheet("""
            * {
                margin: 0.5em;
            }
            QPushButton {
                background-color: #5c6bc0;
                color: white;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #7986cb;
            }
        
            QLabel {
                border: 0.1em solid white;
                border-radius: 8px;
                padding-left: 3em;
                padding-right: 3em;
                color: #FFFFFF;
                font-size: 15px;
                font-weight: bold;
            }
        """)
        
        pass


    def set_password_strength(self, button):
        # Définis la valeur de self.password_strength, peut être égal à WEAK ; MEDIUM ; STRONG
        self.password_strength = f'{button}'

    def generate_password(self):
        # Appel Password.generate_password() en passant la valeur de self.password_strenght()
        password_text = Password()
        password_text.generate_password(self.password_strength)
        self.lb_password.setText(password_text.password_generated)
        # /!\ Attention, le STRONG password ne fonctionne pas /!\


    def copy_password(self):
        # Copie la valeur du champ contenant le mot de passe dans le presse papier
        pyperclip.copy(self.lb_password.text())

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = MyApp()
    widget.show()
    sys.exit(app.exec())