from random import choice
def resp(a):
    computer = choice([0,1,2])
    res = matrix[a][computer]
    print(f'computer choice is: {computer}\n\n{res}')


matrix =[['Draw','You won','you lost'],
          ['You lost','Draw','You won'],
          ['You won','You lost','Draw']
]

print(f'0- Snak \n1- Gun \n2- Water \n-1- exit')

while True:
    try:
        a = int(input("Enter your choise: "))
        if a == -1:
            break
        resp(a)
    except Exception as err:
        print(f'Invalid choice')