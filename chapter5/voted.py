#!/usr/bin/env python
# -*- coding: utf-8 -*-

voted = {}


def check_voter(name):
    if voted.get(name):
        print("Kick", name, "out!")
    else:
        voted[name] = True
        print("Let", name, "vote...")


check_voter('Emilio')
check_voter('Emilio')
check_voter('Sarah')
check_voter('Sarah')
