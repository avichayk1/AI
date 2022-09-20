import random

def create_rundom(n):#defind function that create random board
   board=[]#defind arrey/list(range(n))
   for i in range(n):
       board.append(random.randrange(n))#randomize number between 0-n//board[i]=randrange(n)//append =to add
   return x#return arrey
def threats(b,n):#this is our horistic
    c=0
    for i in range(n):
        for j in range(n):
            if b[i]==b[j] or abs(i-j)==abs(b[i]-b[j]):
               c=c+1
        c=c-1
    return int(c/2)

def improve(b,n):
    min = threats(b,n)
    improved=b[:]#copy arrey not pointer on the same
    for i  in range(n):
        for r in range(n):
             b[0]=r
             x=threats(b,n)
             print(x)
             if x < min:
                improved = b[:]
                min = x
        b=improved
    return min
        #for c in range(n):
         #   b[r]=c
          #  x=threats(b,n)
           # if x<min:
            #    min=x
             #   improved=b[:]
       # b[r]=tmp
    #b=improved[:]
    #return min

b=[0,1,0,3]#create_rundom(4)
#print(create_rundom(4))#start the function with n=4

print (b)
print (threats(b,4))
improve (b,4)
print (b)