def get_item(item):
    if item == 'id':
        line = 0
        char = 11
    elif item =='key':
        line = 1
        char = 8
    elif item == 'path':
        line = 2
        char = 5
    load_profile = open('notes.txt', "r")
    read_it = load_profile.read().splitlines()[line]
    read_it = read_it[char:]
    return read_it