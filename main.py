import os
import time
import crawlingmovie
import mailcontroller

def main():
    status = True

    while True:
        time.sleep(5)
        curtime = time.strftime('%H%M')
        if(curtime == '2118' and status == True):
            result = crawlingmovie.startcrawling()
            mailcontroller.sendmail(result)
            status = False
        elif(curtime != '2118'):
            status = True


if __name__=='__main__':
    main()