# # numebers = [1, 2, 13, 21, 11, 22, 154, 23, 124, 6, 19, 24]
# # for num in enumerate(numebers):
# #     if num<=21:
# #         print(num)
        

# age= int(input("what is your age?\n"))

# def life_in_weeks(years):
#     remaining_years= 90 - years
#     remaining_weeks= 52 * remaining_years
#     print(f"You have {remaining_weeks} weeks left.")
    
    
    
# life_in_weeks(age) 


# def calculate_love_score(name1, name2):
# coin_list = list(map(int, input("Enter coin: ").split()))
# coin_list.sort(reverse=True)
# print(coin_list)
# rupee= int(input("enter any random number\n"))
# coin_count= 0


# for num in coin_list:
#     if(rupee>=num):
#         coin_count+= int(rupee/num)
#         rupee= rupee%num

# print(coin_count)    
        



# print(arr)
# 
# This is the scoring criteria: 

# - Scores 91 - 100: Grade = "Outstanding" 

# - Scores 81 - 90: Grade = "Exceeds Expectations" 

# - Scores 71 - 80: Grade = "Acceptable" 

# - Scores 70 or lower: Grade = "Fail"

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = student_scores

# for grade in student_scores:
#     if(student_scores[grade]<=70):
#         student_grades[grade]= "Fail"
#     elif(student_scores[grade]<=80 and student_scores[grade]>=71):
#         student_grades[grade]= "Acceptable"
#     elif(student_scores[grade]<=90 and student_scores[grade]>=81):
#         student_grades[grade]= "Exceeds Expectations"
#     elif(student_scores[grade]<=100 and student_scores[grade]>=91):
#         student_grades[grade]= "Outstanding"

# print(student_grades)


#lets create a calcultor

# first_value= int(input("enter the first value: "))
# operation= input("+\n-\n*\n/\npick an operation: ")
# second_value= int(input("enter the second value: "))
# answer= (first_value)(operation)(second_value)
# print(answer)




# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.


numbers = [1, 2, 3, 2, 4, 1, 5]  # example input
same_num = 0
remaining_numbers = []

for num in numbers:
    count = numbers.count(num)
    if count > 1:
        same_num += 1
    if num not in remaining_numbers:
        remaining_numbers.append(num) 
                                            