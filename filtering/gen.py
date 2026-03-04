def function():
    counter = 0
    while counter <= 10:
        yield counter
        counter = counter + 1
print(list(function()))