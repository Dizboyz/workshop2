# EX 1
setl = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set3 = setl.union(set2)
print(set3)  # Output: {'c', 'a', 'd', 'e', 'b', 'f'}
# EX 2
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set1.update(set2)
print(set1)  # Output: {'c', 'a', 'd', 'e', 'b', 'f'}

# EX 3
setl = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)  # Output: {'apple'}

# EX 4
setl = ("apple", "banana", "cherry")
set2 = ("google", "microsoft", "apple")
set1.symmetric_difference_update(set2)
print(set1)  # Output: {'google', 'banana', 'microsoft', 'cherry'}
