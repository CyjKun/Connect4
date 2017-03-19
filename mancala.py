player1 = [4,4,4,4]
computerplayer = [4,4,4,4]
home1 = 0
home2 = [0]
pebblesinhand = 0
def boardShow():
 print (home1)
 print (player1)
 print (computerplayer)
 print (home2)

print (boardShow())
print("Select index to start game: ")
x = int(input())

#print (player1[x])
pebblesinhand = pebblesinhand + player1[x]
#print (pebblesinhand)

#def addPebble(pebblesinhand):
'''
while pebblesinhand != 0:
 print (pebblesinhand)
 pebblesinhand -= 1
 if pebblesinhand == 0:
  home1 += 1
  computerplayer[pebblesinhand] += 1
'''
'''
y = 0
while player1[x] != 0:
 if player1[0] == 0:
  home1+=1
 computerplayer[y] += 1
 y+=1
 player1[x] -= 1
 #if player1[0] == 0:
  #home1 +=player[player1[x]] += 1
'''
y = 0
player1[x] = 0

if player1[0] == 0:
 home1 += 1
 computerplayer[y] += 1
 y += 1
 computerplayer[y] += 1
 y += 1
 computerplayer[y] += 1

if player1[1] == 0:
    player1[0] += 1
    home1 += 1    

    
#print (addPebble(pebblesinhand))
print (boardShow())

