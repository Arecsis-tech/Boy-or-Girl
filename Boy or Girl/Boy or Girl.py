user=str(input())
new=[]
for i in range (len(user)):
    if user[i] not in new:
        new.append(user[i])
if len(new)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
