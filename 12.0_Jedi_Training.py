'''
# 12.0 Jedi Training (10 pts)  Name:________________
 
Update the code in this chapter to do the following:
Open a 500px by 500px window.
Change the Ball class to a Box class.
Instantiate two 30px by 30px boxes. One red and one blue.
Make the blue box have a speed of 240 pixels/second
Make the red box have a speed of 180 pixels/second
Control the blue box with the arrow keys.
Control the red box with the WASD keys.
Do not let the boxes go off of the screen.
Incorporate different sounds when either box hits the edge of the screen.
Have two people play this TAG game at the same time.
The red box is always "it" and needs to try to catch the blue box.
When you're done demonstrate to your instructor!


Starter Testing Code:
'''
import arcade
SW = 500
SH = 500
BLUE_SPEED = 4
RED_SPEED = 3

class Box:
    def __init__(self, pos_x, pos_y, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = 0
        self.dy = 0
        self.col = col
        self.laser_sound = arcade.load_sound("sounds/laser.wav")
        self.explosion_sound = arcade.load_sound("sounds/explosion.wav")

    def draw_box(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, 30, 30, self.col)

    def update_red_box(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        # screen border collision
        if self.pos_x < 15:
            self.pos_x = 15
            arcade.play_sound(self.laser_sound)
        if self.pos_x > SW - 15:
            self.pos_x = SW - 15
            arcade.play_sound(self.laser_sound)
        if self.pos_y < 15:
            self.pos_y = 15
            arcade.play_sound(self.laser_sound)
        if self.pos_y > SH - 15:
            self.pos_y = 15
            arcade.play_sound(self.laser_sound)

    def update_blue_box(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        #screen border collision
        if self.pos_x < 15:
            self.pos_x = 15
            arcade.play_sound(self.explosion_sound)
        if self.pos_x > SW - 15:
            self.pos_x = SW - 15
            arcade.play_sound(self.explosion_sound)
        if self.pos_y < 15:
            self.pos_y = 15
            arcade.play_sound(self.explosion_sound)
        if self.pos_y > SH - 15:
            self.pos_y = 15
            arcade.play_sound(self.explosion_sound)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.set_mouse_visible(False)
        self.red = Box(100, 100, arcade.color.RED)
        self.blue = Box(400, 400, arcade.color.BLUE)

    def on_draw(self):
        arcade.start_render()
        self.red.draw_box()
        self.blue.draw_box()

    def on_update(self, dt):
        self.red.update_red_box()
        self.blue.update_blue_box()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.red.dx = -RED_SPEED
        elif key == arcade.key.D:
            self.red.dx = RED_SPEED
        elif key == arcade.key.W:
            self.red.dy = RED_SPEED
        elif key == arcade.key.S:
            self.red.dy = -RED_SPEED

        if key == arcade.key.LEFT:
            self.blue.dx = -BLUE_SPEED
        elif key == arcade.key.RIGHT:
            self.blue.dx = BLUE_SPEED
        elif key == arcade.key.UP:
            self.blue.dy = BLUE_SPEED
        elif key == arcade.key.DOWN:
            self.blue.dy = -BLUE_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.A or key == arcade.key.D:
            self.red.dx = 0
        elif key == arcade.key.W or key == arcade.key.S:
            self.red.dy = 0

        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.blue.dx = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.blue.dy = 0


def main():
    window = MyGame(SW, SH, "User Control Practice")
    arcade.run()

if __name__=="__main__":
    main()