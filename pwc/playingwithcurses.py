import curses
from .colors import colors

banner = """
+=====================+
|    Playing With     |
+=====================+
### # # ### ### ### ###
#   # # ### #   #   #
#   # # #   ### ### ###
#   # # ##    # #     #
### ### # # ### ### ###
"""
bannerheight = 8
bannerwidth = 23

def curses_func(stdscr):
    stdscr.scrollok(True)
    # Clear screen
    stdscr.clear()

    curses.init_pair(1, colors['GREEN'], colors['BLACK'])

    height, width = stdscr.getmaxyx()
    bannery = int((height / 2) - (bannerheight / 2))
    bannerx = int((width / 2) - (bannerwidth / 2))

    stdscr.addstr(bannerx, bannery, banner, curses.color_pair(1))



def main():
    curses.wrapper(curses_func)

main()