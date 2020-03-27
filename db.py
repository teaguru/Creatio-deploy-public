import psycopg2
testname = "second2"
def conndb():
  con = psycopg2.connect(
    database="postgres", 
    user="postgres", 
    password="xxx", 
    host="116.202.197.xxx", 
    port="5432"
  )
  print(con,"555")
  con.autocommit = True
  cur = con.cursor()
 
  return(cur)
  
  
  
def checkdb(cur,testname):
  
  exp_path = 'E:\\testapp'
  print("Database opened successfully")
  data = cur.execute("select * from pg_database;")
  rows = cur.fetchall()
  listx = list()
  for elem in rows:
        listx.append((elem[0]))
  print(listx)
  if testname in listx:
    print('777')  
    return(False)
  print('555')
  return(True)                 

def createdb(exist,cur):
  if exist == True:
    sql = "CREATE DATABASE test WITH OWNER postgres  TEMPLATE template0;" 
    data = cur.execute(sql)   
            

#conndb()
con = conndb()
exist = checkdb(con,testname)
createdb(exist,con)