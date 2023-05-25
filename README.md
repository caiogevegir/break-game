# break-game

Break game made on pygame.

Use the left and right arrow keys to control the board and guide the ball to destroy the bricks.
In addition, as you destroy them, the ball gets slightly faster.

<img src="https://github.com/caiogevegir/break-game/assets/56521026/9ac14d05-b19b-4e52-b498-2131344ca9b9" alt="Brek" style="height: 320px; width:240px;"/>

## Known Issues

- The game treats the paddle as an 1D object, thus the ball may get "stuck" if it collides diagonally. Since the player does not lose the ball if it collides with the upper corners, let's pretend this is a feature :)

## References

I followed this tutorial on [101Computing](https://www.101computing.net/breakout-tutorial-using-pygame-getting-started/) and made some improvements such as organization and custom assets.
