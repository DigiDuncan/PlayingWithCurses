import curses
from pwc.colors import colors

banner = (
    "+=====================+\n"
    "|    Playing With     |\n"
    "+=====================+\n"
    "███ █ █ ███ ███ ███ ███\n"
    "█   █ █ ███ █   █   █\n"
    "█   █ █ █   ███ ███ ███\n"
    "█   █ █ ██    █ █     █\n"
    "███ ███ █ █ ███ ███ ███"
)
bannerheight = len(banner.split("\n"))
bannerwidth = max(len(l) for l in banner.split("\n"))


def printASCIIart(stdscr, y, x, art, color = 0):
    artlist = art.split("\n")
    cy = y
    for line in artlist:
        stdscr.addstr(cy, x, line, curses.color_pair(color))
        cy += 1


def curses_func(stdscr):
    stdscr.scrollok(True)

    # Clear screen
    stdscr.clear()

    curses.init_pair(1, colors['GREEN'], colors['BLACK'])

    height, width = stdscr.getmaxyx()
    bannery = int((height / 2) - (bannerheight / 2))
    bannerx = int((width / 2) - (bannerwidth / 2))

    print(
        f"Term Height: {height}\n"
        f"Term Width: {width}\n"
        f"Banner X: {bannerx}\n"
        f"Banner Y: {bannery}"
    )

    printASCIIart(stdscr, bannery, bannerx, banner, 1)

    stdscr.refresh()
    stdscr.getch()


def main():
    curses.wrapper(curses_func)


# This is needed, or else calling `python -m pwp` will mean that main() is called twice
if __name__ == "__main__":
    main()
