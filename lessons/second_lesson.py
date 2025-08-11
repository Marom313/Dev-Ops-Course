# -------------------------------------------- Excersize - List, Tuple, Set --------------------------------------------
# python Basics

def secondLesson():
    new_lst = [(i + 1) ** 2 for i in range(10)]
    print(new_lst)
    lst = ['apple', 'banana', 'cherry']
    A = lst[0][0]
    B = lst[1][0]
    C = lst[2][0]
    print(A, B, C)
    lst2 = [1, 2, 3, 4, 5]
    print(lst2)
    lst2Squared = [i ** 2 for i in lst2]
    print(lst2Squared)
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    print(nums)
    nums2 = [i for i in nums if i % 2 == 0]
    print(nums2)
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print(list1, list2)
    print(list1 + list2)
    strings = ['foo', 'bar', 'baz']
    print(strings)
    stringA = [s for s in strings if 'a' in s]
    print(len(stringA))
    print(stringA)
    numss = [1, 2, 3, 4]
    print(numss)
    numsZ = [n * 10 for n in numss]
    print(numsZ)
    stringss = ['', 'foo', '', 'bar', 'baz']
    print(stringss)
    stringsNotEmpty = [s for s in stringss if s]
    print(stringsNotEmpty)

# -------------------------------------------- The End --------------------------------------------
