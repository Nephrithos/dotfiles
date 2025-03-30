from libqtile import bar, qtile
from .widgets import *
from libqtile.config import Screen

import os


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


# All other monitors' bars will display everything but widgets 22 (systray) and 23 (spacer).
# def init_widgets_screen2():
#    widgets_screen2 = init_widgets_list()
#    del widgets_screen2[15:16]
#    return widgets_screen2


# For adding transparency to your bar, add (background="#00000000") to the "Screen" line(s)
# For ex: Screen(top=bar.Bar(widgets=init_widgets_screen2(), background="#00000000", size=24)),


def init_screens():
    return [
        Screen(
            top=bar.Bar(widgets=init_widgets_screen1(), margin=[8, 12, 0, 12], size=28)
        ),
        Screen(
            # top=bar.Bar(widgets=init_widgets_screen2(), margin=[8, 12, 0, 12], size=28)
        ),
        Screen(
            # top=bar.Bar(widgets=init_widgets_screen2(), margin=[8, 12, 0, 12], size=8)
        ),
    ]


screens = init_screens()
widgets_list = init_widgets_list()
widgets_screen1 = init_widgets_screen1()
widgets_screen2 = init_widgets_screen2()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)
