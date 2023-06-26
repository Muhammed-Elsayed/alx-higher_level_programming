def safe_print_list(my_list=[], x=0):
    try:
        if x > len(my_list) - 1:
            raise Exception

        for index in range(0, x):
            print(my_list[index], end="")
        print("")
        return (x)

    except:
        for index in range(0, len(my_list)):
            print(my_list[index], end="")
        print("")
        return len(my_list)

