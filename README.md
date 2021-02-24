# Design and Analysis of Software Systems  
## Assignment 2 - Terminal Breakout in Python  
### Made by 
* Aashwin Vaish  
* 2019114014  


## Description  
This is a terminal-based recreation of the popular game Breakout, with gameplay inspiration from DX-Ball. The project is made entirely with Python3, and uses only the modules from the Python Standard Library.  

The game is programmed using Object Oriented Programming approaches.  

**Note**: The project is only set to run only Linux systems.  
**Note**: The colors in the game are affected by the colors set in your terminal emulator.  
**Note**: **Set the terminal emulator to a minimum window size of 120 x 45 (cols x rows).**  
  
## Starting the game  
```
python3 main.py  
```  
## Controls  

**\<a\>, \<d\>** : Move Paddle (Tap them once to nudge the paddle).  
**\<Space\>**: Release grabbed balls.  
**\<x\> or \<q\>**: Quit game. Always use these so that the terminal can return to its default settings.  

## Rules  
The rules are simple, you have a ball and a paddle, try and hit as many bricks as possible and create a high score!

* If a ball misses the paddle and falls out the bottom, its gone from the board.
* If there are no balls on the board, you lose a life.
* Some bricks require multiple hits to take down, the warmer the color, the stronger the brick. (Red >> Blue)
* Some bricks (Cyan) are unbreakable, while some are explosives (Magenta), which will explode their neighbouring blocks, causing them to lose strength or break.
* Powerups are of two categories which are indicated by their icons, green are favourable, while red are not (but in some situations you might find even some red powerups useful!)

## Powerups
Everytime a brick is broken, there is a 1/6 chance that it will spawn a powerup. They have to be picked up using your paddle, and are active for a limited time.

* **Expand Paddle (<>, ➕)**: Extends your paddle by 10 units.
* **Shrink Paddle (><, ➖)**: Shrinks the paddle by 5 units.
* **Ball Multiplier (x2, x2)**: Doubles the number of balls currently on the board.
* **Fast Ball (>>, ⏩)**: Speeds up all the balls on the board.
* **Thru Ball (->, 🔴)**: Supercharges the balls so that they can break all the bricks in one hit, even the previously unbreakable ones.
* **Paddle Grab (╚╝,🧲)**: The paddle becomes magnetised to grab all the balls that land on it. Once grabbed, the balls can be released by pressing \<Space\>.

## Class Stucture

```
├── Entity  --  Base class for all things drawable and movable
│   ├── Ball  --  Ball class
│   ├── Brick  --  Common Brick class
│   ├── Paddle  --  Paddle Class
│   └── Powerup  --  Base class for all powerups, provides interface to 'start()', 'execute()' and 'end()'
│       ├── Expand    ─┐
│       ├── Grab       │
│       ├── Multiply   ├───  As described above, each powerup supplies its own behaviour and appearance.
│       ├── Shrink     │
│       ├── SpeedUp    │
│       └── ThruBall  ─┘
├── BrickHandler  --  Class to manage the bricks on the board, using a grid system.
├── Game  --  Game Logic implemented in 'start()' 'update()' 'render()' 'over()' methods.
├── HUD  --  A HUD to display score, lives and active powerups.
├── Globals  --  Contain global values for Board size, Colors, Brick Strength, Powerup IDs etc
├── InputHandler  --  Handles the input to the program.
└── Vector2  --  2D vector (x,y) with operator overloading to fit the game engine.
```

## Pro Tips
* Multiple powerups can be active at a time! So rack up Expands while avoiding Shrinks.
* Deflection of ball is based on where it hits the paddle.
* Your paddle is only slightly faster than the fastest speed the ball can go. So prioritise following it rather than waiting for powerups.
* Mutiplying balls divides the momentum and can be used to permanently slow down the balls.