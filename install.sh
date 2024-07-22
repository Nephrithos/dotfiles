#!/bin/bash

log_file=~/install_log.txt

sudo pacman -S  --noconfirm --needed zsh 
if type -p zsh > /dev/null; then
    echo "zsh Installed" >> $log_file
else
    echo "zsh FAILED TO INSTALL!!!" >> $log_file
fi

sudo pacman -S --noconfirm --needed  zsh-syntax-highlighting

sudo pacman -S --noconfirm --needed base-devel

if type -p base-devel > /dev/null; then
    echo "base-devel Installed" >> $log_file
else
    echo "base-devel FAILED TO INSTALL!!!" >> $log_file
fi


sudo pacman -S --noconfirm --needed git
if type -p git > /dev/null; then
    echo "git Installed" >> $log_file
else
    echo "git FAILED TO INSTALL!!!" >> $log_file
fi

git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si --noconfirm --needed
if type -p paru > /dev/null; then
    echo "paru Installed" >> $log_file
else
    echo "paru FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed ckb-next 
if type -p ckb-next > /dev/null; then
    echo "ckb-next Installed" >> $log_file
else
    echo "ckb-next FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed neofetch 
if type -p neofetch > /dev/null; then
    echo "neofetch Installed" >> $log_file
else
    echo "neofetch FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed dunst 
if type -p dunst > /dev/null; then
    echo "dunst Installed" >> $log_file
else
    echo "dunst FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed kitty 
if type -p dunst > /dev/null; then
    echo "kitty Installed" >> $log_file
else
    echo "kitty FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed anydesk-bin
if type -p anydesk-bin > /dev/null; then
    echo "anydesk-bin Installed" >> $log_file
else
    echo "anydesk-bin FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed grim
if type -p grim > /dev/null; then
    echo "grim Installed" >> $log_file
else
    echo "grim FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed grimblast-git
if type -p grimblast-git > /dev/null; then
    echo "grimblast-git Installed" >> $log_file
else
    echo "grimblast-git FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed mattermost-desktop-bin 
if type -p mattermost-desktop-bin > /dev/null; then
    echo "mattermost-desktop Installed" >> $log_file
else
    echo "mattermost-desktop FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed nwg-displays
if type -p nwg-displays > /dev/null; then
    echo "nwg-displays Installed" >> $log_file
else
    echo "nwg-displays FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed onlyoffice-bin 
if type -p onlyoffice-bin > /dev/null; then
    echo "onlyoffice Installed" >> $log_file
else
    echo "onlyoffice FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed font-awesome-5


paru -S --noconfirm --removemake --needed rofi rofi-mixer-git rofi-emoji
if type -p rofi-emoji > /dev/null; then
    echo "rofi rofi-mixer-git rofi-emoji Installed" >> $log_file
else
    echo "rofi rofi-mixer-git rofi-emoji FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed spotify
if type -p spotify > /dev/null; then
    echo "spotify Installed" >> $log_file
else
    echo "spotify FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed teams-for-linux
if type -p teams-for-linux > /dev/null; then
    echo "teams-for-linux Installed" >> $log_file
else
    echo "teams-for-linux FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed composer
if type -p composer > /dev/null; then
    echo "composer Installed" >> $log_file
else
    echo "composer FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed python-pip
if type -p python-pip > /dev/null; then
    echo "python-pip Installed" >> $log_file
else
    echo "python-pip FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed cups
if type -p cups > /dev/null; then
    echo "cups Installed" >> $log_file
else
    echo "cups FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed firefox
if type -p dunst > /dev/null; then
    echo "firefox Installed" >> $log_file
else
    echo "firefox FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed zip unzip
if type -p unzip > /dev/null; then
    echo "zip unzip Installed" >> $log_file
else
    echo "zip unzip FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed htop
if type -p htop > /dev/null; then
    echo "htop Installed" >> $log_file
else
    echo "htop FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed waypaper-git
if type -p waypaper-git > /dev/null; then
    echo "waypaper-git Installed" >> $log_file
else
    echo "waypaper-git FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed julia
if type -p julia > /dev/null; then
    echo "julia Installed" >> $log_file
else
    echo "julia FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed lazygit
if type -p lazygit dunst > /dev/null; then
    echo " Installed" >> $log_file
else
    echo "lazygit FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed noto-fonts-emoji


paru -S --noconfirm --removemake --needed npm
if type -p npm > /dev/null; then
    echo "npm Installed" >> $log_file
else
    echo "npm FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed openshh
if type -p openshh > /dev/null; then
    echo "openshh Installed" >> $log_file
else
    echo "openshh FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed nerd-fonts

paru -S --noconfirm --removemake --needed pavucontrol
if type -p pavucontrol > /dev/null; then
    echo "pavucontrol Installed" >> $log_file
