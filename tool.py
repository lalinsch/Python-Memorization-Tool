# write your code here
# define variables and functions
flashcard_dict = {}


def print_menu():
    print('1. Add flashcards')
    print('2. Practice flashcards')
    print('3. Exit')


def add():
    while True:
        print('1. Add a new flashcard')
        print('2. Exit')
        com = input()
        if com == '1':
            while add_new_card():
                break
        elif com == '2':
            break
        else:
            print(com, 'is not an option')


def add_new_card():
    while True:
        print('Question:')
        q = input()
        if q == '':
            continue
        else:
            while True:
                print('Answer:')
                a = input()
                if a == '':
                    continue
                else:
                    flashcard_dict[q] = a
                    return True
    else:
        return False


def practice():
    if len(flashcard_dict) == 0:
        print('There is no flashcard to practice!')
    else:
        for card in flashcard_dict:
            print('Question: ', card)
            print('Please press "y" to see the answer or press "n" to skip:')
            a = input()
            if a == 'y':
                print('Answer: ', flashcard_dict[card])
            else:
                continue

# Start of program


while True:
    print_menu()
    c = input()
    if c == '1':
        add()
    elif c == '2':
        practice()
    elif c == '3':
        print('Bye!')
        break
    else:
        print(c, 'is not an option')
