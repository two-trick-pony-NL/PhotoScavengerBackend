#Creating objects out of the list of items
a_file = open("assignments/easy.txt", "r")
lines = a_file.read()
easy_list_of_lists = lines.splitlines()
print("Created list of EASY objects")
a_file.close()

a_file = open("assignments/medium.txt", "r")
lines = a_file.read()
medium_list_of_lists = lines.splitlines()
print("Created list of MEDIUM objects")
a_file.close()

a_file = open("assignments/hard.txt", "r")
lines = a_file.read()
hard_list_of_lists = lines.splitlines()
print("Created list of HARD objects")
a_file.close()

a_file = open("assignments/impossible.txt", "r")
lines = a_file.read()
impossible_list_of_lists = lines.splitlines()
print("Created list of IMPOSSIBLE objects")
a_file.close()


def readassignment(difficulty):

    print("Difficulty selected: " + difficulty)
    if difficulty == 'easy': 
        return easy_list_of_lists
    if difficulty == 'medium':
        return medium_list_of_lists
    if difficulty == 'hard':
        return hard_list_of_lists
    if difficulty == 'impossible':
        return impossible_list_of_lists