else
    echo "pavucontrol FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed php
if type -p php > /dev/null; then
    echo "php Installed" >> $log_file
else
    echo "php FAILED TO INSTALL!!!" >> $log_file
fi
paru -S --noconfirm --removemake --needed python-pillow
if type -p python-pillow > /dev/null; then
    echo "python-pillow Installed" >> $log_file
else
    echo "python-pillow FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed python-virtualenv
if type -p python-virtualenv > /dev/null; then
    echo "python-virtualenv Installed" >> $log_file
else
    echo "python-virtualenv FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed ranger
if type -p ranger > /dev/null; then
    echo "ranger Installed" >> $log_file
else
    echo "ranger FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed ruby
if type -p ruby > /dev/null; then
    echo "ruby Installed" >> $log_file
else
    echo "ruby FAILED TO INSTALL!!!" >> $log_file
fi
paru -S --noconfirm --removemake --needed ripgrep
if type -p ripgrep > /dev/null; then
    echo "ripgrep Installed" >> $log_file
else
    echo "ripgrep FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed steam
if type -p steam > /dev/null; then
    echo "steam Installed" >> $log_file
else
    echo "steam FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed udiskie
if type -p udiskie > /dev/null; then
    echo "udiskie Installed" >> $log_file
else
    echo "udiskie FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed viewnior-git
if type -p viewnior-git > /dev/null; then
    echo "viewnior Installed" >> $log_file
else
    echo "viewnior FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed vlc
if type -p vlc > /dev/null; then
    echo "vlc Installed" >> $log_file
else
    echo "vlc FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed wl-clipboard
if type -p wl-clipboard > /dev/null; then
    echo "wl-clipboard Installed" >> $log_file
else
    echo "wl-clipboard FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed xdg-desktop-portal-hyprland-git
if type -p xdg-desktop-portal-hyprland-git > /dev/null; then
    echo "xdg-desktop-portal-hyprland-git Installed" >> $log_file
else
    echo "xdg-desktop-portal-hyprland-git FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed xorg-xwayland
if type -p xorg-xwayland > /dev/null; then
    echo "xorg-xwayland Installed" >> $log_file
else
    echo "xorg-xwayland FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed yarn
if type -p yarn > /dev/null; then
    echo "yarn Installed" >> $log_file
else
    echo "yarn FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed zathura zathura-pdf-mupdf
if type -p zathura-pdf-mupdf > /dev/null; then
    echo "zathura zathura-pdf-mupdf Installed" >> $log_file
else
    echo "zathura zathura-pdf-mupdf FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed archzfs
if type -p archzfs > /dev/null; then
    echo "archzfs Installed" >> $log_file
else
    echo "archzfs FAILED TO INSTALL!!!" >> $log_file
fi

paru -S --noconfirm --removemake --needed waybar
if type -p waybar > /dev/null; then
    echo "waybar Installed" >> $log_file
else
    echo "waybar FAILED TO INSTALL!!!" >> $log_file
fi

echo -e "\n====== Summary ======\n"
cat $log_file
echo
echo "Enjoy -Jarrod"
rm $log_file

ln -sf ~/.dotfiles/.config/dunst ~/.config/dunst
ln -sf ~/.dotfiles/.config/gtk-2.0 ~/.config/gtk-2.0
ln -sf ~/.dotfiles/.config/gtk-3.0 ~/.config/gtk-3.0
ln -sf ~/.dotfiles/.config/kitty ~/.config/kitty
ln -sf ~/.dotfiles/.config/hypr ~/.config/hypr
ln -sf ~/.dotfiles/.config/lazygit ~/.config/lazygit
ln -sf ~/.dotfiles/.config/neofetch ~/.config/neofetch
ln -sf ~/.dotfiles/.config/nvim ~/.config/nvim
ln -sf ~/.dotfiles/.config/ranger ~/.config/ranger
ln -sf ~/.dotfiles/.config/rofi ~/.config/rofi
ln -sf ~/.dotfiles/.config/swaylock ~/.config/swaylock
ln -sf ~/.dotfiles/.config/viewnior ~/.config/viewnior
ln -sf ~/.dotfiles/.config/Vieb ~/.config/Vieb
ln -sf ~/.dotfiles/.config/swaylock ~/.config/swaylock
ln -sf ~/.dotfiles/.config/Vieb ~/.config/Vieb
ln -sf ~/.dotfiles/.config/viewnior ~/.config/viewnior
ln -sf ~/.dotfiles/.config/waybar ~/.config/waybar
ln -sf ~/.dotfiles/.config/waypaper ~/.config/waypaper
ln -sf ~/.dotfiles/.config/wlogout ~/.config/wlogout
