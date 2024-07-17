
# #solution using for loop (Time complexity : O(n))


# num = 11
# # If given number is greater than 1
# if num > 1:
#     # Iterate from 2 to n // 2
#     for i in range(2, (num//2)+1):
#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")




#without using for loop (Time complexity : O(sqrt(n)))


from math import sqrt
# n is the number to be check whether it is prime or not
n = 13

# this flag maintains status whether the n is prime or not
prime_flag = 0

if(n > 1):
    x = int(sqrt(n)) + 1
    for i in range(2, x):
        if (n % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        print("True")
    else:
        print("False")
else:
    print("False")