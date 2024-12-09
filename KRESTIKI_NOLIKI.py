def print_board(board):
    """Функция для отображения текущего состояния игрового поля."""
    print("  0 1 2")
    print("  -------")
    for i, row in enumerate(board):
        print(i, "|".join(row))
        print("  -------")


def check_winner(board):
    """Функция для проверки состояния игры."""
    # Проверяем строки и столбцы
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Проверяем диагонали
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Проверка на ничью
    if all(cell != " " for row in board for cell in row):
        return "Ничья"

    return None


def is_valid_input(user_input, board):
    """Функция для проверки корректности ввода координат пользователем."""
    if len(user_input) != 2 or not user_input.isdigit():
        return False
    row, col = map(int, user_input)
    return (0 <= row < 3) and (0 <= col < 3) and (board[row][col] == " ")


def tic_tac_toe():
    """Основная функция игры в Крестики-нолики."""
    while True:  # Новая игра в цикле
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"

        while True:
            print_board(board)
            user_input = input(f"Игрок {current_player}, введите свои координаты (строка и столбец 0, 1 или 2): ")

            if is_valid_input(user_input, board):
                row, col = map(int, user_input)
                board[row][col] = current_player

                winner = check_winner(board)
                if winner:
                    print_board(board)
                    if winner == "Ничья":
                        print("Игра завершилась ничьей!")
                    else:
                        print(f"Игрок {winner} выиграл!")
                    break

                # Смена игрока
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Некорректный ввод. Пожалуйста, попробуйте еще раз.")

        # Спрашиваем, хотят ли игроки сыграть еще раз
        again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
        if again != 'да':
            break


if __name__ == "__main__":
    tic_tac_toe()