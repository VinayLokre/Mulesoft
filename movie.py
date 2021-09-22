import sqlite3

conn=sqlite3.connect('data.sqlite')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS movie')
cur.execute('''CREATE TABLE movie (
id  INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT UNIQUE,
actor TEXT,
actress TEXT,
director TEXT,
year_of_release INTEGER
);''')
cur.execute("INSERT INTO movie (title,actor,actress,director,year_of_release) VALUES ('Bahubali','Prabhas','Tamanna','Rajamouli',2018)")
cur.execute("INSERT INTO movie (title,actor,actress,director,year_of_release) VALUES ('Sahoo','Prabhas','Shraddha','Sujeeth',2019)")
cur.execute("INSERT INTO movie (title,actor,actress,director,year_of_release) VALUES ('NenuLocal','Nani','Keerthi','ThrinadaRao',2017)")
cur.execute("INSERT INTO movie (title,actor,actress,director,year_of_release) VALUES ('MCA','Nani','SaiPallavi','DilRaju',2017)")
cur.execute("INSERT INTO movie (title,actor,actress,director,year_of_release) VALUES ('Arya','AlluArjun','AnuMeheta','Sukumar',2009)")
cur.execute("INSERT INTO movie (title,actor,actress,director,year_of_release) VALUES ('Sarrinodu','AlluArjun','Rakul','BoyapatiSenu',2016)")
cur.execute("INSERT INTO movie (title,actor,actress,director,year_of_release) VALUES ('DJ','AlluArjun','PooajHegde','HasishShankar',2017)")
cur.execute("INSERT INTO movie (title,actor,actress,director,year_of_release) VALUES ('RRR','NTR','AliaBhat','Rajamouli',2021)")


cur.execute('SELECT * FROM movie')
items = cur.fetchall()
for item in items:
    print(item)

s_actor=input('Enter the name of the actor: ')
cur.execute('SELECT title,actress,director,year_of_release FROM movie WHERE actor=?',(s_actor,))
elements=cur.fetchall()
for element in elements:
    print(element)
conn.commit()
