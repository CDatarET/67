import curses
import time
import math

six = ["███", "█", "████", "█   █", " ███"]
seven = ["█████", "    █", "   █", "  █", " █"]

def tri(t):
    return 1 - abs((t % 2) - 1)

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)

    t = 0
    max_offset = 4

    while True:
        stdscr.erase()

        # constant-speed bounce (no easing slowdown)
        base = tri(t * 0.2)

        offset_six = int(base * max_offset)
        offset_seven = max_offset - offset_six

        six_lines = ([""] * offset_six) + six
        seven_lines = ([""] * offset_seven) + seven

        max_lines = max(len(six_lines), len(seven_lines))

        for i in range(max_lines):
            left = six_lines[i] if i < len(six_lines) else ""
            right = seven_lines[i] if i < len(seven_lines) else ""
            stdscr.addstr(i, 0, left.ljust(10) + "   " + right)

        stdscr.refresh()
        time.sleep(0.05)

        t += 1

        if stdscr.getch() != -1:
            break

try:
    curses.wrapper(main)
except KeyboardInterrupt:
    pass