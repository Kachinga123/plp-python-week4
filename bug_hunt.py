count = 1
total = 0

# BUG: The while statement was missing a colon, so I added : at the end.
while count <= 5:
    # BUG: The condition was count < 5, which stopped before adding 5.
    # I changed it to count <= 5 so that 5 is included.
    total = total + count
    count = count + 1

# BUG: You cannot concatenate a string and an integer with +.
# I used a comma so Python can print both values.
print("Sum of 1 to 5 is:", total)