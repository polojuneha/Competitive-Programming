def merge_intervals(intervals):
	
	s = sorted(intervals, key=lambda tup: tup[0])
	merge = []

	for tup in s:
		if not merge:
			merge.append(tup)
		else:
			a = merge.pop()
			print(a)
			if a[1] >= tup[0]:
				new_tup = tuple([a[0], tup[1]])
				merge.append(new_tup)
			else:
				merge.append(a)
				merge.append(tup)
	print("*--",merge,"--*")
	return merge

if __name__ == '__main__':

	k = [(1, 4), (2, 5), (5, 8)]
	print("Original list of ranges: {}".format(k))
	merged_list = merge_intervals(k)
	print("List of ranges after merge_ranges: {}".format(merged_list))