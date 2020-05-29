command = ' '   # records what the user has typed in
started = False   # records whether the car has started

while True:   # While loop is running
    command = input('> ').lower()   # converts all letters into lower case
    if command == 'start':   # If the user types in the input 'start'
        if started:  # if started == True
            print('Car is already started!')
        else:
            started = True   # set started to True so the user does't start the car again
            print('Car started...')
    elif command == 'stop':  # If the user types in the statements 'stop'
        if not started:   # If started == False
            print('Car is already stopped!')
        else:
            started = False  # set started to false so the user cannot stop the car again
            print('Car stopped.')
    elif command == 'help':   # if the user types in the statement 'help'
        print('''
start - to start the car
stop - to stop the car
quit - to quit the game
''')
    elif command == 'quit':   # If the user typed in the statement 'quit'
        break   # exits the while loop
    else:   # If user does not type in any of the input statements above
        print('Sorry! I did not understand that!')


