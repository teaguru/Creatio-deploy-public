import psycopg2
class connector: 
  testname = "second2"
  def conndb():
      con = psycopg2.connect(
        database="postgres", 
        user="postgres", 
        password="123654-pP", 
        host="116.202.197.223", 
        port="5432"
    )
      print(con,"555")
      con.autocommit = True
      cur = con.cursor()
  
      return(cur)