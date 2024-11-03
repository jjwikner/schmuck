import mysql.connector

cnx = mysql.connector.connect(user='root', 
                              password='s0mmar!#$23',
                              host='127.0.0.1',
                              database='skeletor')

print(cnx)
curse = cnx.cursor()

curse.execute("SHOW TABLES")

for x in curse:
  print(x)

curse.execute("SELECT Move, Howl, Blink, Click from Actions")
for Move, Howl, Blink, Click in curse:
  print(Howl)
  

  
sql = "INSERT INTO Actions (Move, Howl, Blink, Click) VALUES (%s, %s, %s, %s)"
val = ("1","2","3","4")
curse.execute(sql, val)

cnx.commit()

print(curse.rowcount, "record inserted.")
cnx.close()
