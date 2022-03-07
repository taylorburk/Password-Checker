import random
import string

Num = int(input('How long would you like your password to be? (Passwords are recommened to have at least 8 characters) '))

if Num <= 5:
  password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = Num))
  print('your new password is weak')
else:
  password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k = Num))
  print('your new password is strong')
 
  
# print result
print("Your generated random password is : " + str(password))



