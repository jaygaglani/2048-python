import random
print('enter a number for N X N game matrix')
n=int(input())
gameboard=[[' ' for i in range(n)] for j in range(n)]

def gamescore(gameboard):
    score=0
    for i in range(n):
        for j in range(n):
            if gameboard[i][j]!=' ':score+=int(gameboard[i][j])
    return score

def gamestatus(gameboard):#retutns a list of empty cells for randomization
    lst=[]
    for i in range(n):
        for j in range(n):
            if gameboard[i][j]==' ':lst.append([i,j])
    return lst

def gameupdate(s,gameboard):
    
    temp2=[[' ' for i in range(n)] for j in range(n)]
    c=0

    if s=='a':#left
        for i in range(1,n):#i-->col
            for j in range(n):#j-->row
                if gameboard[j][i]!=' ':
                    temp=gameboard[j][i]#
                    for k in range(i-1,-1,-1):#k-->col
                        if gameboard[j][k]==temp and temp2[j][k]!=1:
                            c+=1
                            gameboard[j][k]=str(2*int(temp))
                            temp2[j][k]=1
                            gameboard[j][k+1]=' '
                        elif gameboard[j][k]==' ':
                            c+=1
                            gameboard[j][k]=temp
                            gameboard[j][k+1]=' '
                        else:
                            break
    if s=='d':#right              
       for i in range(n-2,-1,-1):#i-->col
            for j in range(n):#j-->row
                if gameboard[j][i]!=' ':
                    temp=gameboard[j][i]
                    for k in range(i+1,n):#k-->col
                        if gameboard[j][k]==temp and temp2[j][k]!=1:
                            c+=1
                            gameboard[j][k]=str(2*int(temp))
                            temp2[j][k]=1
                            gameboard[j][k-1]=' '
                        elif gameboard[j][k]==' ':
                            c+=1
                            gameboard[j][k]=temp
                            gameboard[j][k-1]=' '
                        else:
                            break
        
    if s=='w':#up
        for i in range(1,n):#i-->row
            for j in range(n):#j-->col
                if gameboard[i][j]!=' ':
                    temp=gameboard[i][j]
                    for k in range(i-1,-1,-1):#k-->row
                        if gameboard[k][j]==temp and temp2[j][k]!=1:
                            c+=1
                            gameboard[k][j]=str(2*int(temp))
                            temp2[j][k]=1
                            gameboard[k+1][j]=' '
                        elif gameboard[k][j]==' ':
                            c+=1
                            gameboard[k][j]=temp
                            gameboard[k+1][j]=' '
                        else:
                            break
        
    if s=='s':#down
        for i in range(n-2,-1,-1):#i-->row
            for j in range(n):#j-->cow;
                if gameboard[i][j]!=' ':
                    temp=gameboard[i][j]
                    for k in range(i+1,n):#k-->row
                        if gameboard[k][j]==temp and temp2[j][k]!=1:
                            c+=1
                            gameboard[k][j]=str(2*int(temp))
                            temp2[j][k]=1
                            gameboard[k-1][j]=' '
                        elif gameboard[k][j]==' ':
                            c+=1
                            gameboard[k][j]=temp
                            gameboard[k-1][j]=' '
                        else:
                            break
                        
    if c>0 or len(gamestatus(gameboard))==n*n:
        temp=gamestatus(gameboard)
        temp1=random.choice(temp)
        temp2=random.choice(['2','2','4'])
        gameboard[temp1[0]][temp1[1]]=temp2
        return gameboard
    
    return gameboard
        
def gameover(gameboard):#checks if any moves possible
    for i in range(n):
        for j in range(n):
            if i-1>=0 and gameboard[i-1][j]==gameboard[i][j]:return False
            if j-1>=0 and gameboard[i][j-1]==gameboard[i][j]:return False
            if i+1<n and gameboard[i+1][j]==gameboard[i][j]:return False    
            if j+1<n and gameboard[i][j+1]==gameboard[i][j]:return False
    return True

def gameprint(gameboard):
    for i in range(n):
        print(gameboard[i])

gameupdate('a',gameboard)
gameprint(gameboard)

while gamestatus(gameboard)!=[] or gameover(gameboard)!=True:#game is not over
    print('enter move: w a s d?')
    s=input()
    if s=='q':break
    if s not in ['w','a','s','d']:
        print('invalid input')
        continue
    gameupdate(s,gameboard)
    gameprint(gameboard)

print('game over!!! your score:'+'\n'+str(gamescore(gameboard)))        
