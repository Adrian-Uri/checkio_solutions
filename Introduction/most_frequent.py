def most_frequent(data: list[str]) -> str:
    diccionario = {}
    for a in data:
        try:
            diccionario[a] += 1
        except:
            diccionario[a] = 1

    return max(diccionario,key=diccionario.get)


print("Example:")
print(most_frequent(["a", "b", "c", "a", "b", "a"]))

# These "asserts" are used for self-checking
assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"
assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
