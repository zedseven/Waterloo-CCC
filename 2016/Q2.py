line1 = input("").split(" ")
line2 = input("").split(" ")
line3 = input("").split(" ")
line4 = input("").split(" ")

for i in range(4):
    line1[i] = int(line1[i])
    line2[i] = int(line2[i])
    line3[i] = int(line3[i])
    line4[i] = int(line4[i])

l1Total = line1[0] + line1[1] + line1[2] + line1[3]

req = l1Total

l2Total = line2[0] + line2[1] + line2[2] + line2[3]
l3Total = line3[0] + line3[1] + line3[2] + line3[3]
l4Total = line4[0] + line4[1] + line4[2] + line4[3]
        
c1Total = line1[0] + line2[0] + line3[0] + line4[0]
c2Total = line1[1] + line2[1] + line3[1] + line4[1]
c3Total = line1[2] + line2[2] + line3[2] + line4[2]
c4Total = line1[3] + line2[3] + line3[3] + line4[3]

if req == l2Total and req == l3Total and req == l4Total and req == c1Total and req == c2Total and req == c3Total and req == c4Total:
    print("magic")
else:
    print("not magic")
