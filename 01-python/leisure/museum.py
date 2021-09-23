def draw_museum():
    
    # Ceiling
    print(33*"_")

    for i in range(10):
        if i == 4:
            # Walls + Sign
            print("|", 3*" ", "| El Museo del Prada |",2*" ", "|")
        elif i==8 or i==9:
            # Walls + Door frame
            print("|", 12*" ", "| |",12*" ", "|")
        elif i == 7:
            # Walls + Top of Door
            print("|", 12*" ", "___",12*" ", "|")
        else:
            # Rest of walls
            print("|", 29*" ", "|")

    # Floor
    print(33*"-")



    return