import random
def binary_search(list, x):
	m = len(list)/2
	if list[m] == x:
		return True
	if len(list)==1:
		return False
	if x < list[m]:
		return binary_search(list[:m], x)
	if x > list[m]:
		return binary_search(list[m:], x)

lst = []
for i in range(2000000):
	if random.random() < 0.75:
		lst.append(i)

print(lst[:2000000])
print(binary_search(lst, 10000))