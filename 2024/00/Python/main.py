def unlock_terminal(initial_state: str, moves: str) -> int:
    shift: int = 0
    state = list(map(int, list(initial_state)))
    for m in moves:
        if m == "U":
            # No need to readjust shift due to Python allowing negative indexing
            # Other languages would just use shift % len(moves) to readjust it
            state[shift] = (state[shift] + 1) % 10
        elif m == "D":
            state[shift] = (state[shift] - 1) % 10
        elif m == "L":
            shift -= 1
        elif m == "R":
            shift += 1
    return int("".join([str(i) for i in state]))


start_pos = "528934712834"
moves = "URDURUDRUDLLLLUUDDUDUDUDLLRRRR"

res = unlock_terminal(start_pos, moves)
print(res)
