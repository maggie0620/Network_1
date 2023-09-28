import re
file1 = open('D:/Network/Network 1.txt', 'r')
net1 = file1.read()
file2 = open('D:/Network/Network 2.txt', 'r')
net2 = file2.read()

## 1-1
# Network 1 Node數量
data1 = re.split('\t|\n', net1)
data1.remove('')
mylist1 = [] 
for node in data1:
    if node not in mylist1:
        mylist1.append(node)
print(len(mylist1))

# Network 1 Edge數量
split1 = re.split('\n', net1)
split1.remove('')
edge1 = []
for i in range(0,len(split1)):
    num1 = re.sub('\t','',split1[i])
    edge1.append(num1)
print(len(edge1))

# Network 2 Node數量
data2 = re.split('\t|\n', net2)
data2.remove('')
mylist2 = [] 
for node in data2:
    if node not in mylist2:
        mylist2.append(node)
print(len(mylist2))

# Network 2 Edge數量
split2 = re.split('\n', net2)
split2.remove('')
edge2 = []
for i in range(0,len(split2)):
    num2 = re.sub('\t','',split2[i])
    edge2.append(num2)
print(len(edge2))

## 1-2
# Network 1 是否為simple network
multi1 = []
for i in range(0,len(edge1)):
    element = sorted(edge1[i])
    multi1.append(element)

nonsimple = []
for k in range(0,len(multi1)):
    if multi1[k][0] == multi1[k][1]: #self-loops
        nonsimple.append(multi1[k])
    for j in range(k+1,len(multi1)): #multi-edges
        if multi1[k] == multi1[j] :
            nonsimple.append(multi1[k])

if nonsimple == []:
    print("Network 1 is simple.")
else:
    print("Network 1 is not simple.")
    print(multi1[k])

# Network 2 是否為simple network
multi2 = []
for i in range(0,len(edge2)):
    element = sorted(edge2[i])
    multi2.append(element)

nonsimple = []
for k in range(0,len(multi2)):
    if multi2[k][0] == multi2[k][1]: #self-loops
        nonsimple.append(multi2[k])
    for j in range(k+1,len(multi2)): #multi-edges
        if multi2[k] == multi2[j] :
            nonsimple.append(multi2[k])

if nonsimple == []:
    print("Network 2 is simple.")
else:
    print("Network 2 is not simple.")
    print("Nonsimple elements:", nonsimple)

## 1-3
# Network 1 the neighbors of node e
neigh_e1 = []
for k in range(0,len(multi1)):
    if "e" in multi1[k][0]:
        neigh_e1.append(multi1[k][1])
    elif "e" in multi1[k][1]:
        neigh_e1.append(multi1[k][0])
print("Neighbors of node e (Network 1):", neigh_e1)

# Network 1 the neighbors of node c
neigh_c1 = []
for k in range(0,len(multi1)):
    if "c" in multi1[k][0]:
        neigh_c1.append(multi1[k][1])
    elif "c" in multi1[k][1]:
        neigh_c1.append(multi1[k][0])
print("Neighbors of node c (Network 1):", neigh_c1)

# Network 2 the neighbors of node e (contains duplicated neighbor)
neigh_e2 = []
for k in range(0,len(multi2)):
    if "e" in multi2[k][0]:
        neigh_e2.append(multi2[k][1])
    elif "e" in multi2[k][1]:
        neigh_e2.append(multi2[k][0])
print("Neighbors of node e (Network 2):", neigh_e2)

# Network 2 the neighbors of node c (contains duplicated neighbor and self-neighbors)
neigh_c2 = []
for k in range(0,len(multi2)):
    if "c" in multi2[k][0]:
        neigh_c2.append(multi2[k][1])
    elif "c" in multi2[k][1]:
        neigh_c2.append(multi2[k][0])
print("Neighbors of node c (Network 2):", neigh_c2)

## 1-4
# Check if the inputted two nodes are adjacent (Network 1)
def adj1(node1,node2):
    IsBroken = False
    for k in range(0,len(multi1)):
        if [node1,node2] == multi1[k] or [node2,node1] == multi1[k]:
            IsBroken = True
            break
    if IsBroken == True:
        print("They are adjacent.")
    else:
        print("They are not adjacent.")

# Check if the inputted two nodes are adjacent (Network 2)
def adj2(node1,node2):
    IsBroken = False
    for k in range(0,len(multi2)):
        if [node1,node2] == multi2[k] or [node2,node1] == multi2[k]:
            IsBroken = True
            break
    if IsBroken == True:
        print("They are adjacent.")
    else:
        print("They are not adjacent.")

file1.close()
file2.close()

