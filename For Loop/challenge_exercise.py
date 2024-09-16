number  = [1,1,1,1,6]
# for x in number:
#     print('x'*x)

for x in number:
    output = ''
    for y in range(x):
        output +='x'
    print(output)