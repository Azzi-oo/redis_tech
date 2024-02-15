tumb = ["apple", "pen", "book"]

# for i in tumb:
#     print(i)

it = iter(tumb)

try:
    while True:
        next_val = next(it)
        print("Znach:", next_val)
except StopIteration:
    print('Iteration stop')
print('Program end')
