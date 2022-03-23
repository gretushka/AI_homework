print('Nice to meet you. My name is Nastya')
name = input('And what is your name?')
print(f"I'm so glad yo see you, {name}!")
age = int(input('How old are you?'))
my_age = 32
if age > my_age:
    print('You are older than me')
elif age < my_age:
    print('You are younger than me')
else:
    print(f"We are peers, I'm {age} too")
