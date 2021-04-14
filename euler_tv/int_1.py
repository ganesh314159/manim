#!/usr/bin/env python

from manimlib.imports import *

class int(Scene) :
    def construct(self) :
        text00 = TextMobject('''Here's a new question for you''')
        text00.scale(2)
        text01 = TextMobject('''Here's a new question for you''')
        text01.scale(2)
        text01.to_edge(UP)
        text10 = TextMobject('''If you think that you can solve this integral''', '''\n
        then you can't solve it''')
        text10.scale(1.3)
        text10.to_edge(DOWN)
        text20 = TextMobject('''Solution will be posted later!''', '''\n
        But still you can try it!''','''\n
        Try it on your self and comment the answer!''')
        text20.scale(1.3)
        text20.to_edge(DOWN, buff=1.1)
        formula00 = TexMobject("\int_{-2}^{1}\\frac{1}{x^{2}}dx")
        formula00.scale(2)
        formula01 = TexMobject("\int_{-2}^{1}\\frac{1}{x^{2}}dx")
        formula01.scale(3)
        formula01.to_edge(UP, buff=0.5)
        self.play(Write(text00), run_time=5)
        self.wait(2)
        self.play(ReplacementTransform(text00, text01))
        self.play(Write(formula00), run_time=4)
        self.wait(1)
        self.play(Write(text10[0:1]), run_time=3)
        self.wait(1)
        self.play(Write(text10[1:2]), run_time=2)
        self.wait(2)
        self.play(FadeOutAndShift(text01), FadeOutAndShift(text10), run_time=2)
        self.play(ReplacementTransform(formula00, formula01), run_time=1)
        self.play(Write(text20[0:1]))
        self.wait(0.5)
        self.play(Write(text20[1:2]))
        self.wait(0.5)
        self.play(Write(text20[2:3]))
        self.wait(3)
        self.play(FadeOutAndShift(text20), FadeOutAndShift(formula01), run_time=2)

class ans(Scene) :
    def construct(self) :
        text00 = TextMobject("Solution")
        text10 = TextMobject('''You can get its answer by using''', '''\n
        general defination of definite integral''')
        text20 = TextMobject('''Applying the limits''')
        text30 = TextMobject('''But it's not a right answer to this question''')
        text40 = TextMobject('''If you look at the graph of this function''')
        text50 = TextMobject('''You will realise that this''', '''\n
        function is not defined at x=0''')
        text60 = TextMobject('''That means you can't integrate it between -2 to 1''')
        limit0n = TexMobject("0^-")
        limit0p = TexMobject("0^+")
        # text70 = TextMobject('''But you can integrate it between''', '''\n
        # -2 to ''' + limit0n + ''' and ''' + limit0p + ''' to 1''')
        tex00 = TextMobject('''\\textbf{But you can integrate it between}''', '''\n
        -2\ \\textbf{to}\ 0^{-}\ \\textbf{and}\ 0^{+}\ \\textbf{to}\ 1''')
        self.play(Write(tex00))
        self.wait(6)






