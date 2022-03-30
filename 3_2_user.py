def user(name, surname, year, city, email, phone):
    return (f'{name} {surname}, {year} year of birth, city: {city}, email: {email}, phone number: {phone}')


name = input('Please, input your name ')
surname = input('Now surname ')
year = input('Year of your birth ')
city = input('Where are you from? ')
email = input('Your email ')
phone = input("And your phone number. It's the last question, really=) ")

print(user(name=name, surname=surname, email=email, phone=phone, year=year, city=city))
