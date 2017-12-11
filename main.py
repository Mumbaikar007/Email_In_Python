

import sys
import re
import os
from stmpmime import MailOject
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout, QWidget, QFileDialog)



class EmailClient(QWidget):

    def __init__(self):
        super(EmailClient, self).__init__()

        self.sender_email_le = QLineEdit()
        self.sender_password_le = QLineEdit()
        self.receiver_email_le = QLineEdit()
        self.subject_le = QLineEdit()

        self.text_message = QTextEdit(self)

        self.attachments_label = QLabel("No Attachments yet !!")
        self.attachments_list = []

        self.sender_email_le.setText("")
        self.sender_password_le.setText("")
        self.receiver_email_le.setText("")
        self.subject_le.setText("")
        self.text_message.setPlainText("")

        self.clear_button = QPushButton('Clear')
        self.insert_button = QPushButton('Insert')
        self.send_mail_button = QPushButton('Send')

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
        formlayout.addRow(QLabel("Subject: "), self.subject_le)


        # horizontal 3: Attachments

        h_layout3.addWidget(self.attachments_label)
        h_layout3.addStretch()


        # horizontal 4: Add Clear, Attach Image, Send
        h_layout4.addStretch(1)
        h_layout4.addWidget(self.clear_button)
        h_layout4.addWidget(self.insert_button)
        h_layout4.addWidget(self.send_mail_button)


        # Design vertical layout
        v_layout.addLayout(formlayout)
        v_layout.addWidget(self.text_message)
        v_layout.addLayout(h_layout3)
        v_layout.addLayout(h_layout4)


        # button clicks
        self.send_mail_button.clicked.connect(self.send_mail)
        self.clear_button.clicked.connect(self.clear_text)
        self.insert_button.clicked.connect(self.insert_attachment)


        self.setLayout(v_layout)
        self.setWindowTitle('EmailClient')
        self.show()



    def send_mail(self):

        mail_object = MailOject(self.receiver_email_le.text(),\
                                                self.sender_email_le.text(),\
                                                self.sender_password_le.text(), \
                                                self.subject_le.text(),\
                                                self.text_message.toPlainText(),\
                                                self.attachments_list
                                )
        mail_object.Sending_Email()


    def insert_attachment(self):

        filename = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        self.attachments_list.append(filename[0])


        new_attachment_label = "Attachments: "
        for f in self.attachments_list:
            new_attachment_label += (os.path.basename(f) + ", ")

        self.attachments_label.setText(new_attachment_label)



    def clear_text(self):
        self.text_message.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    emailClient = EmailClient()
    sys.exit(app.exec_())
