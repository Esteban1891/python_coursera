smallest = None # is 4
largest = None

while True:
    number = input("insert number:") # 2
    if number == 'done':
        break
    try:
        number = int(number)
        if smallest is None or smallest < number:
            smallest = number
        if largest is None or largest > number:
            largest = number
    except:
        print('insert invalidate!')
        continue

print('number largest is', largest)
print('number minimium is', smallest)
