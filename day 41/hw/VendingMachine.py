list = ["doritos", "water", "gum", "chips", " sprite"]
prices = [4.20, 1.00, 1.80, 3.30, 2.10] 

def index_num(num, user_money):
    if num > 4:
        print('Index should be less than 4')
    elif num < 0:
        print('Index should be 0 or greater')
    else:
        
        if num == 0:
            product = "doritos"
        elif num == 1:
            product = "water"
        elif num == 2:
            product = "gum"
        elif num == 3:
            product = "chips"
        elif num == 4:
            product = "sprite"  
       

      
        if user_money >= prices[num]:
            print(product)
        else:
            print('You dont have enough money to buy ' + product)

user_money = int(input('Enter the amount of money you have: '))


index = int(input('Enter index between 0 and 4: '))


index_num(index, user_money)
