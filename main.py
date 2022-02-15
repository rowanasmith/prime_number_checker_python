#Write your code below this line 👇

def prime_checker(number):
  prime_number = True
  for numeral in range(2, number-1):
    if (number % numeral) == 0:
      prime_number = False
  if prime_number is True:
    print(f"It's a prime number.")
  if prime_number is False:
    print(f"It's not a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



