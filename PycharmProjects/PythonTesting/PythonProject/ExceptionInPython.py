ItemsInCart = 0

# if ItemsInCart != 2:
#     raise Exception("Product cart are not matching")
#     pass

# assert (ItemsInCart == 2)

# Try catch mechanismmmm
try:
    with open('filke.txt', 'r') as reader:
        reader.read()

except:
    print("Congrats barath, There is an error in your code.")


# We are priniting the error of python instead of our customized print statement.
try:
    with open('filke.txt', 'r') as reader:
        reader.read()

except Exception as B:
    print(B)

finally:
    print("Cleaned up the cookies")





