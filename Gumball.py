import random

def main():
    
    print("Welcome to Nat's Gumball Machine Simulator")
    print()
    print("You are starting with the following Gumballs: ")
    print()

    #calling function to randomly generate the amount of gumballs for each color
    gumballs = beginning_gumball()

    #calling function to randomly generate the purchase made until a red gumball is purchased
    random_purchase(gumballs)

    

def gumball_in_number():

    gumballs = []

    #randomly assign the number of gumballs for each color, putting them into a list
    for i in range(10):
        if i ==0:
            random_gumball_number = random.randint(10,15)
        elif i ==1:
            random_gumball_number = random.randint(1,10)
        elif i ==2:
            random_gumball_number = random.randint(6,15)
        elif i ==3:
            random_gumball_number = random.randint(10,25)
        elif i ==4:
            random_gumball_number = random.randint(1,12)
        elif i ==5:
            random_gumball_number = random.randint(5,10)
        elif i ==6:
            random_gumball_number = random.randint(4,6)
        elif i ==7:
            random_gumball_number = random.randint(5,12)
        elif i ==8:
            random_gumball_number = random.randint(0,10)
        else:
            random_gumball_number = 1

        gumballs.append(random_gumball_number)

    return gumballs

def beginning_gumball():
    gumballs = gumball_in_number()
    colors = ["Yellow", "Blue","White", "Green", "Black", "Purple", "Silver", "Cyan", "Magenta", "Red"]

    #printing the beginning amount of each color of gumball
    for i in range(10):
        print(gumballs[i], colors[i])
        print()

    return gumballs

def random_purchase(gumballs):
    gumball_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    colors = ["Yellow", "Blue","White", "Green", "Black", "Purple", "Silver", "Cyan", "Magenta", "Red"]

    #using a double for loop to create the total array of gumballs in each color(represented by numerical values) as specified by their amount
    total_gumballs = []
    index = 0

    for i in range (10):
        for gumball in range(gumballs[index]):
        
            total_gumballs.append(str(i+1))

        index += 1

        #makes sure the max number of gumballs is 113 (creating an array/list of 113 positions)
        if len(total_gumballs) >=113:
            break 


    #creating lists to put randomly generated gumballs
    generated_gumballs = []
    selected_gumballs = [] 

    total = 0

    keepgoing = True

    #using a for loop to randomly select gumballs(by their assignmed numerical values) in the array of gumballs created above, until the red gumball is selected
    while keepgoing == True:

        selection = random.randint(0, len(total_gumballs)-1)

        gumball = total_gumballs[selection]

        if gumball == "10":
            selected_gumballs.append(gumball)
            total += 1
            keepgoing = False

        elif gumball == "99":
            continue

        else:
            generated_gumballs.append(gumball)
            total_gumballs[selection] = "99"
            total += 1
            selected_gumballs.append(gumball)
           
        


    print("Here are your random purchases:")
    print()

    #using a for loop to print out the color of the gumballs randomly selected 
    for i in range(len(selected_gumballs)):
        number= int(selected_gumballs[i]) -1
        color = colors[number]
        print(color)
        print()

    #creating another list to count the frequency of each individual color of gumballs selected
    freq = []
    
    for gumball in selected_gumballs:
        freq.append(selected_gumballs.count(gumball))

    
    maximum = int(max(freq))

    #putting the maximum gumball color purchsed into a list
    frequency=[]

    for i in range(len(freq)):
        
        number= int(selected_gumballs[i]) -1 
        color = colors[number]

        if freq[i] == maximum and color not in frequency:
            frequency.append(color)
        elif maximum == 1:
            continue


    print("You purchsed "+ str(total)+ " gumballs, for a total of $"+str(total*.25)+ ".")
    print()
    print("The color(s) purchased most:")

    for color in frequency:
        print(color,  end=" ")
        


    
main()

