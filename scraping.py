from bs4 import BeautifulSoup
import requests
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='scraping',
)
mycursor = mydb.cursor()

response = requests.get('https://www.panganku.org/id-ID/semua_nutrisi')

soup = BeautifulSoup(response.text,'html.parser')
rows = soup.find('table',{'id':'data'}).find('tbody').find_all('tr')

for row in rows:
    sql = "INSERT INTO pangan (nama_pangan, kelompok, tipe) VALUES (%s, %s, %s)"
    value = (row.find_all('td')[2].text, row.find_all('td')[3].text, row.find_all('td')[4].text)
    mycursor.execute(sql, value)
    mydb.commit()
    print('insert')
