if __name__=="__main__":
    string_lines = []
    list_lines = []
    transposed = [[]]

    # construct list
    with open('Matrix-Transpose_InputForSubmission_1.txt') as f:
      for line in open('Matrix-Transpose_InputForSubmission_1.txt'):
          string_lines.append(line.rstrip('\n'))

    for line in string_lines:
        list_lines.append([int(i) for i in line.split()])

    #transpose

    transposed = [list(x) for x in zip(*list_lines)]

    #convert to string
    finished = ""
    for line in transposed:
        finished += (" ".join(str(x) for x in line)+"\n")

    print(finished)
