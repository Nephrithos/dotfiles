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
import subprocess
from libqtile import bar,extension, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import RectDecoration

# Startup Applications
@hook.subscribe.startup_once
def autostart():
    if qtile.core.name == "x11":
        autostartscript = "~/.config/qtile/scripts/x11-autostart.sh"
    elif qtile.core.name == "wayland":
        autostartscript = "~/.config/qtile/scripts/wayland-autostart.sh"

    home = os.path.expanduser(autostartscript)
    subprocess.Popen([home])

if qtile.core.name == "wayland":
    os.environ["XDG_SESSION_DESKTOP"] = "qtile:wlroots"
    os.environ["XDG_CURRENT_DESKTOP"] = "qtile:wlroots"


mod = "mod4"
terminal = "kitty"
browser = "firefox"
rofi = os.path.expanduser("~/.config/rofi/launchers/type-6/launcher.sh")
ranger = "kitty -- ranger"
nvim = "kitty -- nvim"
rust = "rustdesk"

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
    Key([mod, "control"], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
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
    Key([mod], "b", lazy.spawn(browser), desc="Launch firefox"),
    Key([mod], "e", lazy.spawn(ranger, shell=True), desc="Launch ranger"),
    Key([mod], "n", lazy.spawn(nvim, shell=True), desc="Launch neovim"),
    Key([mod], "v", lazy.spawn(rust), desc="Launch rustdesk"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn(rofi, shell=True), desc="Spawn rofi launcher"),
]

groups = [Group(i) for i in "123456789"]

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
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
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

widget_defaults = dict(
    font="RobotoMono Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Clock(
                    format=" %m-%d %a %I:%M %p "
                ),
                widget.Spacer(
                    background='#1C00ff00',
                ),
                widget.GroupBox(
                    font = "RobotoMono Nerd Font Bold",
                    fontsize = 12,
                    margin_y = 2,
                    margin_x = 3,
                    padding_y = 2,
                    padding_x = 3,
                    borderwidth = 0,
                    disable_drag = True,
                    rounded = False,
                    highlight_method = "text",
                ),
                widget.Spacer(
                    background='#1C00ff00',
                ),
                widget.WindowName(),
                widget.Spacer(
                    background='#1C00ff00',
                ),
                widget.Systray(),
                widget.Spacer(
                    background='#1C00ff00',
                ),
                widget.CheckUpdates(
                    distro='Arch_paru',
                    no_update_string='0',
                    update_interval=60,
                    colour_no_updates='#008000',
                    colour_have_updates='#ff5733',
                    display_format='󰚰 {updates}',
                    padding=5
                ),
                widget.Net(
                    font = 'RobotoMono Nerd Font Bold',
                    fontsize = 12,
                    format = '{down} ↓↑ {up}',
                    interface = 'wlan0',
                    scroll = True,
                    scroll_fixed_width = True,
                    width = 150,
                    decorations = [
                        RectDecoration (
                            padding_y = 3,
                            radius = 2,
                            filled = True
                        ),
                    ],
                ),
                widget.Volume(
                    emoji=True,
                    fmt='{icon} {volume}%',
                    update_interval=0.2,
                    volume_app='pamixer',
                    volume_down_command='pamixer -d 5',
                    volume_up_command='pamixer -i 5',
                )

            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        wallpaper=os.path.expanduser("~/.dotfiles/.config/hypr/wallapapers/kakshi.jpeg"),
        wallpaper_mode='fill',
    ),
    Screen(
        top=bar.Bar(
            [
                widget.Clock(
                    format=" %m-%d %a %I:%M %p "
                ),
                widget.Spacer(
                    background='#1C00ff00',
                ),
                widget.GroupBox(
                    font = "RobotoMono Nerd Font Bold",
                    fontsize = 12,
                    margin_y = 2,
                    margin_x = 3,
                    padding_y = 2,
                    padding_x = 3,
                    borderwidth = 0,
                    disable_drag = True,
                    rounded = False,
                    highlight_method = "text",
                ),
                widget.Spacer(
                    background='#1C00ff00',
                ),
                widget.WindowName(),
                widget.Spacer(
                    background='#1C00ff00',
                ),
                widget.CheckUpdates(
                    distro='arch',
                    no_update_string='None',
                    update_interval=60,
                    colour_no_updates='#008000',
                    colour_have_updates='#ff5733',
                    fmt='󰚰 {updates}', 
                ),
                widget.Net(
                    font = 'RobotoMono Nerd Font Bold',
                    fontsize = 12,
                    format = '{down} ↓↑ {up}',
                    interface = 'wlan0',
                    decorations = [
                        RectDecoration (
                            padding_y = 3,
                            radius = 2,
                            filled = True
                        ),
                    ],
                ),
                widget.Volume(
                    emoji=True,
                    fmt='{icon} {volume}%',
                    update_interval=0.2,
                    volume_app='pamixer',
                    volume_down_command='pamixer -d 5',
                    volume_up_command='pamixer -i 5',
                )


            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        wallpaper=os.path.expanduser("~/.dotfiles/.config/hypr/wallapapers/kurama-and-naruto-bo-2560x1440.jpg"),
        wallpaper_mode='fill',
    ),
    Screen(
        top=bar.Bar(
            [
                widget.Clock(
                    format=" %m-%d %a %I:%M %p "
                ),
                widget.Spacer(
                    background='#1C00ff00',
                ),
                widget.GroupBox(
                    font = "RobotoMono Nerd Font Bold",
                    fontsize = 12,
                    margin_y = 2,
                    margin_x = 3,
                    padding_y = 2,
                    padding_x = 3,
                    borderwidth = 0,
                    disable_drag = True,
                    rounded = False,
                    highlight_method = "text",
                ),
                widget.Spacer(
                    background='#1C00ff00',
                ),
                widget.WindowName(),
                widget.Spacer(
                    background='#1C00ff00',
                ),
                widget.CheckUpdates(
                    distro='arch',
                    no_update_string='None',
                    update_interval=60,
                    colour_no_updates='#008000',
                    colour_have_updates='#ff5733',
                    fmt='󰚰 {updates}', 
                ),
                widget.Net(
                    font = 'RobotoMono Nerd Font Bold',
                    fontsize = 12,
                    format = '{down} ↓↑ {up}',
                    interface = 'wlan0',
                    decorations = [
                        RectDecoration (
                            padding_y = 3,
                            radius = 2,
                            filled = True
                        ),
                    ],
                ),
                widget.Volume(
                    emoji=True,
                    fmt='{icon} {volume}%',
                    update_interval=0.2,
                    volume_app='pamixer',
                    volume_down_command='pamixer -d 5',
                    volume_up_command='pamixer -i 5',
                )

            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
                # Set wallpaper
        wallpaper=os.path.expanduser("~/.dotfiles/.config/hypr/wallapapers/1331678.png"),
        wallpaper_mode='fill',
    ),

]

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
floats_kept_above = True
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
reconfigure_screens = False 

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
