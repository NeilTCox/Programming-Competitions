#initiate variables
preferences = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
one_coords = ()

#construct preferences list
for i in range(1, 10):
    y = get_number()-1
    x = get_number()-1
    preferences[y][x] = i
    #get coordinate of 1st move
    if i==1:
        one_coords = (y, x)

# OLD IMPLEMENTATION
# #calculate list of lowest sum
# def lowest_sum():
#     #return row as list
#     def get_row():
#         return preferences[one_coords[0]]

#     #return column as list
#     def get_column():
#         column_list = []
#         for i in range(0, 3):
#             column_list.append(preferences[i][one_coords[1]])
#         return column_list

#     #return left diagonal as list
#     def get_left_diagonal():
#         left_diagonal_list = [preferences[0][0], preferences[1][1], preferences[2][2]]


#     #return right diagonal as list
#     def get_right_diagonal():
#         right_diagonal_list = [preferences[0][2], preferences[1][1], preferences[2][0]]

#     #determine winning lists
#     winning_lists = []

#     #middle
#     if one_coords == (1,1):
#         winning_lists.append(get_row())
#         winning_lists.append(get_column())
#         winning_lists.append(get_left_diagonal())
#         winning_lists.append(get_right_diagonal())
#     #top left or bottom right
#     elif one_coords == (0,0) or one_coords == (2,2):
#         winning_lists.append(get_row())
#         winning_lists.append(get_column())
#         winning_lists.append(get_left_diagonal())
#     #top right or bottom left
#     elif one_coords == (0,2) or one_coords == (2,0):
#         winning_lists.append(get_row())
#         winning_lists.append(get_column())
#         winning_lists.append(get_right_diagonal())
#     #elsewhere (diamond)
#     else:
#         winning_lists.append(get_row())
#         winning_lists.append(get_column())

#     #create sum list
#     sum_list = []
#     for item in winning_lists:
#         sum_list.append(sum(item))

#     return winning_lists[sum_list.index(min(sum_list))]


# all solutions list
def all_solutions():
    all_solutions = []
    all_solutions.append(preferences[0])
    all_solutions.append(preferences[1])
    all_solutions.append(preferences[2])
    first_column = []
    for i in range(0, 3):
        first_column.append(preferences[i][0])
    all_solutions.append(first_column)
    second_column = []
    for i in range(0, 3):
        second_column.append(preferences[i][1])
    all_solutions.append(second_column)
    third_column = []
    for i in range(0, 3):
        third_column.append(preferences[i][2])
    all_solutions.append(third_column)
    all_solutions.append([preferences[0][0], preferences[1][1], preferences[2][2]])
    all_solutions.append([preferences[0][2], preferences[1][1], preferences[2][0]])
    return all_solutions

def


#test prints
for thing in preferences:
    print(thing)
print(one_coords)
print(all_solutions())
