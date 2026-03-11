import curses

scr = curses.initscr()
curses.curs_set(0)
scr.clear() 
scr.addstr(10,10,"Hello,world!!!")
scr.getch()
curses.endwin()
