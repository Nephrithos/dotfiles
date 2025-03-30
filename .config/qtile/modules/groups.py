from libqtile.config import Group, Key
from libqtile.lazy import lazy
from .keys import mod, keys

groups = []

group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

group_labels = ["", "", "󰊻", "󰔀", "", "6", "7", "8", "9", "0"]

for i in range(len(group_names)):
    groups.append(Group(name=group_names[i], label=group_labels[i]))


for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
