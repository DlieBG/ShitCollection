#!/usr/bin/env python3
import sys, os,string

vaterUnser="""
Vater unser im Himmel,
geheiligt werde dein Name.
Dein Reich komme.
Dein Wille geschehe,
wie im Himmel so auf Erden.
Unser tägliches Brot gib uns heute.
Und vergib uns unsere Schuld,
wie auch wir vergeben unsern Schuldigern.
Und führe uns nicht in Versuchung,
sondern erlöse uns von dem Bösen.
Denn dein ist das Reich und die Kraft
und die Herrlichkeit in Ewigkeit.
Amen.
"""

vaterUnser=vaterUnser.lower()
for letter in string.ascii_lowercase:
    if letter not in vaterUnser:
        print(letter+" is not in VaterUnser")
