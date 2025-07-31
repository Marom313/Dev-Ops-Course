def list_tuple_set():
    print(
        "-------------------------------------------- Excersize - List, Tuple, Set --------------------------------------------")
    A = ['apple', 'banana', 'cherry']
    A.append('date')
    print(len(A))
    A.remove('apple')
    print("remove", A)
    A.sort()  # Sort alphabetical order
    print("sort", A)
    B = {3, 1, 4, 1, 5, 9}
    print(B.__contains__(7))
    C = ('dog', 'cat', 'fish')
    print(C[2])
    print(C[1])
    print("Convert")
    print(C)
    C = list(C)
    print(C)
    D = [[10, 20], [30, 40]]
    print(D[1][1])


def dictionary():
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

    def freq(words):

        word_frequency = {}
        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
        print(word_frequency)

    def finds():
        A = {"X": 1, "Y": 2, "Z": 3}
        B = {"X": 3, "Y": 2, "Z": 6}

        common_words = {}
        for var in A:
            print(var)
            if var in B and A[var] == B[var]:
                common_words[var] = A[var]
        print(common_words)

    def sums():
        A = {"X": 1, "Y": 2, "Z": 3, "T": 4, "I": 5, "J": 6, "K": 7}

        values = []
        for var in A:
            value = A[var]
            print(value)
            if isinstance(value, int):
                values.append(value)
                print(values)
            else:
                pass
        return sum(values)

    def sorts(dic):
        sorted_keys = sorted(dic, key=dic.get, reverse=True)  # True -> from the large to the small
        return sorted_keys

    def sorts_dics(dics):
        for dic in dics:
            sorted_keys = sorted(dics, key=dic.get)
            print(sorted_keys)

        return sorted_keys

    freq(words)
    finds()
    print(sums())
    B = {"X": 1, "Y": 1, "Z": 1, "T": 1, "I": 1, "J": 1, "K": 1}
    print(sorts(B))
    lst = [[{"X": 15, "Y": 2, "Z": 13, "T": 4, "I": 25, "J": 66, "K": 7}],
           [{"X": 15, "Y": 2, "Z": 1, "T": 4, "I": 5, "J": 6, "K": 7}],
           [{"X": 1, "Y": 1, "Z": 1, "T": 1, "I": 1, "J": 1, "K": 1}]]
    dic2 = {{"name": "Bob", "age": 60}, {"name": "Alice", "age": 18}, {"name": "John", "age": 20}}
    sorts_dics(dic2)

    print(
        "-------------------------------------------- The End -----------------------------------------------------------------")
