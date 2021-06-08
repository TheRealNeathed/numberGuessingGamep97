import random 

x = random.randint(1,9)


z = 0
while z < 5:
    y = int(input("Guess 1-9"))
    if x == y:
        z = z + 1
        print("You guessed it! It took " +str(z)+" tries!")
    else:
        z = z + 1
        print("You missed it! This was your" +str(z)+ " try.")
        if x > y:
            print("Your guess was too low!")
        else:
            print("Your guess was too high!")

if z == 6:
    print("You lose!")
    
