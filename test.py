# # statement_1 if expression else statement_2


# a = 2
# b = 5
# max = a if a > b else b
# print(max)


# while умова:
#     блок циклу


# count  = 1
# while count <=5:
#     print(count)
#     count +=1


# a = ""
# while True:
#     print ('Please enter string [q - quit]')
#     value = input()
#     if value == 'q':
#         break
#     print:('123545')
# print('ok')



a = True
while a:
    name = input('please enter name:')
    if name != 'Ivan':
        continue
    print('Hello Ivan, how old are u?')
    age = input('age:')
    if int(age) == 18:
        break
print('OK')