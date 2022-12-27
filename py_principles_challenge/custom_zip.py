def zap(a, b):
    return [(a[i], b[i]) for i in range(len(a))]

    
# def zap(a, b):
#     zipped = []
#     for i in range(len(a)):
#         zipped.append((a[i], b[i]))
#     return zipped

print(zap(
    [0, 1, 2, 3],
    [5, 6, 7, 8]
))