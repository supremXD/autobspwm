import os, time 



def bspwm():
    os.system("clear")
    print("")
    os.system("sudo apt update")
    os.system("sudo apt install -y xorg xinit git build-essential bspwm sxhkd kitty alacritty picom feh unzip xclip rofi")
    os.system("mkdir -p ~/.config/bspwm")
    os.system("cp files/bspwm/bspwmrc ~/.config/bspwm/")
    os.system("chmod +x ~/.config/bspwm/bspwmrc")
    os.system("mkdir -p ~/.config/picom")
    os.system("cp files/picom/picom.conf ~/.config/picom/")
    os.system("mkdir -p ~/.config/alacritty")
    os.system("cp files/alacritty/alacritty.toml ~/.config/alacritty/")
    os.system("mkdir -p ~/.config/kitty")
    os.system("cp files/kitty/kitty.conf ~/.config/kitty/")
    os.system("clear")
    os.system("mkdir -p ~/.config/sxhkd")
    os.system("")
    terminal = input("Do you want to use kitty or alacritty as the default terminal? (kitty/alacritty)-->> ")
    if terminal == "kitty":
        os.system("cp files/sxhkd/kitty/sxhkdrc ~/.config/sxhkd/")
    elif terminal == "alacritty":
        os.system("cp files/sxhkd/alacritty/sxhkdrc ~/.config/sxhkd/")
    else:
        print("Incorrect format, alacritty was selectec for default terminal")
        time.sleep(3)
    polybar = input("Do you want to install polybar? (y/n)-->> ")
    if polybar == "y":
        os.system("sudo apt install polybar -y")
        os.system("mkdir -p ~/.config/polybar")
        os.system("cp -r files/polybar/* ~/.config/polybar/")
        os.system("chmod +x ~/.config/polybar/scripts/copy_ip.sh")
        os.system("chmod +x ~/.config/polybar/scripts/ip.sh")
        os.system("chmod +x ~/.config/polybar/scripts/powermenu.sh")
        os.system("mkdir -p ~/.local/share/fonts")
        os.chdir(os.path.expanduser ("~/.local/share/fonts/"))
        os.system("wget https://github.com/ryanoasis/nerd-fonts/releases/latest/download/JetBrainsMono.zip")
        os.system("unzip JetBrainsMono.zip")
        os.system("rm JetBrainsMono.zip")
        os.system("fc-cache -fv")
        os.chdir(os.path.expanduser("~"))
    elif polybar == "n":
        print("")
    else:
        print("Nothing selected, not installig polybar...")
        time.sleep(3)
        os.system("clear")
        print("")
    os.system('echo "exec bspwm" > ~/.xinitrc')
    aliases = [
        '',
        'alias editbspwmrc="nano ~/.config/bspwm/bspwmrc"',
        'alias editsxhkdrc="nano ~/.config/sxhkd/sxhkdrc"',
        'alias editpolybar="nano ~/.config/polybar/config.ini"',
        'alias editpicom="nano ~/.config/picom/picom.conf"',
        'alias editalacritty="nano ~/.config/alacritty/alacritty.toml"',
        'alias editkitty="nano ~/.config/kitty/kitty.conf"',
        'alias s="startx"'
    ]
    for alias in aliases:
        os.system(f"echo '{alias}' >> ~/.zshrc")
    os.system("clear")
    print("")
    print("Done!")
    exit()



def main():
    confirm = input("Are you sure you want to install bspwm and its configurations? (y/n)-->> ")
    if confirm == "y":
        bspwm()
    elif confirm == "n":
        exit()
    else:
        print("Invalid format, exiting...")
        exit()

    


if __name__ == "__main__":
    main()