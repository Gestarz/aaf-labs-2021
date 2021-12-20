import numpy as np
import pandas as pd

class Init:
    def __init__(self):
        self.init_roz=0
        self.buffer = []
    def tables(self,tabl):
        """F-друку"""
        colomses = tabl[0]
        ind = np.arange(1, len(tabl))
        tabl_for_print = pd.DataFrame(tabl[1:], columns=colomses, index=ind)
        print('************TABLES************')
        print(tabl_for_print)
        print('**************END*************')
    def parser(self,sob):
        """F-парсер"""
        sob = sob.replace('\n', ' ')
        sob = sob.replace('  ', ' ')
        sob = sob.replace('  ', ' ')
        sob = sob.replace('   ', ' ')
        sob = sob.replace(',', '')
        sob = sob.replace('(', ' ')
        sob = sob.replace(')', ' ')
        sob = sob.replace(';', ' ')
        sob = sob.replace('"', ' ')
        return sob
    def analiz(self,sob):
        """F-парсер-first"""
        sob=self.parser(sob)
        if sob[0:6] == 'CREATE':
            self.create(sob.split())
            print(sob.split())
        if sob[0:6] == 'INSERT':
            print(sob.split())
            self.add(sob.split())
        if sob[0:6] == 'SELECT':
            print(sob.split())
            self.get(sob.split())
        if sob[0:6] == 'DELETE':
            self.deleti(sob.split())
            print(sob.split())
            pass
        else:
            print('=/=')
    def add(self,sob):
        m=0
        k=[]
        try:
            for i in range(len(sob)-3):
                k.append(sob[3+i])
            for i in range(len(self.buffer)):
                if sob[2]==list(self.buffer[i].keys())[0]:
                    for j in range(len(k)):
                        self.buffer[i][sob[2]].append(k[j])
                    m=i
                    break
            #self.buffer[m][sob[2]]=np.array(self.buffer[m][sob[2]])
            print(self.buffer[m][sob[2]])
        except:
            print('Error')
    def deleti1(self,sob):

        m = 0
        for i in range(len(self.buffer)):
            if sob[1] == list(self.buffer[i].keys())[0]:
                m = i
                break
        testi = np.array(self.buffer[m][sob[1]])
        g = (testi.reshape(int(len(testi) / self.init_roz), self.init_roz))
        ind=0
        for i in range(self.init_roz):
            if g[0][i]==sob[3]:
                ind=i
                break
        e=[]
        for i in range(len(g)):
            e.append(g[i][ind])
        k=[]
        for i in range(len(g)):
            time = []
            for j in range(len(g[i])):
                if g[i][j] not in e:
                    time.append(g[i][j])
            k.append(time)
        print(k)
        self.buffer[m][sob[1]]=k
        print(self.buffer[m])
        self.init_roz-=1
    def deleti1(self,sob):
        m = 0
        for i in range(len(self.buffer)):
            if sob[1] == list(self.buffer[i].keys())[0]:
                m = i
                break
        testi = np.array(self.buffer[m][sob[1]])
        g = (testi.reshape(int(len(testi) / self.init_roz), self.init_roz))
        ind=0
        for i in range(self.init_roz):
            if g[0][i]==sob[3]:
                ind=i
                break
        e=[]
        for i in range(len(g)):
            e.append(g[i][ind])
        k=[]
        for i in range(len(g)):
            time = []
            for j in range(len(g[i])):
                if g[i][j] not in e:
                    time.append(g[i][j])
            k.append(time)
        print(k)
        self.buffer[m][sob[1]]=k
        print(self.buffer[m])
        self.init_roz-=1
    def deleti(self,sob):
        try:
            m = 0
            for i in range(len(self.buffer)):
                if sob[1] == list(self.buffer[i].keys())[0]:
                    m = i
                    break
            print(self.buffer[m][sob[1]])
            testi = np.array(self.buffer[m][sob[1]])
            g = (testi.reshape(int(len(testi) / self.init_roz), self.init_roz))
            print(g)
            iniui=sob[3]
            prueer=999
            for i in range(len(g[0])):
                #print(g[0][i])
                if(g[0][i]==iniui):
                    prueer=i
                    break
            if(prueer==999):
                print('Not Found')
                return 0
            else:
                for j in range(len(g)):
                    print(g[j][prueer])
                    if(g[j][prueer]==sob[5]):
                        g = np.delete(g, (j), axis=0)
                        break
                    else:
                        pass
            buff=[]
            for i in range(len(g)):
                for j in range(len(g[i])):
                    buff.append(g[i][j])
            self.buffer[m][sob[1]]=buff
        except:
            print('Error delete')
    def create(self,sob):
        numb = 2
        sp = []
        for j in range(int(len(sob) / 2 - 1)):
            sp.append(sob[numb+1])
            numb += 2
        try:
            self.buffer.append({sob[1]:sp})
            self.init_roz=int(len(sp))
        except:
            print('Error')
    def get(self,sob):
        m = 0
        try:
            for i in range(len(self.buffer)):
                if sob[4] == list(self.buffer[i].keys())[0]:
                    m = i
                    break
            testi = np.array(self.buffer[m][sob[4]])
            print(testi)
            try:
                g=testi.reshape(int(len(testi) / self.init_roz), self.init_roz)
                self.tables(g)
            except:
                self.tables(testi)
        except:
          print("Error")