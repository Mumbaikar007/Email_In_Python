from stmpmime import MailOject
import sys
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout, QWidget)



class EmailClient(QWidget):

    def __init__(self):
        super(EmailClient, self).__init__()

        self.text_message = QTextEdit(self)

        self.clr_btn = QPushButton('Clear')
        self.send_mail_btn = QPushButton('Send')

        self.sender_email_le = QLineEdit()
        self.sender_password_le = QLineEdit()
        self.receiver_email_le = QLineEdit()
        self.subject = QLineEdit()

        self.init_ui()

    def init_ui(self):

        self.setGeometry(300,150,750,420)


        #Declare layouts

        v_layout = QVBoxLayout()
        h_layout1 = QHBoxLayout()
        h_layout2 = QHBoxLayout()
        h_layout3 = QHBoxLayout()
        h_layout4 = QHBoxLayout()
        formlayout = QFormLayout()


        # User : Email, Password ; Sender's Email

        formlayout.addRow(QLabel("Email: "), self.sender_email_le )
        formlayout.addRow(QLabel("Password: "), self.sender_password_le)
        formlayout.addRow(QLabel("To: "), self.receiver_email_le)
        formlayout.addRow(QLabel("Subject: "), self.subject)

        # Clear, Attach Image, Send

        h_layout4.addStretch(1)
        h_layout4.addWidget(self.clr_btn)
        h_layout4.addWidget(self.send_mail_btn)


        # Design vertical layout
        v_layout.addLayout(formlayout)
        v_layout.addWidget(self.text_message)
        v_layout.addLayout(h_layout4)


        # button clicks
        self.send_mail_btn.clicked.connect(self.send_mail)
        self.clr_btn.clicked.connect(self.clear_text)



        self.setLayout(v_layout)
        self.setWindowTitle('EmailClient')
        self.show()



    def send_mail(self):
        to, user, password, subject, message  = self.receiver_email_le.text(),\
                                                self.sender_email_le.text(),\
                                                self.sender_password_le.text(), \
                                                self.subject.text(),self.text_message.toPlainText()

        mail_object = MailOject(to, user, password, subject, message)
        mail_object.Sending_Email()


    def clear_text(self):
        self.text.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    emailClient = EmailClient()
    sys.exit(app.exec_())