def safe_print_list(my_list=[], x=0):
    try:
        for index in range(0, x):
            print(my_list[index], end="")
        return (x)

    except:
        for index in range(0, len(my_list) - 1):
            print(my_list[index], end="")
        return len(my_list) - 1

