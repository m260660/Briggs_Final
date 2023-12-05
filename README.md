The Ojective of the game is to survive as long as possible against enemy invaders. The player will spawn in the center and fend off against enemy spaceships. The player can shoot back at enemies. The player will have 5 lives

The game has 7 files. The Main_game file brings all of the files together, spawns the player and sets conditions for key presses, defines start and end of game, displays score on the top right and number of lives on the bottom left, once player is out of lives, a gameover screen appears and reveals the end score, player cannot leave thebounds of the game. 

The Player file creates a sprite which is a grey diamond shape. It contains the framework of how the player moves by using the left/right arrows to rotate and the up arrow to move forward, and spacebar to shoot. Holding down the space bar for multiple bullets can slow down the game. CAPT Severson and Jackson Winner helped configure aiming the player in the right direction by usuing radians

The Enemy file creates a sprite using the image enemy.png, a spaceship with two straight wings. The purpose of the enemy is to follow the player and shoot you down. It tracks players coordinates and follows them. It is created as a sprite group; it add_enemies sets random coordinates for an enemy sprite and inputs a number of enemies in main_game.

The Bullet file is activated by the space bar. It shoots in the instantaneous direction the player travels in upon firing. CAPT Severson helped configure firing a bullet in the same direction of the player. It disappears upon collision with borders and enemies

The Enemy Bullet file allows the Enemy to shoot bullets randomly in the direction they travel. It uses a random function to fire them unpredictably. Only enemy bullets hurt player; it uses a different .png file to decide whether a player should take damage or not
  
The Parameters file is a reference for screen height, width, player speeds, etc.

The Background file creates background using the given parameters. It uses tiles to blit a space background and a small png image and blits it across the screen

