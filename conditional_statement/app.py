# program designed to understand the if else statement
name=input("enter your name: ",)
age =int(input("enter the age of a person: ",))
if age >=18:
    print(f'Sir/mam you are an adult and have access to vote:{name}')
elif age<=18 and age>=10:
    print(f'Sir,you are a teenager and donot have a access for vote:{name}')
else:
    print(f'Sorry! you are a child and donnot have access to vote:{name} ')

#other approachfor the same problem  using match case statement

match age:
    case age if age >=18:
        print(f'sir/mam!you are eligible for vote:{name}')
    case age if age <=18 and age >=10:
        print(f'Sir!you are a teenager and donot eligible for vote:{name}')
    case _:
        print(f'sorry! you are not eligible for vote:{name}')