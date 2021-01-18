import time
import smtplib
from email.mime.text import MIMEText

def sendmail(result):
    curtime = time.strftime('%Y-%m-%d %H:%M:%S')
    print(result)
    print('[START SEND MAIL]',time.strftime('%Y-%m-%d %H:%M:%S'))
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login('kdy41000@gmail.com','miumxcjlnolhqkiz')
    contents = ''
    no = 1
    for i in result:
        contents += str(no) + '. ' + i +'\n'
        no = no + 1
    msg = MIMEText(curtime+' 기준으로 발송된 CGV영화정보입니다.'+'\n\n'+ contents +'\n\n from DEVYoung')
    msg['Subject'] = 'CGV현재 상영작 정보('+curtime+')'

    s.sendmail('kdy41000@gmail.com','kdy41000@naver.com',msg.as_string())
    s.sendmail('kdy41000@gmail.com','takorina12@naver.com',msg.as_string())
    s.sendmail('kdy41000@gmail.com','ldh8689@gmail.com',msg.as_string())

    s.quit()

    print('[END SEND MAIL]',time.strftime('%Y-%m-%d %H:%M:%S'))