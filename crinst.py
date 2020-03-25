import zipfile
import os.path
import os
import lxml.etree as ET
# def inputpath():
# 		print('Enter path to the zip:')
# 		zippath = input()
# 		print(zippath)
# 		print(os.path.isfile(zippath))
# 		return(zippath)

# def inputexportpath():
# 	print('Input export path')
# 	export_path=input()
# 	if os.path.exists(export_path):
# 		print(export_path)
# 		return(export_path)
# 	else:
# 		print('directory not exist, make it?(y/n)')
# 		answ = input()
# 		if (answ == 'y'):
# 			try:
# 				os.makedirs(export_path)
# 			except OSError:
# 				print ("Создать директорию %s не удалось" % export_path)
# 			else:
# 				print ("Успешно создана директория %s" % export_path)
# 				return(export_path)
# 		else:
# 			print('ERROR')
	







# def export(zippath,exp_path):
# 	try:
# 		fantasy_zip = zipfile.ZipFile(zippath)
# 		fantasy_zip.extractall(exp_path)
# 		fantasy_zip.close()
# 	except OsError:
# 		print ("extraction %s not sucessfull" % exp_path)
# 	else:
# 		print ("sucessfull %s" % exp_path)

# export(zippath,exp_path)

# def read_connection(exp_path):
# 	string_path = exp_path + '\\' + 'ConnectionStrings.config'
# 	f = open(string_path, 'r+')
# 	for line in f:
# 		print(line)

# #def db_setting_input():


#string_path = exp_path + '\\' + 'ConnectionStrings.config'

def input_redis():
	print('input redis port between 0 and 85')
	flag = False
	while flag == False:
		port = input()
		if port.isdigit():
			port = int(port)
			if (port > 0 and port < 85 ):
				flag = True
				return port
			else:
				print("wrong port format, must be between 0 and 85")
		else:
			print("wrong format,not a number")			



def input_subd():
	print('select database postgres[1] or mssql [2]')
	# here we make default names for mssqk server, change it for your company
	defserv1 = "OWNEROR-774F19G"
	defserv2 = "OWNEROR-774F19G\SSDSERV"
	defserv3 = "116.202.197.223"
	flag_subd = False
	while flag_subd == False:
		db_name = input()	
		if int(db_name) == 1:
			print("Postgres")
			print("write postgres server adress, enter ip adress or server name. Also you can write 1 for the first default server{}".format(defserv3))
			servadr = input()
			if servadr == '1':
				servadr = defserv3	
			print("Ok it will be", servadr)
			return("Postgres",servadr)
			flag_subd = True

		if int(db_name) == 2:
			print("write server adress, enter ip adress or server name. Also you can write 1 for the first default server{} or 2 for the second default server {}".format(defserv1,defserv2))
			servadr = input()
			if servadr == '1':
				servadr = defserv1
			if servadr == '2':
				servadr = defserv2	
			print("Ok it will be", servadr)
			return("MSSQL",servadr)
			flag_subd = True
		else:
			print(" choose 1 or 2")	


def input_db():
	print('write dbname')
	db_name = input()
	print("database is:",db_name)
	print('input db user')
	db_user = input()
	print("user is:",db_user)
	print('input db password')
	db_psswd = input()
	print('******')
	db = {'name': db_name,'user': db_user,'password': db_psswd}
	
	return(db)			




def read_connection(db,subd,redis_port,exp_path):
	print(db['name'], 'debug')
	string_path = exp_path + '\\' + 'ConnectionStrings.config'
	with open(string_path, encoding='utf-8') as f:
		tree = ET.parse(f)
		
		root = tree.getroot()

		for elem in root.getiterator():
			try:
			
				print(elem.attrib.get("name"))
				server = subd[1]
				if elem.attrib.get("name") == 'db':
					if subd[0] == 'MSSQL':
						sb_conn = "{}; Initial Catalog={}; Persist Security Info=True; MultipleActiveResultSets=True; user={}; password={}; Pooling = true; Max Pool Size = 100; Async = true; Connection Timeout=500".format(server,db['name'],db['user'],db['password'])
					else:
						sb_conn = "Server={};Port=5432;Database={};User ID={};password={};Timeout=500; CommandTimeout=400;MaxPoolSize=1024;".format(server,db['name'],db['user'],db['password'])

					elem.attrib['connectionString'] = str(sb_conn)
			except AttributeError:
				print('error')
			try:
				print(elem.attrib.get("name"))
				if elem.attrib.get("name") == 'redis':
					print('ddd')
					elem.attrib['connectionString'] = elem.attrib['connectionString'].replace("host=;","host=localhost;")
					elem.attrib['connectionString'] = elem.attrib['connectionString'].replace("db=;","db={};".format(redis_port))
			except AttributeError:
				print('ddd')	
	tree.write(string_path, xml_declaration=True, method='xml', encoding="utf8")

if __name__ == '__main__':
    
    #zippath = inputpath()
    exp_path = 'E:\\testapp'
    subd = input_subd()
    db = input_db()
    redis_port = input_redis()
    
    read_connection(db,subd,redis_port,exp_path)
