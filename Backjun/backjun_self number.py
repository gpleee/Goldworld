origin = set(range(1,10001))
create = set()
com = 0

def sum_digit(number):
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10)

for i in range(10000):
    com = i + sum_digit(i)
    
    create.add(com)

a=list(sorted(origin-create))

for j in range(len(a)):
    print(a[j])