from ecolor import slow_color, slow_print, ecolor
ecolor("This is red text", "red")
ecolor("This is bold blue text", "bold_blue")
slow_print("This is slow_print\n", 0.025)
slow_color("This is slow_print but colorful\n", "blue", 0.025)
slow_color("This is slow_print but colorful and bold\n", "bold_blue", 0.025)
