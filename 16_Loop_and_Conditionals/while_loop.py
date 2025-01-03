#Infinite loop

# n = 0
# while True:
#     n += 1
#     print(n)


# n = 0
# while True:
#     n += 1
#     print(n)
#     if n == 100:
#         break
# print("Completed")

# n = 0
# while n < 1000:
#     n += 1
#     print(n)
#  else:
#      print("Loop completed ,n=1000")

''' continue '''
# n = 0
# while n < 100:
#     n += 1
#     if n == 2:
#       continue  
#     print(n)
# else:
#     print("Loop completed ,n=1000")

''' break '''
# n = 0
# while n < 100:
#     n += 1
#     if n == 10:
#       break 
#     print(n)
# else:
#     print("Loop completed")


# n = 0
# while True:
#     try:
#         n += 1
#         if n == 100000:
#             break
#         print(n)
#     except KeyboardInterrupt:
#         print("Key board Interrupted")
#         break
# print("Script Execution completed")


while True:
    user_input = input("Enter the show command/exit:")
    if user_input == 'exit':
        break
    elif user_input.startswith('show '):
        print(f"Executing the command {user_input}")
    else:
        print("Enter a valid show command")
