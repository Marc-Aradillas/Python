# Marc Anthony Aradillas

# Sample function showing the goal of the game and move commands
def show_instructions():
    # print a main menu and the commands
    print("Zombie Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the Zombie.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


# Define the items dictionary
items = {
    'Flash Light': {'name': 'Flash Light'},
    'Flare': {'name': 'Flare'}
}

# Define the rooms dictionary
rooms = {
    'Supply Room': {'name': 'The Supply Room', 'south': 'Council Room', 'east': 'Storage Room',
                    'item': 'Flash Light', 'text': 'you are in the Supply Room'},

    'Council Room': {'name': 'The Council Room', 'north': 'Supply Room', 'south': 'Locker Room',
                     'east': 'Radio Room', 'west': 'Fire Pit', 'text': 'you are in the Council Room'},

    'Radio Room': {'name': 'The Radio Room', 'west': 'Council Room', 'north': 'Armory',
                   'item': 'Flare', 'text': 'you are in the Radio Room'},

    'Armory': {'name': 'The Armory', 'south': 'Radio Room', 'text': 'you are in the Armory'},

    'Fire Pit': {'name': 'The Fire Pit', 'east': 'Council Room',
                 'text': 'you are at the Fire Pit'},

    'Locker Room': {'name': 'The Locker Room', 'north': 'Council Room', 'east': 'Tent',
                    'text': 'you are in the Locker Room'},

    'Tent': {'name': 'The Tent', 'west': 'Locker Room',
             'text': 'you are in the Tent'},

    'Storage Room': {'name': 'The Storage Room', 'west': 'Supply Room',
                     'text': 'you are in the Storage Room'}
}

# Define the list of valid directions
directions = ['north', 'south', 'east', 'west']

# Initialize the current room and inventory
current_room = rooms['Council Room']
inventory = []

# Game loop
while True:
    # Check if the player has won the game
    if current_room['name'] == 'The Storage Room' and len(inventory) == 2:
        print('Congratulations! You have reached the Storage Room and collected all items!')
        break

    # Print the current room and prompt the user for input
    print(current_room['text'])
    command = input('\nWhat do you do? ').strip().lower()

    # Parse the input and execute the corresponding action
    if command in directions:
        # If the input is a valid direction, check if there is a room in that direction
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            print('You cannot go that way.')
    elif command.startswith('get '):
        # If the input starts with "get ", try to pick up the specified item
        item_name = command[4:]
        if 'item' in current_room and current_room['item'] == item_name:
            # If the item is in the room, pick it up and add it to the inventory
            inventory.append(items[item_name])
            current_room.pop('item')
            print(f"You picked up the {item_name}.")
        else:
            print("That item is not here.")
    elif command == 'inventory':
        # Print the contents of the inventory
        if len(inventory) == 0:
            print("Your inventory is empty.")
        else:
            print("Inventory:")
            for item in inventory:
                print(item['name'])
    elif command == 'help':
        # Show the game instructions
        show_instructions()
    else:
        # If the input is not recognized, print an error message
        print('Command not recognized.')
