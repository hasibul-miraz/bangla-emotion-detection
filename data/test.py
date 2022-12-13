x = [1,2,2,3,4,5,6,8]

for ele in x:
    if ele % 2 == 0:
        x.remove(ele)

print(x)