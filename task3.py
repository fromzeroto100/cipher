import math

def paint_calc(height, width, coverage):
    number_of_cans = (height * width) / coverage
    round_up_cans = math.ceil(number_of_cans)
    print(f"You'll need {round_up_cans} cans of paint.")

    

h_wall = int(input("Enter the height: "))
w_wall = int(input("Enter the width: "))
cover = 5

# def paint_calc():
#     number_of_cans = h_wall * w_wall / coverage

paint_calc(height= h_wall, width= w_wall, coverage= cover)    