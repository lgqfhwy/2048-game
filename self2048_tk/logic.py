from random import *

def new_game(n):
    matrix = []
    for i in range(n):
        matrix.append([0] * n)
    return matrix

def add_two(mat):
    a = randint(0, len(mat) - 1)
    b = randint(0, len(mat) - 1)
    while mat[a][b] != 0:
        a = randint(0, len(mat) - 1)
        b = randint(0, len(mat) - 1)
    mat[a][b] = 2
    return mat

def game_state(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 2048:
                return 'win'
    for i in range(len(mat) - 1):
        for j in range(len(mat[0]) - 1):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return 'not over'

    for i in range(len(mat)):   # check for any zero entries
        for j in range(len(mat)):
            if mat[i][j] == 0:
                return 'not over'

    for i in range(len(mat) - 1):
        if mat[len(mat) - 1][i] == mat[len(mat) - 1][i + 1]:
            return 'not over'

    for j in range(len(mat) - 1):
        if mat[j][len(mat) - 1] == mat[j + 1][len(mat) - 1]:
            return 'not over'
    return 'lose'

def reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0]) - j - 1])
    return new

def transpose(mat):
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new

# The way to do movement is compress -> merge -> compress again
# Basically if they can solve one side, and use transpose and reverse correctly they should
# be able to solve the entire thing just by flipping the matrix around

def cover_up(mat):
    new = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    done = False
    for i in range(len(mat)):
        count = 0
        for j in range(len(mat[i])):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return (new, done)

def merge(mat):
    done = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                done = True
    return (mat, done)

def left(game):
    print("left")
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    return (game, done)

def right(game):
    print('right')
    game, done = left(reverse(game))
    return (reverse(game), done)

def up(game):
    print('up')
    game, done = left(transpose(game))
    return (transpose(game), done)

def down(game):
    print('down')
    game, done = right(transpose(game))
    return (transpose(game), done)

#print(new_game(4))