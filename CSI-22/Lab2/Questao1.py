#Questao 1

def unzip(lista):
    return [list(x) for x in zip(*lista)]

print(unzip([(1, 4), (2, 5), (3, 6)]))  # Output: [(1, 2, 3), (4, 5, 6)]
print(unzip([(7, 8), (9, 10), (11, 12), (12312, 323)]))  # Output: [(7, 9, 11), (8, 10, 12)]