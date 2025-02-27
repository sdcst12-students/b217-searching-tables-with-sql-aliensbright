#!python3
import sqlite3
"""What is the structure of the table?  What are the columns and what datatypes do they store?
Rows
  id = integer (object id) | strength = tinyint | intelligence = tinyint | wisdom = tinyint | dexterity = tinyint | constitution = tinyint | charisma = tinyint | class = tinytext | level = tinyint | hp = tinyint | gold = tinyint

Columns
  different objects/records

How many records are in the table?
  10000 Correct
How many Knights are in the table?
  780 Correct
Which class has the highest number of members?
  Thief Correct
What is the ID number of the Jester with the most gold?
  7907 Correct
What is the total gold of the 100 wealthiest npc's in the table?
  4917 Correct
What is the total gold of the 100 wealthiest npc's under level 5?
  1967 Correct
What is the stats of the Bard with the highest strength?
  (id,strength,intelligence,wisdom,dexterity,constitution,charisma,class,level,hp,gold)
  (3672, 18, 7, 13, 8, 11, 12, 'Bard', 5, 22, 23)  Correct
What is the ID number of the npc with highest total sum of their 6 primary stats?
  8693 Correct
What percentage of all fighter classes (Barbarian, Warrior, Knight, Samurai) are Warriors?
  23.72%
What is the average hitpoints per level of the npc's that are level 10 or higher?
  4.5 Correct

"""
ids = []
connection = sqlite3.connect('dbase.db')
cursor = connection.cursor()

cursor = connection.cursor()
cursor.execute('PRAGMA table_info(npc);')

###Count of Knights and Highest Class

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
countPriest = len(cursor.fetchall())

qThief = "select id from npc where class = 'Thief'"
cursor.execute(qThief)
countThief = len(cursor.fetchall())

qBard = "select id from npc where class = 'Bard'"
cursor.execute(qBard)
countBard = len(cursor.fetchall())

qBarbarian = "select id from npc where class = 'Barbarian'"
cursor.execute(qBarbarian)
countBarbarian = len(cursor.fetchall())

qMonk = "select id from npc where class = 'Monk'"
cursor.execute(qMonk)
countMonk = len(cursor.fetchall())

qAssassin = "select id from npc where class = 'Assassin'"
cursor.execute(qAssassin)
countAssassin = len(cursor.fetchall())

qJester = "select id from npc where class = 'Jester'"
cursor.execute(qJester)
countJester = len(cursor.fetchall())

qSamurai = "select id from npc where class = 'Samurai'"
cursor.execute(qSamurai)
countSamurai = len(cursor.fetchall())
    
print('A',countAssassin,'\nBarb',countBarbarian,'\nBard',countBard,'\nJ',countJester,'\nK',countKnight,'\nM',countMonk,'\nP',countPriest,'\nR',countRanger,'\nSage',countSage,'\nSam',countSamurai,'\nSor',countSorcerer,'\nT',countThief,'\nW',countWarrior)


### Jester with highest gold.

qJester = "select id from npc where class='Jester' order by gold desc"
cursor.execute(qJester)
countJ = cursor.fetchone()
print(countJ,'jester')


### What is the total gold of the 100 wealthiest npc's in the table?

qGold = "select gold from npc order by gold desc limit 100"
cursor.execute(qGold)
listGold = cursor.fetchall()
print(listGold,type(listGold))
countGold = 0

for a in listGold:
  for i in a:
    i = int(i)
    countGold += i

print('gold',countGold)


###What is the total gold of the 100 wealthiest npc's under level 5?

qGold = "select gold from npc where level < 5 order by gold desc limit 100"
cursor.execute(qGold)
listGold = cursor.fetchall()
print(listGold,type(listGold))
countGold = 0

for a in listGold:
  for i in a:
    i = int(i)
    countGold += i

print('gold',countGold)


###What is the stats of the Bard with the highest strength?

qStats = "select * from npc where class = 'Bard' order by strength desc"
cursor.execute(qStats)
Stats = cursor.fetchone()
print(Stats)


###What is the ID number of the npc with highest total sum of their 6 primary stats?
"""str 5
int 7
wis 10
dex 8
con 6
cha 5"""

qSum = "select id, strength, intelligence, wisdom, dexterity, constitution, charisma from npc"
cursor.execute(qSum)
Stats = cursor.fetchall()
#print(Stats)
listSumStats = [] #This will be the list with the sum of the records and the corresponding id value
for record in Stats:
  sumOfOne = record[1] + record[2] + record[3] + record[4] + record[5] + record[6]
  listSumStats.append((sumOfOne,record[0]))
#print(listSumStats)
print(max(listSumStats))

###What percentage of all fighter classes (Barbarian, Warrior, Knight, Samurai) are Warriors?

#countWarrior
#sum of Barb, warrior, knight, samurai


totalFighter = countBarbarian + countWarrior + countKnight + countSamurai
percentageBarb = round(countBarbarian / totalFighter * 100,2)
print('percentageBarb',percentageBarb)

###What is the average hitpoints per level of the npc's that are level 10 or higher?

qHitpoints = "select hp, level from npc where level >= 10"
cursor.execute(qHitpoints)
HitpointLevel = cursor.fetchall()
#print(HitpointLevel)
sumHitpoints = 0
sumLevel = 0

for i in HitpointLevel:
  sumHitpoints += i[0]
  sumLevel += i[1] 

hpPerLevel = round(sumHitpoints / sumLevel,2)
print(hpPerLevel)