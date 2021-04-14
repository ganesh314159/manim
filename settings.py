#from manimlib.imports import *                 #New version
from manimlib.imports import *
 
class RenderingSettings(Scene):
    def construct(self):
        # Texts
        obj1=TextMobject("A")
        obj2=TextMobject("B").to_corner(UL)
        obj3=TextMobject("C").to_corner(UR)
        obj4=TextMobject("D").to_corner(DR)
        obj5=TextMobject("E").to_corner(DL)
        # Animations
        #
        self.play(Write(obj1)) #0
        self.wait(2)           #1
        #
        self.play(Write(obj2)) #2
        self.wait(2)           #3
        #
        self.play(Write(obj3)) #4
        self.wait(2)           #5
        #
        self.play(Write(obj4)) #6
        self.wait(2)           #7
        #
        self.play(Write(obj5)) #8
        self.wait(2)           #9
        #