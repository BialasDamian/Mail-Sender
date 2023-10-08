from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import schedule
import time
if __name__ == '__main__':
    
    
        
    
    
        kto = input("WPISZ MAIL Z KTÓREGO CHCESZ WYSŁAĆ POWTARZALNĄ SEKWENCJĘ SPAMU:  ")
        haslo = input('WPISZ HASŁO DO SWOJEGO MAILA:  ')
        dokogo = input('WPISZ MAIL NA KTÓRY CHCESZ WYSŁAĆ SEKWENCJĘ SPAMU:  ')
        tekst = input('WPISZ TREŚĆ KTÓRĄ CHCESZ WYSŁAĆ MAILOWO POWTARZALNĄ SEKWENCJĄ:  ')
        Temat = input('WPISZ TEMAT SWOJEGO MAILA:  ')
        zalacznik = 'C:/Users/Damian/Desktop/obrazek.png'
        mail_content = tekst
        message = mail_content    #The mail addresses and password
        sender_address = kto
        sender_pass = haslo
        receiver_address = dokogo
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = Temat
        def maile():
            sender_email = kto
            password = haslo
            rec_email = dokogo
        # strona = 'www.google.pl'
        # open(strona)
        #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        attach_file_name = zalacznik
        attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload) #encode the attachment
        #add payload header with filename
        payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        message.attach(payload)
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail został wysłany')
    
    
        # server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.starttls()
        # server.login(kto,haslo) 
        # server.sendmail(kto, dokogo, message)

        print("""                                     ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´`´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´\````´/´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´\´|`/´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´-´--´-( O )-´--´-´´´´´´´¶¶´´¶´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´/´|`\´´´´´´´´´´`´´¶¶´´¶´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´/´´´´´\´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´´´´´´´´´´´
                                        ´´´´´´´´´´´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´´´¶¶´´´´´´´´´´              
                                        ´´´´´´´´´´¶¶´´´´´´´¶¶´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶´¶¶´´´´´´´¶¶´´´´´´´´´´´
                                        ´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´´´´´´
                                        ´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶´´´´¶¶¶´¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶¶´´´´¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´¶´¶´¶´¶´¶´¶´¶´¶´´´¶¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´
                                        ´´´´´´´´´´´´´´´´´´´´´´´´´´´´´ZALOGOWANO Z SUKCESEM´´´´´´´´´´´´´´´´´´´´´´´´´´´´´""")  
        


        while True:
            mail = maile
            schedule.every(2).seconds.do(mail)
            schedule.run_pending()
            time.sleep(1)
            #Powyżej znajduje się ustawienie pętli czasowej wykonania konkretnej funkcji, w tym przypadku petla()
            break