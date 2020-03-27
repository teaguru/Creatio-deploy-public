import psycopg2


class Connector(object):
    def __init__(self):
        exp_path = 'E:\\testapp'

    @staticmethod
    def conndb():
        con = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="xxxx",
            host="116.202.197.xxx",
            port="5432"
        )
        print(con, "555")
        con.autocommit = True
        cur = con.cursor()

        return(cur)

    def checkdb(self, cur, testname):

        print("Database opened successfully")
        data = cur.execute("select * from pg_database;")
        rows = cur.fetchall()
        listx = list()
        for elem in rows:
            listx.append((elem[0]))
        print(listx)
        if testname in listx:
            print('Name in the list')
            return(False)
        print('Not in the list')
        return(True)


def __init__(self):
    print("init")


if __name__ == '__main__':
    testname = "second2"
    con = Connector.conndb()
    obj = Connector()
    exist = obj.checkdb(con, testname)
