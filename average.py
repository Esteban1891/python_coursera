List = []
while True:
    try:
        data = input("insert number to average:")
        if data == 'exit':
            break
        value_data = float(data)
        List.append(value_data)
        average = sum(List) / len(List)
        print("the average is:", average)
    except:
        print("error you used in number type integer")

