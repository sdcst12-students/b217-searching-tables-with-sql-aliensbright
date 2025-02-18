#!python3
import sqlite3
"""What is the structure of the table?  What are the columns and what datatypes do they store?
Rows
  id = integer (object id) | strength = tinyint | intelligence = tinyint | wisdom = tinyint | dexterity = tinyint | constitution = tinyint | charisma = tinyint | class = tinytext | level = tinyint | hp = tinyint | gold = tinyint

Columns
  different objects/records

How many records are in the table?
    10000
How many Knights are in the table?
    780
Which class has the highest number of members?

What is the ID number of the Jester with the most gold?
What is the total gold of the 100 wealthiest npc's in the table?
What is the total gold of the 100 wealthiest npc's under level 5?
What is the stats of the Bard with the highest strength?
What is the ID number of the npc with highest total sum of their 6 primary stats?
What percentage of all fighter classes (Barbarian, Warrior, Knight, Samurai) are Warriors?
What is the average hitpoints per level of the npc's that are level 10 or higher?
"""
ids = []
connection = sqlite3.connect('dbase.db')
cursor = connection.cursor()

cursor = connection.cursor()
cursor.execute('PRAGMA table_info(npc);')



qKnight = "select id from npc where class = 'Knight'" 
cursor.execute(qKnight)
countKnight = len(cursor.fetchall())

qWarrior = "select id from npc where class = 'Warrior'"
cursor.execute(qWarrior)
countWarrior = len(cursor.fetchall())

qRanger = "select id from npc where class = 'Ranger'"
cursor.execute(qRanger)
countRanger = len(cursor.fetchall())

qSorcerer = "select id from npc where class = 'Sorcerer'"
cursor.execute(qSorcerer)
countSorcerer = len(cursor.fetchall())

qSage = "select id from npc where class = 'Sage'"
cursor.execute(qSage)
countSage = len(cursor.fetchall())

qPriest = "select id from npc where class = 'Priest'"
cursor.execute(qPriest)
countPriest = cursor.fetchall()

qThief = "select id from npc where class = 'Thief'"
cursor.execute(qThief)
countThief = cursor.fetchall()

qBard = "select id from npc where class = 'Bard'"
cursor.execute(qBard)
countBard = cursor.fetchall()

qBarbarian = "select id from npc where class = 'Barbarian'"
cursor.execute(qBarbarian)
countBarbarian = cursor.fetchall()

qMonk = "select id from npc where class = 'Monk'"
cursor.execute(qMonk)
countMonk = cursor.fetchall()

qAssassin = "select id from npc where class = 'Assassin'"
cursor.execute(qAssassin)
countAssassin = cursor.fetchall()

qJester = "select id from npc where class = 'Jester'"
cursor.execute(qJester)
countJester = cursor.fetchall()

qSamurai = "select id from npc where class = 'Samurai'"
cursor.execute(qSamurai)
countSamurai = cursor.fetchall()
    
print(max())