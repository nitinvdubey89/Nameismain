a = 9
b = int(input('Enter b '))
# b = str(b)

del b # another unspecified error

try:
    c = a/b
except ZeroDivisionError as e:
    print('Division by 0 is not allowed! Exception raised:', e)
except TypeError as e: # e is a temp variabel
    print('a and b must be numbers . Exception raised:', e)
except Exception as e: ## best prpactise is specify the name of the exception each time
    print('Another unspecified error.Exception raised:', e)
else:
    print('No error')
    print(f'C={c}')
#finally block is used in releasing external resources such as files or network connecitons , regardless of the use of the resources 


print('other part of the code still runs')