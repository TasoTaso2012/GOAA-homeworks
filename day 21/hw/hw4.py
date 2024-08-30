products=['kitkat','oreo','sprite','water','chips',
          'doritos','gum','twix','m&m','pepsi']

print('''available products:kitkat,oreo,sprite,water,
      chips,doritos,gum,twix,m&m,pepsi''')

user_input=int(input('enter product code'))

user_choice=products[user_input-1]

print('you received ' + user_choice)

                