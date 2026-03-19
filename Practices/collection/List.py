l = []
print(l)
l1 = [10, 20.5, True, "Aaa", 10]
print(l1) #Insertion order preserved
print(l1[0])
print(l1[-1])
print(l1[1:4]) #Include:Exclude

# Growable in size
l.append(60)
l.extend([10,20,30,70,50,40])
l.sort() #Bydefault it sorts  ascending order
l.sort(reverse=True) #Descening order
print(l)
l.insert(0,{'a':3, 'b':4})
print(l)
print(l[0]["a"])
l.pop(1)
print(l)
l.remove({'a':3, 'b':4})
print(l)
