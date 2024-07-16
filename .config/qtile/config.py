# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import re
import socket
import subprocess
from typing import List
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration


@hook.subscribe.startup_once
def autostart():
        processes = [
            ['picom', '-b'],
            ['teams'],
            ['teamviewer'],
            ['sh', '/home/nephrithos/.config/qtile/autostart.sh'],
        ]
        for p in processes:
            subprocess.Popen(p)


mod = "mod4"
terminal = "kitty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], 'space', lazy.window.toggle_floating(), desc="toggle floating window on/off"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn('/home/nephrithos/.config/rofi/launchers/type-6/launcher.sh'), desc="Spawn rofi"),
    # Spawn Firefox
    Key([mod],"b", lazy.spawn('firefox'), desc="Spawn firefox"),

    # Spawn Teams
    Key([mod],"t", lazy.spawn('teams-for-linux'), desc="Spawn teams"),
    # Spawn Teamviewer
    Key([mod],"v", lazy.spawn('teamviewer'), desc="Spawn TeamViewer"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-"), desc="Lower Volume by 5%"),

    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+"), desc="Raise Volume by 5%"),

    Key([], "XF86AudioMute", lazy.spawn("amixer sset Master 1+ toggle"), desc="Mute/Unmute Volume"),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause player"),

    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),

    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),
]

groups = [
    Group("1", matches=[Match(wm_class=["teamviewer"])]),
    Group("2", matches=[Match(wm_class=["firefox"])]),
    Group("3", matches=[Match(wm_class=["microsoft teams - preview"])]),
    Group("4", matches=[Match(wm_class=[terminal])]),

]
## groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus_stack = ["#d75f5f", "#8f3d3d"],
        border_width = 0,
        margin = 8
    ),
    layout.Max(
            margin = 8
        ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

##### COLORS #####
colors = [["#2e3440", "#2e3440"],  # panel background
          ["#434758", "#434758"],  # background for current screen tab
          ["#ffffff", "#ffffff"],  # font color for group names
          ["#ff5555", "#ff5555"],  # border line color for current tab
          ["#8d62a9", "#8d62a9"],  # border line color for other tab and odd widgets
          ["444444", "444444"],  # color for the even widgets
          ["#e1acff", "#e1acff"]]  # window name
background="444444"

##### PROMPT #####
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="FiraCode NF",
    fontsize=14,
    padding=2,
    background='#ff0000.0', opacity=1,
    theme_path="~/.local/share/icons/Adwaita/16x16/status"
)

decoration_group = {
    "decorations": [
        RectDecoration(
            clip = True,
            colour="#004040", 
            radius=10, 
            filled=True, 
            group=True)
    ],
    "padding": 10,
}
extension_defaults = widget_defaults.copy()

##### WIDGETS #####


def init_widgets_list():
    widgets_list = [
        widget.GroupBox(
            # font="Ubuntu Bold",
            fontsize=12,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=10,
            borderwidth=3,
            active=colors[2],
            inactive=colors[2],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[3],
            this_screen_border=colors[4],
            other_current_screen_border=colors[0],
            other_screen_border=colors[0],
            foreground=colors[2],
            background=colors[0],
            **decoration_group
        ),
        widget.OpenWeather(
            app_key='65eb1b03cab1bdc06fdf5f037f879d04',
            cityid='2165828',
            update_interval=10,
            fontsize=14,
            metric=False,
            background=colors[0],
            foreground=colors[2],
            format=("{icon} {main_temp} "
                    "°{units_temperature}")
        ),
        widget.WindowName(
            font="FiraCode NF",
            foreground=colors[2],
            background=colors[0],
            padding=15
        ),
        widget.CheckUpdates(
            update_interval=60,
            distro="Arch_paru",
            display_format="Updates: {updates} ",
            no_update_string='No updates',
            foreground=colors[5],
            colour_have_updates=colors[2],
            colour_no_updates=colors[2],
            mouse_callbacks={'Button1': lambda: lazy.spawn(terminal + 'paru')},
            padding=5,
            background=colors[0],
        ),
        widget.StatusNotifier(
            background=colors[0],
            foreground=colors[2],
            **decoration_group
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            background="#818589",
            scale=0.7,
            **decoration_group
          
        ),
        widget.CurrentLayout(
            foreground=colors[2],
            background="#818589",
            **decoration_group
         
        ),
        widget.CapsNumLockIndicator(
            foreground=colors[2],
            background="#818589",
            **decoration_group
        ),
        widget.Clock(
            format="%A %d %B  [ %H:%M ]",
            **decoration_group
        ),

    ]
    return widgets_list

# SCREENS ##### (TRIPLE MONITOR SETUP)


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[4]   # Slicing removes unwanted widgets on Monitors 1,3
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    # Monitor 2 will display all widgets in widgets_list
    return widgets_screen2


def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26),wallpaper='~/.config/qtile/wallpaperflare.com_wallpaper.jpg'),
        Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26),wallpaper='~/.config/qtile/wallpaperflare.com_wallpaper.jpg'),
        Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=26),wallpaper='~/.config/qtile/city_scapes_1080x1920.jpg')
    ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()



# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True



# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
