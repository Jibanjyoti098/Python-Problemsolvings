# l = [12, 32, 45, 12, 32, 7, 4, 45]
# count = 0
# lCopy = l.copy()
# lCopy.sort()
# k = len(lCopy)
# # print(l)# [4, 7, 12, 12, 32, 32, 45, 45]
# for o in range(k):
#     if lCopy[o] == lCopy[o+1]:
#         lCopy.pop(lCopy[o])
#         count += 1
#     k = len(lCopy)-count
# print("New list =", lCopy)

# failed
l = [12, 32, 45, 12, 32, 7, 4, 45]
newLi = []
for i in range(0, len(l)):
    if l[i] not in newLi:
        newLi.append(l[i])

print(newLi)
