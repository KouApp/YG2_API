import pyodbc

class Search:
    def __init__(self):
        self.db = pyodbc.connect(
                            'Driver={ODBC Driver 17 for SQL Server};'
                            'Server=sql.athena.domainhizmetleri.com;'
                            'Database=abdullah_pys;'
                            'UID=abdullah_pys;'
                            'PWD=@PassWord123;'
                            )

    def headlineSearch(self,projeid):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[t_Projects]')
        dataTable = curs.fetchall()
        for data in dataTable:
            if data[0] ==projeid:
                headline = data[3]
                print("headline : ",headline)
                for data2 in dataTable:
                    headline2 = data2[3]
                    print("headline 2 :",headline2)
                    print(self.text_to_text(headline,headline2))


    def matterSearch(self):
        pass

    def contentSearch(self,projeid):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[t_Projects]')
        dataTable = curs.fetchall()
        for data in dataTable:
            if data[0] ==projeid:
                headline = data[5]
                for data2 in dataTable:
                    other_proje_id = data2[0]
                    headline2 = data2[5]
                    result = self.text_to_text(headline,headline2)
                    print("Main proje {0} - Other Proje {1} - Benzerlik {2}".format(projeid,other_proje_id,result))

    def purposeSearch(self):
        pass

    def text_to_text(self,text1,text2):
        benzer_kelime_sayisi = 0
        text1 = text1.split()
        text2 = text2.split()
        for mt1 in text1:
            for mt2 in text2:
                if mt1 == mt2 and len(mt1) > 2 and len(mt2) > 2 :
                    benzer_kelime_sayisi += 1
        return benzer_kelime_sayisi

nesne = Search()
nesne.contentSearch(2)


# metin1 = []
# with open("metin1.txt","r") as f1:
#     metin1 = f1.read().split()
#
# metin2 = []
# with open("metin2.txt","r") as f2:
#     metin2 = f2.read().split()
#
# print("metin1 : ",metin1)
# print("metin2 : ",metin2)
#
# benzer_kelime_sayisi = 0
#
# for mt1 in metin1:
#     for mt2 in metin2:
#         if mt1 == mt2 and len(mt1) > 2 and len(mt2) > 2 :
#             benzer_kelime_sayisi += 1
#
# print("Benzer kelime sayisi : ",benzer_kelime_sayisi)
# print("Toplam kelime sayisi : ",str(len(metin1)+len(metin2)))
