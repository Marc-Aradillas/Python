# Marc Anthony Aradillas

# A dictionary linking a room to other rooms
# linking one item for each room except the Start room (Council Room) and the room containing the villain

rooms = {
    'The Council Room': {'north': 'Supply Room', 'south': 'Locker Room',
                         'east': 'Radio Room', 'west': 'Fire Pit'},

    'The Radio Room': {'west': 'Council Room', 'item': 'Flare',
                       'north': 'Armory', 'text': 'you are in the Radio Room'},

    'The Supply Room': {'south': 'Council Room', 'east': 'Storage Room',
                        'item': 'Flash Light', 'text': 'you are in the Supply Room'},

    'The Armory': {'south': 'Radio Room', 'item': 'Riot Shield',
                   'text': 'you are in the Armory'},

    'The Fire Pit': {'east': 'Council Room', 'item': 'Grilled Corn',
                     'text': 'you are at the Fire Pit'},

    'The Locker Room': {'north': 'Council Room', 'east': 'Tent',
                        'item': 'Baseball Bat', 'text': 'you are in the Locker Room'},

    'The Tent': {'west': 'Locker Room', 'item': 'Four Leaf Clover',
                 'text': 'you are in the Tent'},

    'The Storage Room': {'west': 'Supply Room', 'item': 'Zombie',
                         'text': 'you are in the Storage Room'}  # villain
}

# print a main menu and the comma
def show_instructions():
    print('-' * 20)
    print("Zombie Text Adventure Game\n"
          "Collect 6 items to win the game, or be eaten by the Zombie.\n"
          "Move commands: go south, go north, go east, go west\n"
          "Add to Inventory: get 'item name'\n")
    print('-' * 20)


# assign inventory to empty list and current room to Council Room

inventory = []
current_room = 'The Council Room'
current_item = ''
player_move = ['north', 'south', 'east', 'west']


def show_status():
    print('You are in', current_room)
    print('Gathered Items:', inventory)
    print("-" * 20)


def show_travel():
    print('you have traveled to', current_room)
    print('Gathered Items:', inventory)
    print("-" * 20)


def main():
    pass


show_instructions()

show_status()

# gameplay loop / while loop

while True:

    # get move from player
    
    command = input('\nWhat do you do? ').split()
    print('-' * 20)

    room = current_room

    # while statement if go is true
    
    if command[0] == 'go':
    
        # assign direction to second half of move
        
        direction = (command[1]).capitalize()
        
        # if statement to determine if direction is in room dictionary
        
        if direction in rooms[current_room]:
        
            # assign new room to value in dictionary
            
            room = rooms[room][(player_move[1]).capitalize()]
            
            # show current room & item
            
            show_travel()

            if 'item' not in rooms[room]:
                pass
            else:
                # print item if not collected yet
                print('You see', rooms[room]['item'])
                print('-' * 20)

            if room == 'The Storage Room':
                # winning statement
                if len(inventory) == 7:
                    print('Congratulations! you have reached the Storage Room and eliminated the Zombie!')
                    exit()

                # losing statement
                elif len(inventory) != 7:
                    print('You have not gathered enough items!'
                          '\nThe Zombie bit you. bye bye!')
                    exit()

            player_move = input('\nWhat do you do? ').split()
            print('-' * 20)

        else:
            print('You cannot travel this way!')
            print('-' * 20)
            player_move = input('\nWhich direction are you trying to go? ').split()
            print('-' * 20)

    elif player_move[0] == 'get':
        # assign item name to second half of move
        item_name = (player_move[1]).capitalize()

        # if statement to determine if item name is in room dictionary
        if item_name in rooms[room]['item']:
            # add item name to inventory
            inventory.append(item_name)
            del rooms[room]['item']
            print('Great! you gathered', item_name)
            print('-' * 20)
            player_move = input('\nWhat do you do? ').split()
            print('-' * 20)
        else:
            print('Please enter a valid command.')
            player_move = input('\nWhat do you do? ').split()
            print('-' * 20)

    else:
        print('Please enter a valid command.')
        player_move = input('\nWhat do you do? ').split()
        print('-' * 20)

main()