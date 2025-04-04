import random


def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack

# Example Inputs and Outputs
inputs = ["({}{}{})", "()[]{}", "(]", "([{}])", "{[()]}", "([)]", "", "]"]
outputs = [isValid(i) for i in inputs]

# Displaying the results
for i, o in zip(inputs, outputs):
    print(f"Input: {i} -> Output: {o}")
for number in range(1, 2):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)

print("welcome to the password creater")


number_of_hurdle = 6
while number_of_hurdle>0:
    number_of_hurdle -= 2
    print(number_of_hurdle)


letter=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

# password_list =[]
# number_of_letter = int(input("how many letter whould u like in your password?\n"))
# number_of_symbol = int(input("how many symbol whould u like in your password?\n"))
# number_of_number = int(input("how many number whould u like in your password?\n"))

# for char in range(1, number_of_letter+1):
#     password_list.append(random.choice(letter))

# for char in range(1, number_of_symbol+1):
#     password_list.append(random.choice(symbol))

# for char in range(1, number_of_number+1):
#     password_list.append(random.choice(numbers))
# random.shuffle(password_list)
# print(password_list)    
# password=""
# for char in password_list:
#     password += char

# print(password)    

#guess the word game

print("guess the word")
print("you have ")
number_of_hurdle = 6
word="cricket"
while number_of_hurdle>0:
    number_of_letter = input("enter your letter?\n")



