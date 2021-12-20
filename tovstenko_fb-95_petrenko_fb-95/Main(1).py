import time
from Function import Init
if __name__ == '__main__':
    print('========================Start========================')
    sob=''
    print('Дальше можете вводить свои команды ========>')
    for i in range(10):
        print('.',end='')
        time.sleep(0.2)
    print('')
    cla=Init()
    while sob!='Exit':
        sob=input('Root>')
        cla.analiz(sob)