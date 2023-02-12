from PyQt5.QtWidgets import QWidget,QApplication,QLineEdit,QPushButton,QVBoxLayout,QLabel,QListWidget
from PyQt5.QtGui import QFont
from transliterate import to_latin,to_cyrillic

app=QApplication([])
window=QWidget()
window.setStyleSheet("background-color: #ffd79d")
window.setFixedSize(440,308)

ver=QVBoxLayout()

#Created by Jurayevkh - Jo'rayev Rustambek


def convert():
    txt=input.text()
    input.setText("")
    result.clear()
    if txt.isascii():
        if "o'"in txt or "O'" in txt:
            txt=txt.replace("o'","ў")
            txt=txt.replace("O'","Ў")
        result.addItem(to_cyrillic(txt))
    else:
        result.addItem(to_latin(txt))


input=QLineEdit()
input.setPlaceholderText("Krillchada yoki Lotinchada so'z kiriting...")
input.setFixedSize(400,50)
input.setStyleSheet("color:black; border-radius:15px; border:2px solid #320d3e")
input.setFont(QFont("Gill Sans",20))
btn=QPushButton("Convert")
btn.setFixedSize(100,35)
btn.setStyleSheet("color:black; border-radius:5px; border:2px solid #320d3e")
btn.setFont(QFont("Gill Sans",15))
btn.clicked.connect(convert)

label=QLabel("Result")
label.setFont(QFont("Gill Sans",30))
label.setStyleSheet("color:black;")
result=QListWidget()
result.setStyleSheet("border:2px solid #320d3e; border-radius:15px;")
result.setFont(QFont("Gill Sans",20))
result.setFixedSize(400,100)


ver.addWidget(input)
ver.addWidget(btn)
ver.addWidget(label)
ver.addWidget(result)

window.setLayout(ver)

window.show()
app.exec_()
