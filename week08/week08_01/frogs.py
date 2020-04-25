def create_frog_board(num_frogs):
    return '>' * (num_frogs // 2) + '_' + '<' * (num_frogs // 2)


def list_to_string(list):
    return ''.join(list)


def create_nodes(board):
    nodes = list()
    pos_of_space = board.index('_')
    swamp = list(board)
    for i in range(-2, 3):
        if i != 0:
            if (pos_of_space - i) < len(swamp) and (pos_of_space - i) >= 0:
                if i < 0:
                    if swamp[pos_of_space - i] == '<':
                        swamp[pos_of_space], swamp[pos_of_space - i] = swamp[pos_of_space - i], swamp[pos_of_space]
                if i > 0:
                    if swamp[pos_of_space - i] == '>':
                        swamp[pos_of_space], swamp[pos_of_space - i] = swamp[pos_of_space - i], swamp[pos_of_space]
                nodes.append(list_to_string(swamp))
                swamp = list(board)

    return nodes


def play_game(board, final_state, path=[]):
    cur_path = path + [board]

    if board == final_state:
        return cur_path

    moves = create_nodes(board)

    for node in moves:
        if node not in cur_path:
            new_path = play_game(node, final_state, cur_path)
            if new_path:
                return new_path

    return None


def main():
    num_frogs = int(input('Number of frogs:'))
    board = create_frog_board(num_frogs)
    final = board[::-1]
    for moves in play_game(board, final):
        print(moves)


if __name__ == '__main__':
    main()
