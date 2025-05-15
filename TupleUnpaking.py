point = (0,5)
match point:
    case (0,0):
        print("Origin")
    case (0,y):
        print(f"Y-axis at {y}")
    case (x,0):
        print(f"x-axis at {x}")
    case (x,y):
        print(f"point at ({x},{y})")
    case _: 
        print("Not a point")                