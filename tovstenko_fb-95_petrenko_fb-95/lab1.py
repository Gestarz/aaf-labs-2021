import sqlite3 as sql

def add(sob):
    con = sql.connect('test.db')
    with con:
        cur = con.cursor()
        try:
            cur.execute(sob)
            print('Table has been update')
        except:
            print('Error')
def delete(sob):
    con = sql.connect('test.db')
    with con:
        cur = con.cursor()
        try:
            cur.execute(sob)
            print('Table has been update')
        except:
            print('Error')
def create(l):
    con = sql.connect('test.db')
    with con:
        cur = con.cursor()
        try:

            #"CREATE TABLE 'test1' ('add' STRING, 'surname' STRING)"
            l=l[:13]+'IF NOT EXISTS '+l[13:]
            #l="CREATE TABLE 'test1' ('add2' STRING, 'surname' STRING)"
            #l="CREATE TABLE 'test7' ('add3' STRING, 'surname1' STRING)"
            #print(l)
            cur.execute(str(l))
            print('Table has been created')
        except:
            print('Error')
def get(sob):
    con = sql.connect('test.db')
    with con:
        cur = con.cursor()
        cur.execute(sob)
        rows = cur.fetchall()
        for row in rows:
            print(row[0], row[1])
if __name__ == '__main__':
    sob=''
    while sob!='Exit':
        sob=input('')
        sob=sob.replace('\n',' ')
        sob=sob.replace('  ',' ')
        sob = sob.replace('  ', ' ')
        sob = sob.replace('   ', ' ')
        if sob[0:6]=='CREATE':
            create(sob)
            #CREATE TABLE 'test7' ('add3' STRING, 'surname1' STRING)
        if sob[0:6]=='INSERT':
            add(sob)
            #INSERT INTO 'test' VALUES('pr','HAR')
        if sob[0:6]=='SELECT':
            get(sob)
            #SELECT * FROM 'test'
        if sob[0:6]=='DELETE':
            #DELETE FROM 'test7'
            delete(sob)
