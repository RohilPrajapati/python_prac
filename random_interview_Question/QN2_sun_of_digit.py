"""
2. Write a function that takes in a number and performs the sum of its digits until a single digit remains.
Example: 8993 should return 2
8993 => 8+9+9+3 = 29
29 => 2+9 = 11
11 => 1+1 = 2
2
"""
# my Solution
# def sum_of_digit(num):
#     num_str = str(num)
#     number = list(num_str)
#     sum = 0
#     for n in number:
#         sum += int(n)
#     if sum//10 == 0:
#         return sum 
#     else:
#         return sum_of_digit(sum)
    
# solution from chatgpt
def sum_of_digit(num):
    if num < 10:
        return num
    return sum_of_digit(sum(int(d) for d in str(num)))

"""Improvements Made:
- Removed unnecessary variable assignments like num_str, number, and sum = 0.
- Used generator expression: sum(int(d) for d in str(num)).
- Directly check if num < 10: instead of sum // 10 == 0 — more readable and efficient.
"""

if __name__ == '__main__':
    num = 8993
    result = sum_of_digit(num)
    print(result)