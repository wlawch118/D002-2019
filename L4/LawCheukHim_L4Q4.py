def checker(sentence, letter):
    result = []
    # Your code here
    for i in range(0,len(sentence)):
        if sentence[i]==letter:
            result.append(i)
    return result
print(checker("Apple", "p") )
print(checker("Banana", "p"))
print(checker("Cat", "a"))
input()
