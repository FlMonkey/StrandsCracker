import manipulate
puzzle = [
    ['S', 'C', 'E', 'E', 'B', 'T'],
    ['K', 'H', 'R', 'S', 'E', 'S'],
    ['N', 'A', 'N', 'I', 'G', 'A'],
    ['H', 'G', 'N', 'R', 'E', 'R'],
    ['T', 'I', 'G', 'O', 'S', 'D'],
    ['S', 'A', 'I', 'S', 'F', 'F'],
    ['W', 'L', 'N', 'C', 'R', 'Y'],
    ['A', 'Y', 'S', 'E', 'E', 'L']
]
puzzleStr = []

for i in puzzle:
    for letter in i:
        puzzleStr.append(letter)



def makeset():
    def check_sublist(word, main_list):
        # Create a copy of the main_list to manipulate
        word = word.upper()
        sublist = []
        for letter in word:
            sublist.append(letter)

        temp_list = main_list.copy()

        try:
            # Try to remove each element in sublist from temp_list
            for item in sublist:
                temp_list.remove(item)
            # If all elements are removed successfully, return True
            return True
        except ValueError:
            # If an element in sublist is not found in temp_list, return False
            return False



    # Read the words from the file
    with open('WordList.txt', 'r') as file:
        words = file.readlines()
    global filtered_words
    # Filter the words based on the defined criteria
    filtered_words = [word for word in words if check_sublist(word.strip(),puzzleStr)]

    # Write the filtered words back to a new file or the same file
    with open('WordListSet.txt', 'w') as file:
        file.writelines(filtered_words)


def checkNeighbors(x,y,c,w):
    if len(w) == c:
        return w
    if puzzle[x+1][y] == w[c]:
        c += 1
        checkNeighbors(x+1,y,c,w)
    if puzzle[x+1][y+1] == w[c]:
        c += 1
        checkNeighbors(x+1,y,c,w)
    if puzzle[x+1][y-1] == w[c]:
        c += 1
        checkNeighbors(x+1,y,c,w)
    if puzzle[x][y+1] == w[c]:
        c += 1
        checkNeighbors(x+1,y,c,w)
    if puzzle[x-1][y+1] == w[c]:
        c += 1
        checkNeighbors(x+1,y,c,w)
    if puzzle[x+1][y+1] == w[c]:
        c += 1
        checkNeighbors(x+1,y,c,w)
    if puzzle[x-1][y-1] == w[c]:
        c += 1
        checkNeighbors(x+1,y,c,w)
    if puzzle[x-1][y] == w[c]:
        c += 1
        checkNeighbors(x+1,y,c,w)
    if puzzle[x][y-1] == w[c]:
        c += 1
        checkNeighbors(x+1,y,c,w)
    else:
        return False




    pass
def checkword():
    #with open('WordListSet.txt', 'w') as file:
    #    words = file.readlines()

    words = filtered_words

    validWordList = []
    for word in words:
        j = 0
        i = 0
        for i in range(0,len(puzzle)):
            for j in range(0,len(puzzle[0])):
                if word[0] == puzzle[i][j]:
                    try:
                        validWordList.append(checkNeighbors(i,j,0,word))
                    except:
                        pass
    with open('validWordList.txt', 'w') as file:
        file.writelines(validWordList)

makeset()
checkword()