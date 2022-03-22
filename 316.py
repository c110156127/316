import random
tmp = [1,2,3]
aaa = (1,2,3)
tmp[0]=2

k = "c1101561"
d = []
for i in range(1,60):
    d.append(k+'{0:02d}'.format(i))


grade = []
for i in range(1,60):
    grade.append(random.randint(0,100))

#dict
tmp2 = {"c110156101":88,"c110156102":78,"c110156103":90}
print(grade[0])
print(tmp2["c110156103"])