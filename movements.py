"""Creates the actual logic and valid movements of the tiles. Utilizing matrixs
to keep track of the specific tile and the number asscoiated with that tile."""

import random
import constants as c


def new_game(n):
    """Create the game(main) matrix that stores the other matrixs."""
    matrix = []
    for i in range(n):
        matrix.append([0] * n)

    matrix = add_two(matrix)
    matrix = add_two(matrix)
    return matrix


def add_two(mat):
    """Place a random number within the range into an empty tile"""
    a = random.randint(0, len(mat) - 1)
    b = random.randint(0, len(mat) - 1)
    while mat[a][b] != 0:
        a = random.randint(0, len(mat) - 1)
        b = random.randint(0, len(mat) - 1)
    mat[a][b] = 2
    return mat

def game_state(mat):
    """Checks the state of the game, whether the user has lost, won, or if there
        are possible moves that can still be made."""
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == '2048':
                return 'win'

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'

    for i in range(len(mat) - 1):
        for j in range(len(mat[0]) - 1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'not over'
    for k in range(len(mat) - 1):
        if mat[len(mat) - 1][k] == mat[len(mat) - 1][k + 1]:
            return 'not over'
    for j in range(len(mat) - 1):
        if mat[j][len(mat) - 1] == mat[j + 1][len(mat) - 1]:
            return 'not over'
    return 'lose'


def reverse(mat):
    """Return a reversed version of the tile's original placement
        ,will be used later on."""
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0])-j-1])
    return new


def flip(mat):
    """Return a matrix in which the order of the tiles is changed where a matrix
    of horizontal tiles is fliped so that it becomes vertical and is placed
    in its respective place. This can also be one inversely from vertical
    to horizontal as well."""
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new


def cover_up(mat):
    """Given the gameboard, it returns a new matrix in which the non-zero tiles
    in each matrix is moved to the left and space unoccupied is converted into
    an empty tile(0)."""
    new = []
    for j in range(c.grid_len):
        partial_new = []
        for i in range(c.grid_len):
            partial_new.append(0)
        new.append(partial_new)
    done = False
    for i in range(c.grid_len):
        count = 0
        for j in range(c.grid_len):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return new, done


def merge(mat, done):
    """Given the gameboard as an argument, it merges the tiles inside the matrix
    that have the same value."""
    for i in range(c.grid_len):
        for j in range(c.grid_len - 1):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j + 1] = 0
                done = True
    return mat, done


def moveUp(game):
    print("up")
    game = flip(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = flip(game)
    return game, done


def moveDown(game):
    print("down")
    game = reverse(flip(game))
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = flip(reverse(game))
    return game, done


def moveLeft(game):
    print("left")
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    return game, done


def moveRight(game):
    print("right")
    game = reverse(game)
    game, done = cover_up(game)
    game, done = merge(game, done)
    game = cover_up(game)[0]
    game = reverse(game)
    return game, done
            
                          
                        
        
