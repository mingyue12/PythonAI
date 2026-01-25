
for row in range(1, 10):
    for col in range(1, row + 1):
        print("%d * %d = %d" % (col, row, col * row), end="\t")
    print()
