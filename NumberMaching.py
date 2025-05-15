def number_to_string(num):
    match num:
        case 1:
            return "one"
        case 2:
            return "Two"
        case 3 :
            return "Three"
        case _:
            return "Unknown number"
        
print(number_to_string(2))        
print(number_to_string(5))