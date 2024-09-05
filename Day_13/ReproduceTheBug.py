from random import randint

# this code sometimes gives errors
dice_images = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(1, 6) # the issue is that it can sometimes grab the number 6. dice_images[6] is out of the bounds of the list. It should be randint(0, 5)
print(dice_images[dice_num])