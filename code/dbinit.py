import os
try:
    os.unlink('toeic.db')
except:
    print('首次建檔')

import sqlite3
conn = sqlite3.connect('toeic.db')
cur = conn.cursor()

def show_all_rows(all_rows):
    for row in all_rows:
        print(row)
    print()

# 單字表
cur.execute('''CREATE TABLE WORDS
    (ID integer, WORD text, DEFINITIONS text)''')
conn.commit()
# 單字表批次新增資料
row_id = 0
fin = open('toeic-words.txt', 'rt', encoding='utf-8')
lines = fin.readlines()
for line in lines:
    row_id += 1
    word, definition = line.split(' -> ')
    cur.execute("INSERT INTO WORDS VALUES (?, ?, ?)", (row_id, word, definition.strip('\n')))
conn.commit()    
fin.close()
# 查詢單字表
cur.execute("SELECT * FROM WORDS")
show_all_rows(cur.fetchall())

# 設定表
cur.execute('''CREATE TABLE SETTINGS
    (ID integer, TYPE text, NUM_OF_QUESTIONS integer, OPTION integer)''')
# 設定表初始資料
cur.execute("INSERT INTO SETTINGS VALUES (1, 'multiple_choice', 10, 4)")
cur.execute("INSERT INTO SETTINGS VALUES (2, 'fill_in_the_blank', 10, 1)")
conn.commit()
# 查詢設定表
cur.execute("SELECT * FROM SETTINGS")
show_all_rows(cur.fetchall())

# 考生表
cur.execute('''CREATE TABLE EXAMINEES
    (ID integer, ACCOUNT text, NAME text, GENDER text, BIRTH_YEAR integer)''')
# 考生表初始資料
cur.execute("INSERT INTO EXAMINEES VALUES (1, 'john', 'John Doe', 'M', 1980)")
cur.execute("INSERT INTO EXAMINEES VALUES (2, 'jane', 'Jane Doe', 'F', 1985)")
conn.commit()
# 查詢考生表
cur.execute("SELECT * FROM EXAMINEES")
show_all_rows(cur.fetchall())

# 成績表
cur.execute('''CREATE TABLE SCORES
    (ID integer, ACCOUNT text, TYPE text, SCORE integer, DATE_TIME text)''')
# 成績表初始資料
cur.execute("INSERT INTO SCORES VALUES (1, 'john', 'multiple_choice', 100, '2020-04-02')")
cur.execute("INSERT INTO SCORES VALUES (2, 'jane', 'multiple_choice', 100, '2020-04-02')")
conn.commit()
# 查詢成績表
cur.execute("SELECT * FROM SCORES")
show_all_rows(cur.fetchall())

conn.close()
