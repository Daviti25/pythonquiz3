import requests
import json
import sqlite3
from win10toast import ToastNotifier

def connection(database):
    return sqlite3.connect(database)

def api_1(url):
    resp = requests.get(url)
    print(resp.status_code)
    print(resp.headers)
    print(resp.text)

def api_2(url):
    resp = requests.get(url).text
    resp_structured = json.dumps(json.loads(resp), indent=4)
    json_file = open("jsonfile.json", "w")
    json_file.write(resp_structured)
    json_file.close()

def api_2_2(url):
    resp = requests.get(url).text
    resp_structured = json.dumps(resp, indent=2)
    json_file = open("jsonfile1.json", "w")
    json_file.write(resp_structured)
    json_file.close()


'''ეს ფუნქცია არის 3-4-6 დავალების
(ბაზის შექმნის კოდი ბოლოში 
მაქ გადაკოპირებული)'''

def api_3_4_6(conn, url):
    cursor = conn.cursor()
    resp = requests.get(url).text
    resp_dict = json.loads(resp)
    keys = ['name', 'actor', 'gender', 'dateOfBirth', 'house', 'image']
    list_values = []
    index = int(input("Index: "))
    for key in keys:
         print(resp_dict[index][key])
         list_values.append(resp_dict[index][key])
    tuple_values = tuple(list_values)
    cursor.execute('insert into Harry_Potter (name, actor, gender, birth_date, house, image) values (?,?,?,?,?,?)', tuple_values)
    conn.commit()
    notifier = ToastNotifier()
    notifier.show_toast("Your information", "Name : {}".format(list_values[0]),  duration = 5)

def main():
    conn = connection('Harry-Potter.sqlite')
    # api_1('https://hp-api.onrender.com/api/characters')
    # api_2('https://hp-api.onrender.com/api/characters')
    # api_2_2('https://hp-api.onrender.com/api/characters')
    # api_3_4_6(conn, 'https://hp-api.onrender.com/api/characters')


if __name__ == '__main__' :
    main()


# cursor.execute('''create table Harry_Potter
    #                 (id integer primary key autoincrement,
    #                 name varchar(100),
    #                 actor varchar(100),
    #                 gender varchar(100),
    #                 birth_date date,
    #                 house varchar(100),
    #                 image varchar(100));''')
    # conn.commit()