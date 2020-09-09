'''
Given 2 Arrays

2nd one is shuffled and i element is taken
you have to find that element

'''

#Time Complexity is O(nlogn)
def FindMissingElement_usingSort(lst1, lst2):
	lst1 = sorted(lst1)
	lst2 =sorted(lst2)
	for i in range(len(lst2)):
		if lst1[i] != lst2[i]:
			return lst1[i]
	return None

#print(FindMissingElement_usingSort([1,4,2,3,5, 6, 7], [4,5,2,6,7,1]))


#Time Complexity is O(n)
def FindMissingElement_usingDict(lst1, lst2):
	lst2_dict = {}

	for i in lst2:
		if i in lst2_dict: lst2_dict[i] += 1
		else: lst2_dict[i] = 0

	for i in lst1:
		if i not in lst2_dict: return i

	return None

#print(FindMissingElement_usingDict([1,4,2,3,5, 6, 7], [4,5,2,6,7,1]))




#Best Method but Doesnt work in all Cases (misses Accuracy in case of Floats)
def FindMissingElement_usingSum(lst1, lst2):
	return sum(lst1) - sum(lst2)

print(FindMissingElement_usingSum([1,4,2,3,5, 6, 7], [4,5,2,6,7,1]))
