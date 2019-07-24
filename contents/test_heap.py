import heapq

li = [(5, "NA"),(7, "NV"), (9, "NY"), (1, "CA"), (3, "AL")]
# li = [5, 7, 9, 1, 3] 

# print(li)
# li.sort()
# print(li)
# print(li[0][0])


# li2 = [1,4,2,6]
# print(li2)
# li2.sort()
# print(li2)

heapq.heapify(li)

print(list(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
print(list(li))

heapq.heappush(li, (1, 'TW'))
print(list(li))