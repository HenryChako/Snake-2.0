
# Snake Game Report

## Introduction

The goal of this coursework was to create engaging game using Python. The chosen application for this project is a classic game known as "Snake". 

To run the program, navigate to the directory containing the `game.py` file in a terminal and type `python game.py`. 

To play the game, use the arrow keys to control the direction of the snake. The objective is to eat the food (red square) which causes the snake to grow in length. The game ends when the snake collides with itself or the window boundary.


## Body/Analysis

### Object-Oriented Programming (OOP) Pillars

The program implements all four pillars of OOP: Polymorphism, Abstraction, Inheritance, and Encapsulation.

1. **Polymorphism**: This is the ability of an object to take on many forms. The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class object. In the game, polymorphism is used in the `change_direction` method of the `Game` class. The method behaves differently depending on the key pressed by the user.

```python
def change_direction(self, e): #e = event
    if (e.keysym == "Up" and self.snake.velocityY != 1):
        self.snake.velocityX = 0
        self.snake.velocityY = -1
    elif (e.keysym == "Down" and self.snake.velocityY != -1):
        ...
```

2. **Abstraction**: This is a mechanism to hide the complex implementation details and only show the functionality to the users. In the game, the `Game` class provides an abstraction for the game logic. The user doesn't need to know how the game is drawn or how the snake moves. They just need to know how to control the snake.

3. **Inheritance**: This is the process by which one class takes on the attributes and methods of another. The game uses inheritance in the `Object`, `Snake`, and `Game` classes. For example, the `Snake` class inherits from the `Object` class.

```python
class Snake(Object):  # Snake inherits from Object
    def __init__(self, x, y):
        super().__init__(x, y)
        self.head = Tile(x, y)
        self.velocityX = 0
        self.velocityY = 0
```

4. **Encapsulation**: This is the practice of keeping fields within a class private, then providing access to them via public methods. It’s a protective barrier that keeps the data and code safe from outside interference. In the game, the `Snake` and `Game` classes use encapsulation. The data members of these classes are not accessible directly. They are accessed through the methods of their respective classes.

### Design Patterns

The game uses two design patterns: Singleton and Factory Method.

1. **Singleton**: This pattern restricts the instantiation of a class to a single instance and provides a global point of access to it. The `Game` class uses the Singleton pattern to ensure that only one game instance exists throughout the application.

```python
class Game(Object):  # Game inherits from Object
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Game, cls).__new__(cls)
        return cls._instance
```

2. **Factory Method**: This pattern provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. In the game, the `Tile` class acts as a simple factory to create `Tile` objects.

```python
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

### Reading from File & Writing to File

The game reads and writes to a text file to keep track of the high score across sessions. The `get_high_score` method reads the high score from the file, and the `save_high_score` method writes the new high score to the file.

```python
def get_high_score(self):
    try:
        with open('high_score.txt', 'r') as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

def save_high_score(self, score):
    with open('high_score.txt', 'w') as f:
        f.write(str(score))
```

### Testing

The core functionality of the game is covered with unit tests. The `TestSnakeMethods` and `TestGameMethods` classes in the `test_game.py` file test the initialization and reset functionality of the `Snake` and `Game` classes, respectively.

```python
class TestSnakeMethods(unittest.TestCase):
    def setUp(self):
        self.snake = Snake(5, 5)

    def test_init(self):
        self.assertEqual(self.snake.head.x, 5)
        self.assertEqual(self.snake.head.y, 5)
        self.assertEqual(self.snake.velocityX, 0)
        self.assertEqual(self.snake.velocityY, 0)
```

## Results

- The game successfully implements the classic Snake game in a simple and intuitive manner.
- The game keeps track of the player's score and high score, providing a sense of progression and achievement.
- The game's code follows the principles of Object-Oriented Programming (OOP), making it modular and easy to understand and modify.

## Conclusions

This project successfully achieved its goal of creating a simple and engaging game using Python. The resulting Snake game provides an enjoyable and challenging experience for players, and its high score feature adds replayability. 

In the future, the game could be extended in several ways, such as adding different levels of difficulty, introducing new types of food that affect the snake in different ways, or adding multiplayer AI functionality.
