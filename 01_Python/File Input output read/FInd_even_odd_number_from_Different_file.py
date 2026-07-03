count = 0

with open("practice.txt", "r") as f:
    data = f.read()

    num = data.split(",")

    for val in num:
        if int(val) % 2 == 0:
            count += 1

print(count)