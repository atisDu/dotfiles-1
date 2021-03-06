# This is my config, modify it to your liking
#   ____  _   _     _   _ __   __
#  / ___|| | | |   | | / \\ \ / /     Sujay R
#  \___ \| | | |_  | |/ _ \\ V /      Reddit: https://www.reddit.com/u/sujay1844
#   ___) | |_| | |_| / ___ \| |       Github: https://www.github.com/sujay1844
#  |____/ \___/ \___/_/   \_\_|  
                            
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

from typing import List  # noqa: F401
import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

# Keybindings
keys = [
    # Switch between windows in current stack pane
    Key([mod], "k",
        lazy.layout.down(),
            desc="Move focus down in stack pane"),
    Key([mod], "j",
        lazy.layout.up(),
            desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_down(),
            desc="Move window down in current stack "),
    Key([mod, "shift"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space",
        lazy.layout.next(),
            desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space",
        lazy.layout.rotate(),
            desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return",
        lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return",
        lazy.spawn("alacritty"),
            desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab",
        lazy.next_layout(),
            desc="Toggle between layouts"),
    Key([mod], "q",
        lazy.window.kill(),
            desc="Kill focused window"),

    Key([mod, "control"], "r",
        lazy.restart(),
            desc="Restart qtile"),
    Key([mod, "control"], "q",
        lazy.shutdown(),
             desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawn("dmenu_run"),
        desc="Spawn dmenu_run"),
    
    # Applications
    Key([mod], "v", 
        lazy.spawn("pavucontrol"),
            desc="Launch pavucontrol"),
    Key([mod], "b",
        lazy.spawn("blueman-manager"),
            desc="Launch Blueman Manager (Bluetooth Manager)"),
    Key([mod], "f",
        lazy.spawn("dolphin"),
            desc="Launch file manager"),
    Key([mod], "c",
        lazy.spawn("gnome-calculator"),
            desc="Launch gnome-calculator"),
    Key([mod], "t",
	lazy.spawn("alacritty"),
	    desc="Launch terminal"),
]

group_names = [("1", {'layout': 'floating'}),
               ("2", {'layout': 'monadtall'}),
               ("3", {'layout': 'monadtall'}),
               ("4", {'layout': 'monadtall'}),
               ("5", {'layout': 'monadtall'}),
               ("6", {'layout': 'monadtall'}),
               ("7", {'layout': 'monadtall'}),
               ("8", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

#groups = [Group(i) for i in "12345678"]

#for i in groups:
#    keys.extend([
        # mod1 + letter of group = switch to group
#        Key([mod], i.name, lazy.group[i.name].toscreen(),
#            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
#        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
#    ])

layouts = [
    layout.MonadTall(),
    layout.Max(),
    layout.Floating(),
]

widget_defaults = dict(
    font='Noto Sans',
    fontsize=12,
    padding=5,
    background="#212121",
)
extension_defaults = widget_defaults.copy()

pipe=widget.TextBox(text='|')

colors=["#6ac16d","#f7383c",]

screens = [
    Screen(
        top=bar.Bar(
            [
		#widget.Image("/home/sujay1844/Downloads/archicon.png"),

		widget.GroupBox(
                    disable_drag=False,
                    highlight_method='block',
                    margin=5,
                    ),
                
                widget.WindowName(),
                
                widget.CapsNumLockIndicator(),pipe,
               
		widget.CurrentLayoutIcon(),
		widget.CurrentLayout(foreground=colors[1]),pipe,

		widget.TextBox(text='????'),

		widget.ThermalSensor(),pipe,

                widget.Clock(
                    format='%d-%m %a',
			foreground="#34bc39",
                    ),pipe,
                
                widget.Systray(),pipe,
                
                widget.BatteryIcon(theme_path="/usr/share/icons/Tela-dark/",foreground=colors[1]),
                widget.Battery(format='{percent:1.0%}', padding=0),pipe,
                widget.Clock(
                    format=' %I:%M %p',
                    fontsize="16",
                    font="Arial",
                    ),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

#@hook.subscribe.startup
#def autostart():
    #processes = [
    #    ['nitrogen','--restore'],
    #    ['blueman-applet'],
    #    ['telegram-desktop'],
    #]
    #home = os.path.expanduser('/home/sujay1844/.config/qtile/autostart.sh')
    #subprocess.call([home])
#for p in processes:
#    subprocess.Popen(p)
