# for i in range(100):
#     if i % 3 == 0:
#         print('fizz', end='')
#     if i % 4 == 0:
#         print('gozz', end='')
#     if i % 5 == 0:
#         print('buzz', end='')
#     if not(i % 3 == 0 or  i % 4 == 0 or i % 5 == 0):
#         print(i, end='')
#     print('')

for i in range(1, int(input("How high should I go?\n"))): print("Fizz"*(not i%3) + "Gozz"*(not i%4) + "Buzz"*(not i%5) + str(i)*bool(i%3 and i%4 and i%5))