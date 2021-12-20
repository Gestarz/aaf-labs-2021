from Function import Init
class Test:
    def test(self):
        cla = Init()
        cla.analiz('CREATE cars ( id NOMER, name Marka, name Contry ,id  price ,name kilkist);')
        cla.analiz('INSERT INTO cars ( " 1 ", " Mazda ", " Ukraine " , " 10200 " , " 1000 ");')
        cla.analiz('INSERT INTO cars ( " 3 ", " Nissa ", " Ukraine " , " 10100 " , " 10020 ");')
        cla.analiz("SELECT * FROM ' cars ';")
        cla.analiz('INSERT INTO cars ( " 2 ", " Nissan ", " Ukraine " , " 15200 " , " 100 ");')
        cla.analiz("SELECT * FROM ' cars ';")
        print('=======')
        cla.analiz('DELETE cars WHERE Marka = "Mazda";')
        cla.analiz("SELECT * FROM ' cars ';")
te=Test()
te.test()