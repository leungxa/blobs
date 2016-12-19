class Player:
    ATTACK_MISS = 0
    ATTACK_HIT = 1
    ATTACK_ALREADY_TAKEN = 2
    ATTACK_SUNK = 3
    ATTACK_WIN = 4
    
    def __init__(self, name, rows, cols):
        self.name = name
        self.board = Board(rows, cols)
    
    def print_board(self):
        print "========== {}'s Board ==========".format(self.name)
        self.board.bprint()
    
    def place_ships(self, ship_coords):
        self.board.place_ships(ship_coords)
        self.alive_ship_count = len(ship_coords)
    
    def attack_player(self, coord, player):
        row, col = coord[1], coord[0]
        # result = player.attack_at_coord(0, 0)
        value = player.board.get_value_at_coord(row, col)
    
        if value == Board.EMPTY_SLOT:
            player.board.set_value_at_coord(row, col, Board.ATTACK_MISS)
            return Player.ATTACK_MISS
        
        if value == Board.SHIP_SLOT:
            player.board.set_value_at_coord(row, col, Board.ATTACK_HIT)
            
            # set that ship has been hit
            ship = self.board.get_ship_from_coord(coord)
            ship.set_hit(coord)
            if ship.is_sunk():
                player.alive_ship_count -= 1
                if player.alive_ship_count == 0:
                    return Player.ATTACK_WIN
                
                # # check all other ships
                # all_sunk = True
                # for ship in self.board.ships:
                #     if not ship.is_sunk():
                #         all_sunk = False
                #         break
                # if all_sunk:
                #     return Player.ATTACK_WIN
                return Player.ATTACK_SUNK

            return Player.ATTACK_HIT
        
        if value in [Board.ATTACK_HIT, Board.ATTACK_MISS]:
            return Player.ATTACK_ALREADY_TAKEN
        
        return
    
    
class Ship:
    UNDAMAGED = 0
    DAMAGED = 1
    def __init__(self, coords):
        self.coords_status = {}
        for c in coords:
            self.coords_status[c] = Ship.UNDAMAGED

    def is_sunk(self):
        values = self.coords_status.values()
        all_damaged = True
        for v in values:
            if v == Ship.UNDAMAGED:
                all_damaged = False
                break
        return all_damaged

    def get_coords(self):
        return self.coords_status.keys()
    
    def set_hit(self, coord):
        if coord in self.coords_status:
            self.coords_status[coord] = Ship.DAMAGED
    
    
class Board:
    EMPTY_SLOT = ' '
    SHIP_SLOT = 'S'
    ATTACK_MISS = 'O'
    ATTACK_HIT = 'X'
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = []
        self.ships = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(Board.EMPTY_SLOT)
            self.board.append(row)
    
    def bprint(self):
        for row in self.board:
            print row
    
    def get_value_at_coord(self, row, col):
        return self.board[row][col]

    def set_value_at_coord(self, row, col, value):
        self.board[row][col] = value
    
    def place_ships(self, ships_coords):
        for ship_coords in ships_coords:
            s = Ship(ship_coords)
            for c in ship_coords:
                self.board[c[1]][c[0]] = Board.SHIP_SLOT
            self.ships.append(s)
    
    def get_ship_from_coord(self, coord):
        for ship in self.ships:
            if coord in ship.get_coords():
                return ship
    

ships = [[(0,1), (0,2)], [(1,3), (2,3), (3,3)]]

def main(b_rows, b_cols, p1_ships, p2_ships):
    players = []
    p1 = Player('Player1', b_rows, b_cols)
    p1.place_ships(p1_ships)
    players.append(p1)
         
    p2 = Player('Player2', b_rows, b_cols)
    p2.place_ships(p2_ships)
    players.append(p2)
    
    for p in players:
        p.print_board()
        
    p1.moves = [
        (0,0),
    ]
    
    p2.moves = [
        (0,1),
    ]
    
    while (True):
         for i in range(len(players)):
            curr_player = players[i]
            print "{}'s Turn, coords to attack:".format(curr_player.name)
            # attack_coord = input()
            if curr_player.moves:
                attack_coord = curr_player.moves.pop(0)
                opponent = players[1-i]
                result = curr_player.attack_player(attack_coord, opponent)
                opponent.print_board()
                print "Result: {}".format(result)
                if result == Player.ATTACK_WIN:
                    print "{} Wins".format(curr_player.name)
                    return
            else:
                return
    return    

# main(10, 10, ships, ships)
                
def mock_attack():
    ships = [[(0,1), (0,2)], [(1,3), (2,3), (3,3)]]
    p1 = Player('Player1', 10, 10)
    p1.place_ships(ships)
    
    p2 = Player('Player2', 10, 10)
    p2.place_ships(ships)
    
    result = p1.attack_player((0,1), p2)
    assert(result == Player.ATTACK_HIT)
    result = p1.attack_player((0,1), p2)
    assert(result == Player.ATTACK_ALREADY_TAKEN)
    result = p1.attack_player((0,0), p2)
    assert(result == Player.ATTACK_MISS)
    result = p1.attack_player((0,0), p2)
    assert(result == Player.ATTACK_ALREADY_TAKEN)
    result = p1.attack_player((0,2), p2)
    assert(result == Player.ATTACK_SUNK)
    
    for coord in [(1,3), (2,3)]:
        result = p1.attack_player(coord, p2)
        assert(result == Player.ATTACK_HIT)
    result = p1.attack_player((3,3), p2)
    assert(result == Player.ATTACK_WIN)
mock_attack()
