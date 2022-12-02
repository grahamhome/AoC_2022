import sys

class SortedLimitedList:
    def __init__(self, limit):
    	self.limit = limit
    	self.items = []
    	
    def append(self, item):
    	if len(self.items) < self.limit:
    		self.items.append(item)
    		self.items.sort()
    	elif item > self.items[0]:
    		self.items = sorted([*self.items[1:], item])
    

def richest_elves(filepath):
	richest_elves = SortedLimitedList(3)
	current = 0
	for item in [*list(map(lambda i: i.strip(), open(filepath).readlines())), ""]:
		if item != "":
			current += int(item)
		else:
			richest_elves.append(current)
			current = 0
	return sum(richest_elves.items)
	
print(richest_elves(sys.argv[1]))
