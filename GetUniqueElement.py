'''
Get unique elements from a list
'''
v = [1,3,2,4,7,3,3,4,5,11]

def get_num_uniques(v):
  count = []
	dup = []
	tmp = []
	for i in v:
		if i not in count:
			count.append(i)
		else:
			dup.append(i)
			count.remove(i)
	for j in count:
		if j not in dup:
			tmp.append(j)

	return tmp

print get_num_uniques(v)
