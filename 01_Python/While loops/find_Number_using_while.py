# Tupple Number Find
n=int(input("write num to find: "))
num = (2,3,4,64,67,877,235,875,123)
i=0
while i < len(num):
    if n == num[i]:
        print("number Found")
        break
    i += 1
else:
    print("Not Found")
        
    


