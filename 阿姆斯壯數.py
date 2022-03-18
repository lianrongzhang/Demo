number1,number2 = input().split()
number1_int = int(number1)
number2_int = int(number2)
while (number1_int < number2_int):
    total = 0
    value = 0
    for i in range(number1_int,number2_int):
        total = 0
        i_str = str(i)
        i_len = len(i_str)
        for x in i_str:
            total += int(x)**i_len
        if(total == i):
            value = 1
            print(total,end=' ')
    if value != 1:
        print("none")
    break