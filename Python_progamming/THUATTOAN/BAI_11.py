number = int(input('Nhập một số: '))
for num in range(2, number):
    is_prime = True
    i = 2
    while i * i <= num:
        if num%i==0:
            is_prime = False
            break
        i += 1
    if is_prime == True:
        print(num,end=" ")


    
# class Prime:
#     def __init__(self):
#         # This can store prime numbers if we want to reuse them
#         self.primes = []

#     def tim_so_nguyen_to(self, number):
#         # This function will find all prime numbers smaller than 'number'
#         ket_qua = []  # result list

#         for num in range(2, number):  # start from 2, because 0 and 1 are not prime
#             la_so_nguyen_to = True

#             # Check if num is divisible by any number from 2 to sqrt(num)
#             for i in range(2, int(num ** 0.5) + 1):
#                 if num % i == 0:
#                     la_so_nguyen_to = False
#                     break

#             if la_so_nguyen_to:
#                 ket_qua.append(num)

#         self.primes = ket_qua  # save result in the object
#         return ket_qua


# # Example usage
# p = Prime()
# print(p.tim_so_nguyen_to(10))  # Output: [2, 3, 5, 7]
