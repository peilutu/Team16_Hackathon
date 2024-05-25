# Breakout Challenge

Your goal is to create a playable version of the Wozniak's classic game Breakout.

Here's a playable version:
- https://www.crazygames.com/game/atari-breakout

Here's a sweet easter egg alternative:
- https://elgoog.im/breakout/

Because this is a large goal for a flash hackathon, we'll help you decompose the problem into a series of increasingly complex features:

1. Create the blocks
1. Create the paddle, making it move with arrow keys. (look into pygame.key)
    - https://www.pygame.org/docs/ref/key.html
1. Create the ball, getting it to bounce off of the walls.
1. Check for a collision and change block color, no reflection or destruction yet. (investigate pygame.Rect methods)
    - https://www.pygame.org/docs/ref/rect.html
1. Handle the ball's reflection on collision, against both paddle and blocks.
1. Handle losing and winning.

## Bonus Features:

- Multiple lives
- Sounds
- "Edges" of the paddle
- Acceleration to increase the challenge
- High Score tracking
- Power-ups
