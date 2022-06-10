import random
lotto=[]
while len(lotto) < 6:
    num = random.randint(1,45) #1<=x<=45
    if num not in lotto:
        lotto.append(num)

print("pick list : ",end=""); print(lotto)
lotto.sort(reverse=True)
print("sorted list(ASC) : ", end=""); print(lotto)
lotto.sort()
print("sorted list(DESC) : ", end=""); print(lotto)