# --coding:utf-8--

import curses

scr = curses.initscr()
curses.curs_set(0)
scr.clear() 
scr.addstr(10, 10, "Hello,world!!!")
scr.addstr(11, 10, "Curses Library")
scr.getch()
curses.endwin()
