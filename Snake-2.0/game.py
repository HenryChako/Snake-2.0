import tkinter
import random
import os

# Set up constants for the game
ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Object(Tile):  # Object inherits from Tile
    def __init__(self, x, y):
        super().__init__(x, y)
        self.body = []

class Snake(Object):  # Snake inherits from Object
    def __init__(self, x, y):
        super().__init__(x, y)
        self.head = Tile(x, y)
        self.velocityX = 0
        self.velocityY = 0

class Game(Object):  # Game inherits from Object
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Game, cls).__new__(cls)
        return cls._instance

    def __init__(self, window, canvas):
        super().__init__(0, 0)  # x and y are not used in Game, so we can set them to 0
        self.window = window
        self.canvas = canvas
        self.snake = Snake(TILE_SIZE * 5, TILE_SIZE * 5)  # Initialize snake here
        self.food = Tile(TILE_SIZE * 10, TILE_SIZE * 10)
        self.game_over = False
        self.score = 0
        self.high_score = self.get_high_score()  # Load the high score at the start of the game

    def reset_game(self):
        self.snake = Snake(TILE_SIZE * 5, TILE_SIZE * 5)  # Reset snake here
        self.food = Tile(TILE_SIZE * 10, TILE_SIZE * 10)
        self.snake.velocityX = 0
        self.snake.velocityY = 0
        self.snake.body = []
        self.game_over = False
        self.score = 0

    def change_direction(self, e): #e = event
        if (self.game_over):
            if (e.keysym == 'r'):
                self.reset_game()
                self.draw()  # Start the game loop again
            return

        if (e.keysym == "Up" and self.snake.velocityY != 1):
            self.snake.velocityX = 0
            self.snake.velocityY = -1
            
        elif (e.keysym == "Down" and self.snake.velocityY != -1):
            self.snake.velocityX = 0
            self.snake.velocityY = 1

        elif (e.keysym == "Left" and self.snake.velocityX != 1):
            self.snake.velocityX = -1
            self.snake.velocityY = 0

        elif (e.keysym == "Right" and self.snake.velocityX != -1):
            self.snake.velocityX = 1
            self.snake.velocityY = 0

    def move(self):
        if (self.game_over):
            return
        
        if (self.snake.head.x < 0 or self.snake.head.x >= WINDOW_WIDTH or self.snake.head.y < 0 or self.snake.head.y >= WINDOW_HEIGHT):
            self.game_over = True
            return
        
        for tile in self.snake.body:
            if (self.snake.head.x == tile.x and self.snake.head.y == tile.y):
                self.game_over = True
                return
        
        #Collision
        if (self.snake.head.x == self.food.x and self.snake.head.y == self.food.y): 
            self.snake.body.append(Tile(self.food.x, self.food.y))
            self.food.x = random.randint(0, COLS-1) * TILE_SIZE
            self.food.y = random.randint(0, ROWS-1) * TILE_SIZE
            self.score += 1
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score(self.high_score)  # Save the new high score

        #Update snake body
        for i in range(len(self.snake.body)-1, -1, -1):
            tile = self.snake.body[i]
            if (i == 0):
                tile.x = self.snake.head.x
                tile.y = self.snake.head.y
            else:
                prev_tile = self.snake.body[i-1]
                tile.x = prev_tile.x
                tile.y = prev_tile.y
        
        self.snake.head.x += self.snake.velocityX * TILE_SIZE
        self.snake.head.y += self.snake.velocityY * TILE_SIZE
        
    def draw(self):
        self.canvas.delete("all")  # Clear the canvas
        if self.game_over:
            # Game over text
            self.canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, font = "Arial 20", text = f"Game Over: {self.score}", fill = "white")
            self.canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 30, font = "Arial 20", text = "Press 'r' to restart", fill = "white")
            self.canvas.create_text(WINDOW_WIDTH - 70, 20, font = "Arial 10", text = f"High Score: {self.high_score}", fill = "white")  # Display the high score
        else:
            self.move()
            # Drawing food
            self.canvas.create_rectangle(self.food.x, self.food.y, self.food.x + TILE_SIZE, self.food.y + TILE_SIZE, fill = 'red')
            # Drawing snake head
            self.canvas.create_rectangle(self.snake.head.x, self.snake.head.y, self.snake.head.x + TILE_SIZE, self.snake.head.y + TILE_SIZE, fill = 'lime green')
            # Drawing snake body
            for tile in self.snake.body:
                self.canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill = 'lime green')
            # Displaying score and high score
            self.canvas.create_text(30, 20, font = "Arial 10", text = f"Score: {self.score}", fill = "white")
            self.canvas.create_text(WINDOW_WIDTH - 70, 20, font = "Arial 10", text = f"High Score: {self.high_score}", fill = "white")
            self.window.after(100, self.draw)  # Schedule next draw

    def get_high_score(self):
        try:
            with open('high_score.txt', 'r') as f:
                return int(f.read())
        except FileNotFoundError:
            return 0

    def save_high_score(self, score):
        with open('high_score.txt', 'w') as f:
            f.write(str(score))

# Initialize game
snake = Snake(TILE_SIZE * 5, TILE_SIZE * 5)
food = Tile(TILE_SIZE * 10, TILE_SIZE * 10)

# Game window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()

# Center the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

# Format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

game = Game(window, canvas)
game.draw()
window.bind("<KeyRelease>", game.change_direction)  # Bind key release event to change_direction
window.mainloop()  # Start the game loop
