#Juego de los palitos con MiniMax "sticks"
import random

def sticks(stick):
    for i in range(stick):
        print("|", end="")
    print()

def successors_generator (stick):
    successors = []
    for i in range(1, min(stick, 4)):
        successors.append(stick - i)
    return successors

def MiniMax(stick, depth, is_maximizing_player):
    if depth == 0 or stick == 0:
        return 0
    
    if is_maximizing_player:
        max_eval = -float('inf')
        for successor in successors_generator(stick):
            eval = MiniMax(successor, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    
    else:
        min_eval = float('inf')
        for successor in successors_generator(stick):
            eval = MiniMax(successor, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval


def get_best_move(stick):
    best_eval = -float('inf')
    best_move = 0
    for i in range(1, min(stick, 4)):
        eval = MiniMax(stick - i, 15, False)
        if eval > best_eval:
            best_eval = eval
            best_move = i
    return best_move


stick = 25

sticks(stick)

while stick > 0:

    # Turno de la maquina (aleatorio)
    palos_ia = random.randint(1, 3)
    palos_ia = min(palos_ia, stick)
    print(f"La IA quita {palos_ia} palos.")
    stick -= palos_ia
    sticks(stick)
    if stick == 0:
        print("MiniMax win")
        break

    # Turno de Minimax
    
    drop = get_best_move(stick)
    print(f"MiniMax quita {drop} palos.")
    stick -= drop
    sticks(stick)
    if stick == 0:
        print("Maquina aleatoria win(no deberia ganar)")
        break
