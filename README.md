# --- Brick Breaker Pong_game ---
## - About my project -
This project is about a classic pong game rewrite with Python. turtle method, but there are some extra features, that our classic one doesn't have.

First, for every 5 times the ball bounces will randomly create a new brick at a random location, but not any location on the map(mostly because if it spawns too low it will be impossible to hit/reflect sometimes).

Second, when playing, the ball speed will keep increasing bit by bit to increase difficulty, when the stage is cleared the speed will be reduced to the base speed of the new level.

This game also saves your highest scores, in case you want to know what's your best play too.

## - How to install/run -
1. Fork this repo to your GitHub 
2. Clone it to your pc folder
3. Open the folder and click "run_ball.py" file
4. Have fun!
 
## - Usage -
- To interact with this game. On your keyboard, use the Left and Right keys to move left and right in games.
- The expected output should be the ball moving around, and when it hits the wall/paddle or bricks it should bounce 90 degrees back. 
- Sadly I wasn't able to implement the inelastic collision, so sometimes the ball could potentially get stuck in a loop but I've already made a way to fix that in the game already 
so no worries!

Here's a link to how to start the game and play it. 
- https://youtu.be/cvrcs0FMv7E
## - Project design and implementation -
### - UML -
![image](https://github.com/user-attachments/assets/208e071b-531b-4be2-b879-c270c13973c8)



### - Purpose for each class -
1. class Ball: creates a ball object that can change its direction when collides with any surfaces
2. class Paddle: create a paddle object that can move left and right
3. class Obstacles: creates an obstacle with a rectangle shape and random colour
4. class InterfaceL: stores all UI interfaces of the game whether it's border, stats, etc.
5. class run_ball: stores the mechanics of the game, stores all class objects, and makes them functional



## - Use/Extend/Modify the code -
- I copied the method of drawing borders and made it work with other UI interfaces
- I put the method to move the paddle in the paddle class because I feel like that method should be the property of the paddle object.
- I rewrote how the game works. Prof.Paruj has __redraw and __draw methods for moving and animating objects but mine is the turtle itself,
- yes I know, doing it like Prof.Paruj would be better because the object can be deleted instantly and redrew at a different location and it's less laggy, but for my turtle, it seems like I cannot do it that way so the only method I could come up with to deal with this is to use hideturtle() method.
- Using this method might not be the best option because you just hide it. it didn't go away it's still there on the screen if the player keeps playing for like an hour, I'm sure some lags and nonfunctioning are likely to happen.

## - Description/Bugs known to be resolved -
**How I test my code:** 
- Through trial and error, I ran it and read the terminal error on which line the problem occurred.
- For balancing the game I played it myself paired with giving it out to some of my friends to test it and observe how they perform.
- From this, I can say that my project is not working at 100% the range will be between 80-90%. 

## For bugs to be resolved : 
(I could be wrong here on every topic it's just my assumption on how this happens)
- While playing, sometimes the ball goes through the paddle, which is likely to happen because the time the turtle updates, the ball gets to the paddle before the check function is triggered.
- The ball moves normally on my pc but slowly on my friend's pc. I have already provided a way to fix this problem in the run_ball.py. But the reason I have to put this in is that TA's pc might be like mine or 
  my friend's so if the ball moves slowly please refer to the fix method in run_ball.py (at the bottom of run_ball.py), also you can adjust the speed, I've already commented in where to set the initial speed.
- There's a chance the random obstacle spawner might triggered more than once. (This rarely happens, I found this bug while writing this README)

## - Sophistication level: 90 -
- if 100 is for inelastic collisions, I say mine would be 90 because my game can create a new brick at a random location and it collides with multiple surfaces it's quite unique for the game to have multiple 
  obstacles that can randomly spawn making the game more challenging and the ball can speed up itself. 

- I even implemented a method to fix the game, in case it goes into an infinite loop because of elastic collision (I know that it's not the best method but at least I tried to find a way to fix it). Moreover, I 
  almost rewrote the entire code again, I don't see much of Prof. Paruj's code in mine.

