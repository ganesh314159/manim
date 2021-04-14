#!/usr/bin/env python

from manimlib.imports import *

class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 2
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}",font="Arial",stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)

# $ Absolute position
# object.function(parameters)
# Object is a shape we want to render :
# 1. Dot()
# 2. TextMobject("")
# Funcion is position of the object be rendered using Parameters
# 1. To render at edges :
#     to_edge()
#     Parameters are :
#     LEFT
#     RIGHT
#     UP
#     DOWN
# 2. To render at corners :
#     to_corner()
#     Parameters are :
#     UR = for upper left corner
#     UL = for upper right corner
#     DR = for down right corner
#     DL = for down left corner
# Some other parameters :
#     1. To render objects to closer to the edges use buff parameter, 
#        less the value of buff, object will be more closer to edge
#        .to_edge(DIRECTION, buff=NUMBER)
#     2.


class Position(Scene) :
    def construct(self) : 
        grid=ScreenGrid(rows=10, columns=10)
        object=Dot()
        object.to_edge(UP, buff=2)
        self.add(grid, object)
        self.wait(2)


# $ Relative position
# object.function(parameters)
# object is a shape we want to render :
# 1. Dot()
# 2. TextMobject("")
# Funcion is movement of the object to be rendered using Parameters
# 1. To move the objects :
#     .move_to()
#     Parameters are :
#     NUMBER*LEFT or RIGHT + NUMBER*RIGHT or LEFT 
#     # here NUMBER will be any integer or
#     # any float which will change the DIRECTION
#     # We can use vector too with co-ordinates to change DIRECTION 
#     vector=np.array([x,y,z]) # z will be always 0 for 2D plots
#     ReferenceText = To take any object as Reference
#     .get_center = to take an object as an centre

#     .next_to()
#     Parameters are :
#     buff = To render objects to closer to the edges use buff parameter, 
#            less the value of buff, object will be more closer to edge

#     .shift()
#     Parameters are :
#     RIGHT
#     LEFT
#     UP
#     DOWN

class Move(Scene) :
    def construct(self) :
        grid=ScreenGrid()
        object=Dot()
        ReferenceText=TextMobject("A")
        ReferenceText.move_to(3*LEFT+2*UP)
        # vector=np.array([-3, -2,  0])
        #                 x,  y,  z  
        # object.move_to(vector)
        # object.move_to(ReferenceText.get_center()+5*RIGHT)
        object.move_to(UP+RIGHT)
        # object.next_to(ReferenceText, RIGHT, buff=1)
        self.add(grid, ReferenceText, object)
        self.wait()
        object.shift(RIGHT)
        self.wait()
        object.shift(RIGHT)
        self.wait()
        object.shift(RIGHT)
        self.wait()
        object.shift(RIGHT)
        self.wait()
        object.shift(RIGHT)
        self.wait()


# $ Rotation of objects
# object.function(parameters)
# Object is a shape we want to render :
# 1. Dot()
# 2. TextMobject("")
# Funcion is rotation of the object to be rendered using Parameters
# 1. To rotate objects :
#     .rotate()
#     Parameters are :
#     Angle in radian format # ex. PI/2 or PI/4 or PI/6
#     Angle in degree format # ex. 45*DEGREES

class Rotate(Scene) :
    def construct(self) :
        textM = TextMobject("Text")
        textC = TextMobject("Reference text")
        textM.shift(UP)
        textM.rotate(PI/4) # <-- Radians
        # We can use .rotate(45*DEGREES) too
        self.play(Write(textM), Write(textC))
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI/4)
        self.wait(2)
        textM.rotate(PI)
        self.wait(2)


# $ Fliping objects
# object.function(parameters)
# Object is a shape we want to render :
# 1. Dot()
# 2. TextMobject("")
# Funcion is fliping of the object to be rendered using Parameters
# 1. To flip objects
#     .flip()
#     Parameters are :
#     UP
#     DOWN
#     RIGHT
#     LEFT

class Flip(Scene) :
    def construct(self) :
        textM = TextMobject("Text")
        textM.flip(UP)
        self.play(Write(textM))
        self.wait(2)

