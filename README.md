# alien-invasion-pygame
This is a project developed with Pygame intending to create a simple 2D videogame. The name of the videogame is alien invasion. It is based on the first hands-on project in "Python Crash Course" book by Eric Matthes. The core of my code follows the lines of code shown in the book, however, my main contributions to this project are: (1) create an option to pause and to continue playing, (2) add a help button that shows the instructions by pressing it, (3) allow the spaceship to move vertically besides moving only horizontally, (4) show an explosion visualization every time the spaceship crashes with an alien or an alien reaches the earth, (5) allow the videogame to record the high-score, (6) show "GAME OVER" in the screen when losing the current game, and (7) change some of the original rules to make it more entertaining and dynamic for the user.

This repository contains ten py files, one txt file, and one folder with three images. 

The ten py files are:
1. "alien_invasion.py" - It is the main file of the videogame, as the main loop for the game is here.
2. "game_functions" - It contains all the requiered functions to play this 2D videogame such as move the spaceship, fire bullets, pause the game, continue playing, and others.
3. "help_button.py" - It contains the Help_Button class with all its attributes and methods to create a button.
4. "play_button.py" - It contains the Play_Button class with all its attributes and methods to create a button.
5. "alien.py" - It contains the Alien class with all its attributes and methods.
6. "bullet.py" - It contains the Bullet class with all its attributes and methods.
7. "ship.py" - It contains the Ship class with all its attributes and methods.
8. "scoreboard.py" - It contains the Scoreboard class with all its attributes and methods to visualize a simple but dynamic scoreboard while playing.
9. "game_stats.py" - It contains the GameStats class with all its attributes and methods to keep track of the basic statistics of the game such as level, current score, high-score, and number of available spaceships. 
10. "settings.py" - It contains the Settings class with all the attributes to specify the screen, alien, bullet, ship, and general settings. Besides, it contains the methods to initialize the dynamic settings and change them while advancing to harder levels.

The only txt file is:
1. "ai_high_score.txt" - This file records only the high-score and every time it is beaten, it is updated.

The only folder is "images" and it has three images:
1. alien.bmp - This image was extracted from <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
2. ship.bmp - This image is available in the book's resources through https://www.nostarch.com/pythoncrashcourse/. 
3. boom.png - This image is a modified version of the original one that was extracted from https://elements.envato.com/.
