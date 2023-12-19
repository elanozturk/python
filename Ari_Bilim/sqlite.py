import sqlite3

conn = sqlite3.connect("my_db.sqlite")  #bu isimde bi db yoksa oluşturup bağlanır, varsa bağlanır.

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS cihazlar(
  isim TEXT,
  personel TEXT,
  marka TEXT,
  model TEXT,
  ssd INTEGER,
  ram INTEGER,
  fiyat REAL
)""")

c.execute("""INSERT INTO cihazlar VALUES(
    'Tarkan Tevetoğlu',
    'Furkan Kazan',
    'Apple',
    'iPhone 15 Pro Max',
    256,
    16,
    99000
    )""")

conn.commit()