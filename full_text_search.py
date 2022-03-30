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
        self.intihal = {}

    def headlineSearch(self,projenumber):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[t_Projects]')
        dataTable = curs.fetchall()
        dicte = {}
        for data in dataTable:
            if data[1] ==projenumber:
                headline = data[3]
                for data2 in dataTable:
                    headline2 = data2[3]
                    if data2[1] != projenumber:
                        intihal = self.text_to_text(headline,headline2)
                        dicte.update({data2[1]:intihal})
        self.intihal.update({"headline":dicte})

    def matterSearch(self,projenumber):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[t_Projects]')
        dataTable = curs.fetchall()
        dicte = {}
        for data in dataTable:
            if data[1] ==projenumber:
                headline = data[4]
                for data2 in dataTable:
                    headline2 = data2[4]
                    if data2[1] != projenumber:
                        intihal = self.text_to_text(headline,headline2)
                        dicte.update({data2[1]:intihal})
        self.intihal.update({"matter":dicte})

    def contentSearch(self,projenumber):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[t_Projects]')
        dataTable = curs.fetchall()
        dicte = {}
        for data in dataTable:
            if data[1] ==projenumber:
                headline = data[5]
                for data2 in dataTable:
                    headline2 = data2[5]
                    if data2[1] != projenumber:
                        intihal = self.text_to_text(headline,headline2)
                        dicte.update({data2[1]:intihal})
        self.intihal.update({"content":dicte})

    def purposeSearch(self,projenumber):
        curs = self.db.cursor()
        curs.execute('SELECT * FROM [abdullah_pys].[t_Projects]')
        dataTable = curs.fetchall()
        dicte = {}
        for data in dataTable:
            if data[1] ==projenumber:
                headline = data[6]
                for data2 in dataTable:
                    headline2 = data2[6]
                    if data2[1] != projenumber:
                        intihal = self.text_to_text(headline,headline2)
                        dicte.update({data2[1]:intihal})
        self.intihal.update({"purpose":dicte})

    def text_to_text(self,text1,text2):
        benzer_kelime_sayisi = 0
        text1 = text1.split()
        text2 = text2.split()
        toplam_kelime_sayisi = len(text1) + len(text2)
        for mt1 in text1:
            for mt2 in text2:
                if mt1 == mt2 and len(mt1) > 2 and len(mt2) > 2 :
                    benzer_kelime_sayisi += 1
        yuzde = round(benzer_kelime_sayisi/toplam_kelime_sayisi*100,2)
        return yuzde

    def allin(self,projenumber):
        self.matterSearch(projenumber)
        self.headlineSearch(projenumber)
        self.contentSearch(projenumber)
        self.purposeSearch(projenumber)
        matter = self.intihal["matter"]
        content = self.intihal["content"]
        purpose = self.intihal["purpose"]
        headline = self.intihal["headline"]
        for i in matter:
            genel_toplam = 0
            genel_toplam += matter[i]
            genel_toplam += content[i]
            genel_toplam += purpose[i]
            genel_toplam += headline[i]
            genel_ort = int(genel_toplam/4)
            self.plagiarism_insert(int(projenumber),i,genel_ort)
            print("allin succes")
            # print("Main : {0} - Other : {1} - İntihal : {2}".format(projenumber,i,genel_ort))

    def plagiarism_insert(self,mainprojeid,otherprojeid,plagrismrate):
        try:
            curs = self.db.cursor()
            curs.execute("insert into t_Plagiarism(mainProjeID,otherProjeID,plagiarismRate) values (?,?,?)",
                         mainprojeid,
                         otherprojeid,
                         plagrismrate)
            curs.commit()
            return "Successful"
        except Exception as e:
            e = str(e)
            return e




# nesne = Search()
# nesne.allin("1114738")

