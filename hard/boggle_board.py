class Board:
    def __init__(self, board):
        self.board = board
        
    @property
    def row_count(self):
        return len(self.board)
        
    @property
    def column_count(self):
        return len(self.board[0])
        
    @property
    def is_empty(self):
        if not self.board or not self.board[0]:
            return True
        return False
        
    def valid_coordinates(self, coordinates):
        if coordinates.row < 0:
            return False
        if coordinates.column < 0:
            return False
        if coordinates.row >= self.row_count:
            return False
        if coordinates.column >= self.column_count:
            return False
        return True
        
    def get_letter_at(self, coordinates):
        return self.board[coordinates.row][coordinates.column]

    def get_empty_board(self):
        return [[False for letter in range(self.column_count)] for row in range(self.row_count)]
        

class TrieNode:
    END_SYMBOL = ''
    def __init__(self):
        self.root = {}
        
    def add_word(self, word):
        current_node = self.root
        for letter in word:
            if not letter in current_node:
                current_node[letter] = {}
            current_node = current_node[letter]
        current_node[self.END_SYMBOL] = word


class Coordinates:
    def __init__(self, row, column):
        self.row = row
        self.column = column


def boggleBoard(board, words):
    found_words = set()
    board = Board(board)
    if board.is_empty:
        return found_words
    visited = board.get_empty_board()
    
    trie = TrieNode()
    for word in words:
        trie.add_word(word)
    
    coordinates = Coordinates(0, 0)
    for row_index in range(board.row_count):
        coordinates.row = row_index
        for column_index in range(board.column_count):
            coordinates.column = column_index
            visit_coordinates(board, coordinates, trie.root, visited, found_words)
    return found_words

def visit_coordinates(board, coordinates, trie, visited, found_words):
    if not board.valid_coordinates(coordinates):
        return
    if visited[coordinates.row][coordinates.column]:
        return

    current_letter = board.get_letter_at(coordinates)
    if not current_letter in trie:
        # no chance of reaching a needed word at this point
        return
    trie = trie[current_letter]
    if TrieNode.END_SYMBOL in trie:
        found_words.add(trie[TrieNode.END_SYMBOL])
    
    visited[coordinates.row][coordinates.column] = True
    for neighbour in get_neighbours(coordinates):
        visit_coordinates(board, neighbour, trie, visited, found_words)
    # don't let current state spill to other depth first searches
    visited[coordinates.row][coordinates.column] = False

def get_neighbours(coordinates):
    neighbours = []
    for row in range(-1, 2):
        for column in range(-1, 2):
            if not row and not column:
                continue
            neighbour_coordinates = Coordinates(coordinates.row + row, coordinates.column + column)
            neighbours.append(neighbour_coordinates)
    return neighbours
