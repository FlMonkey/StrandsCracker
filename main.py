
puzzle = [
    ['E', 'R', 'M', 'F', 'A', 'N'],
    ['V', 'I', 'E', 'A', 'K', 'T'],
    ['E', 'M', 'G', 'F', 'E', 'A'],
    ['R', 'E', 'I', 'B', 'N', 'S'],
    ['T', 'N', 'E', 'O', 'Y', 'S'],
    ['A', 'M', 'L', 'I', 'I', 'U'],
    ['E', 'Y', 'E', 'V', 'I', 'L'],
    ['R', 'D', 'A', 'D', 'E', 'L']
]

puzzleStr = []
used = []
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


def checkNeighbors(x, y, c, w, used):
    if c >= len(w):
        return True

    directions = [(1, 0), (1, 1), (1, -1), (0, 1), (-1, 1), (-1, -1), (-1, 0), (0, -1)]
    for dx, dy in directions:
        newX, newY = x + dx, y + dy
        # Check boundaries and if the new position is not already used
        if 0 <= newX < len(puzzle) and 0 <= newY < len(puzzle[0]) and (newX, newY) not in used:
            if puzzle[newX][newY] == w[c]:
                used.append((newX, newY))
                if checkNeighbors(newX, newY, c + 1, w, used):
                    return True
                used.pop()  # Backtrack if not a valid path

    return False


def checkword():
    words = filtered_words
    validWordList = []

    for word in words:
        word = word.strip().upper()
        for i in range(len(puzzle)):
            for j in range(len(puzzle[0])):
                if word[0] == puzzle[i][j]:
                    used = [(i, j)]
                    if checkNeighbors(i, j, 1, word, used):
                        validWordList.append(word + '\n')
                        break  # Exit the loop once a valid placement is found

    with open('validWordList.txt', 'w') as file:
        file.writelines(validWordList)

makeset()
checkword()