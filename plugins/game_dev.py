import discord

def plugin_ready(client):
    main_client = client
    print(f'Plugins loaded.')


def plugin_on_message(message, author):
    if str(message) == "!plugins":
        response = f"Plugins are loaded."
        return response

    if str(message) == "!help":
        response = f"""These are the supported commands:\n
!contact - Details of a contactable developer\n
!help - Displays this list\n
!updates - Current project details\n
"""
        return response

    if str(message) == "!play":
        game = TicTacToe(author)
        response = f"{game.board}\nWould you like to go first or second?"
        return response

class TicTacToe:

    def __init__(self, author):
        player = author
        game_start = True
        cells = setup_cells(self)
        board = draw_board(self, cells)
        
    def setup_cells(self):
        cells = {"A1": "0", "A2": "0", "A3": "0",
                "B1": "0", "B2": "0", "B3": "0",
                "C1": "0", "C2": "0", "C3": "0"}
        return cells

    def draw_board(self):
        board = f""".     1    2    3
    - - - - - - - -
    A  | {cells[0][0]} | {cells[0][1]} | {cells[0][2]} |
    B  | {cells[1][0]} | {cells[1][1]} | {cells[1][2]} |
    C  | {cells[2][0]} | {cells[2][1]} | {cells[2][2]} |
    - - - - - - - -"""
        return board

    def wait_for_user_response(self):
        pass

    def ai_response(self):
        pass

    def stop_game(self):
        game_start = False
