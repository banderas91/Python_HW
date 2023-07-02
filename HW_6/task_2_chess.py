import chess

safe_positions = chess.find_safe_positions()
for i, positions in enumerate(safe_positions):
    print(f"Расстановка {i + 1}:")
    for position in positions:
        print(position)
