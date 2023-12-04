The Ojective of the game is to survive as long as possible against enemy invaders

  -The player will spawn in the center and fend off against enemy spaceships
  -The player can shoot back at enemies
  -The player will have 5 lives

The game has 7 files
 -Main_game
    -Brings all of the files together
    -Spawns the player and sets conditions for key presses
    -Defines start and end of game
    -Displays score on the top right and number of lives on the bottom left
    -Once player is out of lives, a gameover screen appears and reveals the end score
    -Player cannot leave the bounds of the game
  -Player
    -Sprite is a grey diamond shape
    -Contains the framework of how the player moves
    -Uses arrow keys
    -Up to move forward
    -Left/Right to rotate
    -Space to shoot
      -Hold down the space bar for multiple bullets; can slow down the game
    -CAPT Severson and Jackson Winner helped configure aiming the player in the
    right direction by usuing radians
  -Enemy
    -Sprite is enemy.png, a spaceship with two straight wings
    -Goal is to follow the player and shoot you down
    -Tracks players coordinates and follows them
    -Created as a sprite group
      -add_enemies sets random coordinates for an enemy sprite 
        -inputs a number of enemies in main_game
  -Bullet
    -Activated by the space bar
    -Shoots in the instantaneous direction the player travels in upon firing
      -CAPT Severson helped configure firing a bullet in the same direction of the player
    -Disappears upon collision with borders and enemies
  -Enemy Bullet
    -Enemy shoots bullets randomly in the direction they travel
    -Uses a random function to fire them unpredictably
    -Only enemy bullets hurt player
    -Uses a different .png file to decide whether a player should take damage or not
  Parameters
    -Reference for screen height, width, player speeds, etc.
  -Background
    -Creates background using the given parameters
    -Uses tiles to blit a space background
    -Uses a small png image and blits it across the screen

