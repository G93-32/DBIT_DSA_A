def count_characters(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

text = "data structures and algorithms"
result = count_characters(text)

for char, count in sorted(result.items()):
    print(f"'{char}': {count}")