import random 
def auto_guess(secret):
    attempts = 0 
    guess = 0 
    while guess != secret:
        guess =random.randint(1,100)
        attempts  = attempts + 1 
        print(f'Trying:{guess}')
    print(f'Found it ! The number was {secret}')
    print (f'It took{attempts} attempts:')
secret = random.randint(1,100)
print(f'Secret number is :{secret}')
auto_guess(secret)