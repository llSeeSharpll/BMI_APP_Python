import sys
from PyQt5.QtWidgets import *;


bmi=0
app=QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('BMI Calculator')
window.setGeometry(300, 300, 300, 300)
window.move(60, 15)


userLabel = QLabel('<strong>Name</strong>', parent=window)
userLabel.move(50,50)


userText = QLineEdit(parent=window)
userText.move(120,48)


hieghtLabel = QLabel('<strong>Hieght(m)</strong',parent=window)
hieghtLabel.move(50,100)


hieghtText = QLineEdit(parent=window)
hieghtText.move(120,98)


wieghtLabel = QLabel('<strong>Wieght(Kg)</strong',parent=window)
wieghtLabel.move(50,150)


wieghtText = QLineEdit(parent=window)
wieghtText.move(120,148)


bmiLabel=QLabel(parent=window);
bmiLabel.move(50,250)


def wraper():
   bmi=calculateBmi(hieghtText.text(),wieghtText.text())

def calculateBmi(hieght,wieght):
    if(hieght==''):
        hieght=1
    if(wieght==''):
        wieght=0
    try:
        bmi=float(wieght)/float(pow(2,float(hieght)))
    except:
        bmiLabel.setText('wrong input format')
        bmiLabel.adjustSize()
        bmiLabel.show
    if(bmi>0):
        Text=userText.text()+', your Bmi is '+str(bmi)
        Text+=checkBmi(bmi,Text)
        bmiLabel.setText(Text)
        bmiLabel.adjustSize()
        bmiLabel.show
    else:
        bmiLabel.setText('wrong input format')
        bmiLabel.adjustSize()
        bmiLabel.show



def checkBmi(bmi,Text):
    if bmi<25:
        return '\nYou are not overwieght'
    else:
        return '\nYou are overwieght'


Login = QPushButton('Calculate',parent=window)
Login.move(50,200)


Login.clicked.connect(wraper)


window.show()
sys.exit(app.exec_())