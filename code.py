from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QListWidget, QLineEdit, QLabel, QHBoxLayout,QVBoxLayout, QPushButton

app = QApplication([])
window = QWidget()
window.setWindowTitle("Розумні замітки")
window.setFixedWidth(900)
window.setFixedHeight(600)

text = QTextEdit()
text.setText("Я розумна замітка!")

label1 = QLabel("Список заміток")
label2 = QLabel("Список тегів")

butt1 = QPushButton("Створити замітку")
butt2 = QPushButton("Видалити замітку")
butt3 = QPushButton("Зберегти замітку")
butt4 = QPushButton("Додати до замітки")
butt5 = QPushButton("Відкріпити від замітки")
butt6 = QPushButton("Шукати по тегу")

list1 = QListWidget()
list1.addItem("Що це таке?")
list2 = QListWidget()

line = QLineEdit()
line.setPlaceholderText("Введіть тег 💔💔...")

HmainBox = QHBoxLayout()
V1 = QVBoxLayout()
V2 = QVBoxLayout()
H1 = QHBoxLayout()
H2 = QHBoxLayout()

V1.addWidget(text)
H1.addWidget(butt1)
H1.addWidget(butt2)
H2.addWidget(butt4)
H2.addWidget(butt5)

V2.addWidget(label1)
V2.addWidget(list1)
V2.addLayout(H1)
V2.addWidget(butt3)
V2.addWidget(label2)
V2.addWidget(list2)
V2.addWidget(line)
V2.addLayout(H2)
V2.addWidget(butt6)

HmainBox.addLayout(V1, stretch=2)
HmainBox.addLayout(V2, stretch=1)
window.setLayout(HmainBox)

notes = list()
notes.append("Що це таке")
print(notes)

def delete_note():
    list1.currentRow()
butt2.clicked.connect(delete_note)
window.show()
app.exec_()
