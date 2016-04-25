def merge(l):
    merged = []
    for i in range(0, len(l), 3):
        merged.append(l[i] + l[i + 1] + l[i + 2])
    return merged

print(merge([1, 2, 3, 4, 5, 6, 7, 8, 9]))
