def rsapper_def():
    from random import randint   
    import matplotlib.pyplot as plt
    import time

    print('(Min:6x6)')
    n = int(input('Please, set n: '))
    m = int(input('Please, set m: '))
    random_number_storage = []
    opened = []
    points = {}
    desk = []
    number_of_bombs = randint(m, round(n*m/6))
    again = 0
    integer = 1
    number = 1
    opened_numbers = []
    flag_place = 0
    flag_places = []

    def screen():
        integer = 1
        while integer <= n*m:
            if integer not in range(n,n*m,n):
                if integer in flag_places:
                    print('F ', end='')
                elif integer in opened or integer in opened_numbers:
                    print(f"{points[integer]} ", end='')
                else:
                    print('@ ', end='')
            else:
                if integer in flag_places:
                    print('F ')
                elif integer in opened or integer in opened_numbers:
                    print(f"{points[integer]} ")
                else:
                    print('@ ')
            integer += 1

    class Pos():
        def __init__(self, place):
            self.place = place
        def pos(self):
            if number_for_points == random_number + self.place and random_number + self.place not in random_number_storage:
                points[random_number + self.place] += 1

    class Cord():
        def __init__(self, place):
            self.place = place
        def pos(self):
            if points[op + self.place] == 0 and op + self.place not in opened and op + self.place not in random_number_storage:
                opened.append(op + self.place)
            if points[op +self.place] != 0:
                opened_numbers.append(op + self.place)


    right_ = Cord(1)
    left_ = Cord(- 1)
    down_ = Cord(n)
    up_ = Cord(- n)
    right_down_ = Cord((n+1))
    left_down_ = Cord((n-1))
    right_up_ = Cord(- (n-1))
    left_up_ = Cord(- (n+1))

    right = Pos(1)
    left = Pos(- 1)
    down = Pos(n)
    up = Pos(- n)
    right_down = Pos((n+1))
    left_down = Pos((n-1))
    right_up = Pos(- (n-1))
    left_up = Pos(- (n+1))

    print('TYPE 0 to set flag!')

    while number <= n*m:
        desk.append(number)
        points[number] = 0
        number += 1

    while again < number_of_bombs:
        random_number = randint(1,n*m)
        if random_number not in random_number_storage:   
            points[random_number] = 0                           
            random_number_storage.append(random_number)
            again += 1
            for number_for_points in desk:               
                if random_number in range(2,n-1):                                                                      
                    left.pos()
                    right.pos()
                    down.pos()
                    right_down.pos()
                    left_down.pos()

                elif random_number in range(n+1,n*m-(2*n-2),n):                                                        
                    right.pos()
                    up.pos()
                    down.pos()
                    right_up.pos()
                    right_down.pos()

                elif random_number in range(n*2,n*m-n+2,n):                                                             
                    left.pos()
                    up.pos()
                    down.pos()
                    left_down.pos()
                    left_up.pos()

                elif random_number in range(n*m-n+2,n*m-1):                                                           
                    left.pos()
                    right.pos()
                    up.pos()
                    right_up.pos()
                    left_up.pos()

                elif random_number == 1:     
                    right.pos()
                    down.pos()
                    right_down.pos()

                elif random_number == n:
                    left.pos()
                    down.pos()
                    left_down.pos()

                elif random_number == n*m-(n-1):
                    right.pos()
                    up.pos()
                    right_up.pos()

                elif random_number == n*m:
                    left.pos()
                    up.pos()
                    left_up.pos()

                else:
                    up.pos()
                    down.pos()
                    right.pos()
                    left.pos()
                    left_down.pos()
                    left_up.pos()
                    right_up.pos()
                    right_down.pos()
        else:             
            continue

    opened = []

    screen()


    while True:
        if sorted(random_number_storage) == sorted(flag_places):
            print('YOU WON!')
            while integer <= n*m:
                integer = 1
                if integer not in range(n,n*m,n):
                    if integer not in random_number_storage:
                        print(f"{points[integer]} ", end='')
                    else:
                        print('@ ', end='')
                else:
                    if integer not in random_number_storage:
                        print(f"{points[integer]} ")
                    else:
                        print('@ ')
            break
        choose = int(input('COORDS: '))
        if choose == 0:
            flag_place = int(input('F_COORDS: '))
            integer = 1
            if flag_place not in flag_places and flag_place not in opened and flag_place not in opened_numbers:
                flag_places.append(flag_place)
            elif flag_place in flag_places:
                flag_places.remove(flag_place)
            else:
                print('\nAlready opened, cant place flag')
            screen()
            continue
        elif choose not in opened and choose not in opened_numbers:
            if points[choose] == 0:
                opened.append(choose)
            else:
                opened_numbers.append(choose)
            if choose in random_number_storage and choose not in flag_places:
                print("YOU LOOOOSE!")
                while integer <= n*m:
                    integer = 1
                    if integer not in range(n,n*m,n):
                        if integer not in random_number_storage:
                            print(f"{points[integer]} ", end='')
                        else:
                            print('@ ', end='')
                    else:
                        if integer not in random_number_storage:
                            print(f"{points[integer]} ")
                        else:
                            print('@ ')
                break
            elif choose not in random_number_storage and choose not in flag_places:
                for op in opened:
                    if op in range(2,n-1):                                                                      
                        left_.pos()
                        right_.pos()
                        down_.pos()
                        right_down_.pos()
                        left_down_.pos()

                    elif op in range(n+1,n*m-(2*n-2),n):                                                        
                        right_.pos()
                        up_.pos()
                        down_.pos()
                        right_up_.pos()
                        right_down_.pos()

                    elif op in range(n*2,n*m-n+2,n):                                                             
                        left_.pos()
                        up_.pos()
                        down_.pos()
                        left_down_.pos()
                        left_up_.pos()

                    elif op in range(n*m-n+2,n*m-1):                                                           
                        left_.pos()
                        right_.pos()
                        up_.pos()
                        right_up_.pos()
                        left_up_.pos()

                    elif op == 1:     
                        right_.pos()
                        down_.pos()
                        right_down_.pos()

                    elif op == n:
                        left_.pos()
                        down_.pos()
                        left_down_.pos()

                    elif op == n*m-(n-1):
                        right_.pos()
                        up_.pos()
                        right_up_.pos()

                    elif op == n*m:
                        left_.pos()
                        up_.pos()
                        left_up_.pos()

                    else:
                        up_.pos()
                        down_.pos()
                        right_.pos()
                        left_.pos()
                        left_down_.pos()
                        left_up_.pos()
                        right_up_.pos()
                        right_down_.pos()
                print(opened)
                print(opened_numbers)
                print('\n')
                for f in flag_places:
                    if f in opened_numbers:
                        opened_numbers.remove(f)
                    if f in opened:
                        opened.remove(f)
                screen()
                print(flag_places)
            elif choose in flag_places:
                print('\nFlag there!')


