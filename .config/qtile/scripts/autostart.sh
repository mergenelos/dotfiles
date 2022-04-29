#!/bin/env bash

# set background
bash $HOME/.config/qtile/scripts/.fehbg

# Kill if already running
killall -9  picom xfce4-power-manager ksuperkey dunst \
            sxhkd eww workrave redshift-gtk pcmanfm nm-applet\
            blueman-applet openrgb copyq kdeconnect-indicator

# Launch Conkeww
sed -i "s/colors\/color-.*/colors\/color-dracula.yuck\")/g" $HOME/.config/conkeww/eww.yuck
eww --config $HOME/.config/conkeww/ open conkeww-main

# start hotkey daemon
#sxhkd &

# Launch notification daemon
pgrep -xu "$USER" dunst >/dev/null || dunst -config $HOME/.config/qtile/dunstrc &

# Enable Super Keys For Menu
ksuperkey -e 'Super_L=Alt_L|F1' &
ksuperkey -e 'Super_R=Alt_L|F1' &

# power manager and picom start
xfce4-power-manager &
picom --config $HOME/.config/qtile/picom.conf &

if [[ ! `pidof xfce-polkit` ]]; then
    /usr/lib/xfce-polkit/xfce-polkit &
fi

#xautolock -time 30 -locker /usr/bin/i3lock-fancy-dualmonitor -detectsleep &

# Start xautolock daemon
#pgrep -xu "$USER" xautolock >/dev/null || \
#    xautolock -locker "i3lock-fancy-dualmonitor -pt ''" -time 30 &
#pgrep -xu "$USER" xss-lock >/dev/null || \
#    xss-lock -n "Lock activated" --  i3lock-fancy-dualmonitor -pt '' &


# Keyboard layout
setxkbmap -model pc105 -layout us,az,tr,ir -option grp:alt_shift_toggle &

# Start udiskie for device automonting
grep -xu "$USER" udiskie >/dev/null ||udiskie &

grep -xu "$USER" nm-applet >/dev/null || nm-applet &
/usr/bin/emacs --daemon &
grep -xu "$USER" openrgb >/dev/null || openrgb --startminimized &
grep -xu "$USER" copyq >/dev/null || copyq &
grep -xu "$USER" kdeconnect-indicator >/dev/null || kdeconnect-indicator &

# Hide mouse after idle
grep -xu "$USER" unclutter >/dev/null || unclutter -idle 1 &

# Polkit agent
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Change screen timeout
# xset s 590 590

# run Bluetooth app
grep -xu "$USER" blueman-applet >/dev/null || sleep 2 && blueman-applet &

# Fix touchpad
fix_xcursor &

# Fix theming
ff-theme-util &

# Touchpad setup
xsetroot -cursor_name left_ptr &

# Set numlock on
numlockx on &

# Player control deamon
playerctld &

# File manager deamon
grep -xu "$USER" pcmanfm >/dev/null ||  pcmanfm -d &

# Start Update-notifier
sleep 2 && /usr/bin/octopi-notifier &

# Location agent for redshift
/usr/lib/geoclue-2.0/demos/agent &

# Start Redshift
grep -xu "$USER" redshift-gtk >/dev/null || redshift-gtk &

# Start Workrave
grep -xu "$USER" workrave >/dev/null || workrave &

# Set wm type (for intellij)
wmname LG3D &


# # Start polybar
# # Terminate already running bar instances
# killall -q polybar
# # Wait until the processes have been shut down
# while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done
# # Launch bar1 and bar2
# polybar -c $HOME/.config/polybar/config.ini main &

# # Hot corners
# # Toggle visibility of systray
# xdotool behave_screen_edge --quiesce 600 --delay 0 top-left \
#     exec --sync "$BSPWM_CONFIG/scripts/toggleSysTray" &

