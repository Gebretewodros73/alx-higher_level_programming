def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            quotient = 0
            if i < len(my_list_1):
                element_1 = my_list_1[i]
                if type(element_1) not in [int, float]:
                    print("wrong type")
                    continue
            else:
                print("out of range")
                continue
                
            if i < len(my_list_2):
                element_2 = my_list_2[i]
                if type(element_2) not in [int, float]:
                    print("wrong type")
                    continue
                elif element_2 == 0:
                    print("division by 0")
                    continue
                else:
                    quotient = element_1 / element_2
            else:
                print("out of range")
                continue
                
            new_list.append(quotient)
            
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
    
    return new_list
