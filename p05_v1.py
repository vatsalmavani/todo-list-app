# print('welcome to my to do list app\nwhat would you like to do?')
# print('create\tview\tupdate\tdelete')
# inp = input()

def create(string):
    with open('p05_v1.txt', 'a') as fhand:
        fhand.write(string+'\n')

# create(inp)

def view():
    with open('p05_v1.txt', 'r') as fhand:
        for line in fhand:
            print(line.strip())

# view()

# def update(tbu, new): # to be updated
#     with open('p05_v1.txt', 'r+') as fhand:
#         for line in fhand:
#             if tbu in line:
#                 line.replace(tbu, new)

# tbu = input('what needs to be updated? ')
# new = input('what should we replace it with? ')

# update(tbu, new)

def update(tbu, new):
    l = []
    with open('p05_v1.txt', 'r') as fhand:
        for line in fhand:
            line = line.strip()
            l.append(line)
    # print(l)
    del l[tbu - 1]
    # print(l)
    l.append(new)
    with open('p05_v1.txt', 'w') as fhand2:
        for line in l:
            fhand2.write(line+'\n')

# tbu = int(input('which line number needs to be updated? '))
# new = input('what do yuo want it to be updated with? ')
# update(tbu, new)

# view()

def delete(tbr): # to be removed
    l = []
    with open('p05_v1.txt', 'r') as fhand:
        for line in fhand:
            line = line.strip()
            l.append(line)
    del l[tbr - 1]
    with open('p05_v1.txt', 'w') as fhand2:
        for line in l:
            fhand2.write(line+'\n')

# tbr = int(input('which line needs to be removed? '))
# delete(tbr)

# view()

while True:
    print('what would you like to do?')
    print('create\tview\tupdate\tdelete')
    inp = input()
    if inp == 'create':
        crt = input('what do you want to add in your to do list? ')
        create(crt)
        print('added successfully')
    elif inp == 'view':
        print('here are the things you need to do:')
        view()
    elif inp == 'update':
        tbu = int(input('which line number needs to be updated? '))
        new = input('what do yuo want it to be updated with? ')
        update(tbu, new)
        print('updated successfully')
    elif inp == 'delete':
        tbr = int(input('which line needs to be removed? '))
        delete(tbr)
        print('deleted successfully')
    else:
        print('please select one:\ncreae\tview\tupdate\tdelete')
    cont = input('would you like to continue? [y/n] ')
    if cont == 'y':
        pass
    else:
        break