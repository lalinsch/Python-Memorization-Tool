# write your code here
# define variables and functions
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')

Base = declarative_base()


class Flashcard(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    box = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


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
                    new_card = Flashcard(question=q, answer=a, box=1)
                    session.add(new_card)
                    session.commit()
                    return True


def update(card):
    print('press "d" to delete the flashcard:')
    print('press "e" to edit the flashcard:')
    a = input()
    if a == 'd':
        delete_card(card)
    elif a == 'e':
        print('current question:', card.question)
        print('please write a new question:')
        card.question = input()
        if card.question != '':
            print('current answer:', card.answer)
            print('please write a new answer:')
            new_answer = input()
            if new_answer != '':
                card.answer = new_answer
                session.commit()
    else:
        print(a, 'is not an option')


def move_card_to_next_session(card):
    current_box = card.box
    card.box = current_box + 1
    session.commit()


def move_card_to_session_one(card):
    card.box == 1
    session.commit()


def delete_card(card):
    session.delete(card)
    session.commit()


def print_learn_menu(card):
    print('press "y" if your answer is correct:')
    print('press "n" if your answer is wrong:')
    a = input()
    if a == 'y':
        if card.box == 3:
            delete_card(card)
        else:
            move_card_to_next_session(card)
    elif a == 'n':
        move_card_to_session_one(card)
    else:
        print(a, 'is not an option')


def practice():
    flashcard_list = session.query(Flashcard).all()
    if len(flashcard_list) == 0:
        print('There is no flashcard to practice!')
    else:
        for card in flashcard_list:
            print('Question: ', card.question)
            print('press "y" to see the answer:')
            print('press "n" to skip:')
            print('press "u" to update:')

            a = input()
            if a == 'y':
                print('Answer: ', card.answer)
                print_learn_menu(card)
            elif a == 'n':
                print_learn_menu(card)
                continue
            elif a == 'u':
                update(card)
            else:
                print(a, 'is not an option')


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
