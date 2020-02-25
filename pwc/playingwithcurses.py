import curses
from .colors import colors

banner = """
+=====================+
|    Playing With     |
+=====================+
███ █ █ █▛▜ ███ ███ ███
█   █ █ █▙▟ █   █   █
█   █ █ █   ███ ███ ███
█   █ █ ██    █ █     █
███ ███ █ █ ███ ███ ███
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

    print(f"""
Term Height: {height}
Term Width: {width}
Banner X: {bannerx}
Banner Y: {bannery}""")
    stdscr.addstr(bannery, bannerx, banner, curses.color_pair(1))



def main():
    curses.wrapper(curses_func)


# This is needed, or else calling `python -m pwc` will mean that main() is called twice
if __name__ == "__main__":
    main()