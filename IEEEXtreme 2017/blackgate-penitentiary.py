#implementation
crew = []
count = get_number()

while count>0:
    crew.append((get_word(), get_number()))
    count-=1

crew_sorted = sorted(crew, key = lambda t: (t[1], t[0]))

current_height = crew_sorted[0][1]
start_index = 1
end_index = 1
crew_members = crew_sorted[0][0] + ' '
for item in crew_sorted[1:]:
    if current_height != item[1]:
        current_height = item[1]
        print(crew_members + str(start_index) + " " + str(end_index))
        end_index += 1
        start_index = end_index
        crew_members = item[0] + ' '
    else:
        crew_members += item[0] + ' '
        end_index += 1
print(crew_members + str(start_index) + " " + str(end_index))
