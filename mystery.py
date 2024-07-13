import json
import os
import random
import pickle

class MysteryGame:
    def __init__(self):
        self.mystery = None
        self.current_clue = 0
        self.solution_revealed = False
        self.twist_revealed = False

    def load_mystery(self):
        mysteries_dir = "mysteries"
        mystery_files = [f for f in os.listdir(mysteries_dir) if f.endswith('.json')]
        if not mystery_files:
            print("No mystery files found in the 'mysteries' directory.")
            return False

        chosen_file = random.choice(mystery_files)
        with open(os.path.join(mysteries_dir, chosen_file), 'r') as file:
            self.mystery = json.load(file)
        return True

    def give_clue(self):
        if self.current_clue < len(self.mystery.get('clues', [])):
            clue = self.mystery['clues'][self.current_clue]
            print(f"Clue #{clue.get('id', self.current_clue + 1)}:")
            print(clue.get('description', 'No description provided.'))
            if 'location' in clue:
                print(f"Location: {clue['location']}")
            self.current_clue += 1
        else:
            print("There are no more clues.")

    def reveal_solution(self):
        if not self.solution_revealed:
            print(f"Solution: {self.mystery.get('solution', 'No solution provided.')}")
            self.solution_revealed = True
        else:
            print("The solution has already been revealed.")

    def reveal_twist(self):
        if not self.twist_revealed:
            twist = self.mystery.get('plotTwist', {})
            print(f"Plot Twist: {twist.get('description', 'No plot twist provided.')}")
            if 'revealTrigger' in twist:
                print(f"Reveal Trigger: {twist['revealTrigger']}")
            self.twist_revealed = True
        else:
            print("The plot twist has already been revealed.")

def save_state(game):
    with open('game_state.pkl', 'wb') as f:
        pickle.dump(game, f)

def load_state():
    if os.path.exists('game_state.pkl'):
        with open('game_state.pkl', 'rb') as f:
            return pickle.load(f)
    return None

def delete_state():
    if os.path.exists('game_state.pkl'):
        os.remove('game_state.pkl')
        print("Game state has been reset.")
    else:
        print("No saved game state found.")

def main():
    game = load_state()
    if game is None:
        game = MysteryGame()
        if not game.load_mystery():
            return

    print(f"Welcome to the mystery: {game.mystery.get('misdeed', 'Undefined Mystery')}")

    while True:
        command = input("Enter a command (clue/solution/twist/reset/quit): ").lower()
        
        if command == 'clue':
            game.give_clue()
        elif command == 'solution':
            game.reveal_solution()
        elif command == 'twist':
            game.reveal_twist()
        elif command == 'reset':
            delete_state()
            game = MysteryGame()
            if not game.load_mystery():
                return
            print(f"New mystery loaded: {game.mystery.get('misdeed', 'Undefined Mystery')}")
        elif command == 'quit':
            print("May all your rolls be 20!")
            break
        else:
            print("Invalid command. Please try again.")

        if command != 'reset':
            save_state(game)

if __name__ == "__main__":
    main()