# bounce.py
# A rubber ball is dropped from a height of 100 meters and each time 
# it hits the ground, it bounces back up to 3/5 the height it fell. 
# Write a program bounce.py that prints a table showing the height 
# of the first 10 bounces.
# Exercise 1.5
init_height = 100
bounce = 3/5
for i in range(10):
    print(i+1, round(bounce*init_height, 4))
    init_height = bounce * init_height