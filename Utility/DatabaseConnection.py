import pyodbc
class DBConnection:
    cnxn = ""
    def __init__(self):
        self.cnxn = pyodbc.connect('DRIVER={SQL Server};'
                              'SERVER={atxcccwmdb-q04.devid.local};'
                              'DATABASE={TestDB};'
                              'Trusted_Connection=yes;')
        self.cursor = self.cnxn.cursor()

    def connect(self,query,val):
        self.cursor.execute(query,(val))
        self.cnxn.commit()


    def FetchTableResult(self,query,val):
        self.cursor.execute(query,(val))
        columns = [column[0] for column in self.cursor.description]
        result = dict(zip(columns, self.cursor.fetchone()))
        return result


    def FetchResult(self,query,val):
        self.cursor.execute(query,(val))
        result = self.cursor.fetchone()
        res = [x for x in result]
        return res[0]

