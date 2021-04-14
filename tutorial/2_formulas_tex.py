#!/usr/bin/env python

from manimlib.imports import *

class Formula(Scene) :
    def construct(self) :
        text00=TextMobject("The mathematical problem,\nwhich can give you 1 MILLION US DOLLARS.")
        text00.scale(0.8)
        text01=TextMobject("The mathematical problem,\nwhich can give you 1 MILLION US DOLLARS.")
        text01.scale(0.8)
        text01.to_edge(UP)
        text10=TextMobject("Riemanns Hypothesis")
        text10.scale(0.7)
        text10.to_edge(DOWN, buff=1)
        formula0=TexMobject("\zeta", "(s)", "=", "\sum_{n=1}^{\infty}", "\\frac{1}{n^{s}}")
        #                       0      1     2              3                     4
        formula0.scale(1.5)
        formula1=TexMobject("\zeta", "(s)", "=", "\sum_{n=1}^{\infty}", "\\frac{1}{n^{s}}", "=", "\\frac{1}{1^{s}}", "+" "\\frac{1}{2^{s}}" "+" "\\frac{1}{3^{s}}+....")
        #                      0       1     2              3                    4           5             6          7           8          9              10
        formula1.scale(1.5)
        self.play(Write(text00) , run_time=5)
        self.wait(2)
        self.play(ReplacementTransform(text00, text01))
        self.play(Write(text10),Write(formula0), run_time=3)
        # self.play(Write(formula0), run_time=3)
        self.wait(2)
        self.play(ReplacementTransform(formula0[0:], formula1[0:5]),
                  Write(formula1[5:])
        )
        self.wait(2)
        # text10.scale



