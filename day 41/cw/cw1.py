list = ["hair ","study", "food", "redd", "phone"]

def index_num(num):
    if num > 3:
     print('index should be less than 4')
     if num < -4:
        print('index should be more than -4')
    if num <= 3:
       print(list[num])

       
index = int(input('enter index between 0 and 3: '))


index_num(index)