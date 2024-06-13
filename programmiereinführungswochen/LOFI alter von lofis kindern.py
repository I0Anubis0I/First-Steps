alter=[2,3,4,1]
i=0
for i in range(3):
    if alter[i]<alter[i+1]:
        print(alter[i], "ist jünger als", alter[i+1])
    else:
        print(alter[i], "ist älter als", alter[i+1])