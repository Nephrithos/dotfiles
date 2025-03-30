from libqtile import widget, qtile
from .keys import myTerm
from .colors import Nord as colors

widget_defaults = dict(font="Ubuntu Bold", fontsize=12, padding=0, background=colors[0])

extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Spacer(length=12),
        widget.Image(
            filename="~/.config/qtile/wallapapers/nephrithos.png",
            scale="False",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm)},
        ),
        widget.Prompt(font="Ubuntu Mono", fontsize=14, foreground=colors[1]),
        widget.GroupBox(
            fontsize=12,
            margin_y=5,
            margin_x=8,
            padding_y=0,
            padding_x=1,
            borderwidth=3,
            active=colors[8],
            inactive=colors[9],
            rounded=False,
            highlight_color=colors[2],
            highlight_method="line",
            this_current_screen_border=colors[7],
            this_screen_border=colors[4],
            other_current_screen_border=colors[7],
            other_screen_border=colors[4],
        ),
        widget.TextBox(
            text="|", font="Ubuntu Mono", foreground=colors[9], padding=2, fontsize=14
        ),
        widget.CurrentLayout(foreground=colors[1], padding=5),
        widget.TextBox(
            text="|", font="Ubuntu Mono", foreground=colors[9], padding=2, fontsize=14
        ),
        widget.WindowName(foreground=colors[6], padding=4, max_chars=40),
        widget.CPU(
            format=" Cpu: {load_percent}%",
            foreground=colors[4],
            padding=6,
        ),
        widget.Memory(
            foreground=colors[8],
            padding=6,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm + " -e htop")},
            format="{MemUsed: .0f}{mm}",
            fmt="🖥  Mem: {} used",
        ),
        widget.DF(
            update_interval=60,
            foreground=colors[5],
            padding=6,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(myTerm + " -e df")},
            partition="/",
            # format = '[{p}] {uf}{m} ({r:.0f}%)',
            format="{uf}{m} free",
            fmt="󰋊  Disk: {}",
            visible_on_warn=False,
        ),
        widget.Volume(
            foreground=colors[7],
            padding=6,
            fmt="󰖀  Vol: {}",
        ),
        widget.KeyboardLayout(
            foreground=colors[4],
            padding=6,
            fmt="⌨  Kbd: {}",
        ),
        widget.Clock(
            foreground=colors[8],
            padding=6,
            format="⏱  %a, %b %d - %H:%M",
        ),
        widget.Systray(padding=3),
        widget.Spacer(length=8),
    ]
    return widgets_list
