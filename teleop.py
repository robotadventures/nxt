#!/usr/bin/python

import control
import curses

class TeleOp:
    stdscr = None
    control = None

    def __init__(self, control):
        self.control = control
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.clear()
        self.loop()

    def __del__(self):
        curses.endwin()

    def clear(self):
        self.stdscr.erase()
        self.stdscr.addstr(0,10,"Hit 'q' to quit")

    def readTacho(self):
        left, right = self.control.getTacho()
        self.stdscr.addstr(2, 4, "Left Degrees:  %d        " % left)
        self.stdscr.addstr(3, 4, "Right Degrees: %d        " % right)

    def loop(self):
        self.stdscr.timeout(250)
        k = ''
        while k != ord('q'):
            self.readTacho()

            k = self.stdscr.getch()
            #self.stdscr.addstr(5, 4, "k = %d" % k)
            if k == 65: #curses.KEY_UP: 
                self.stdscr.addstr(8, 1, "FORWARD ");
                self.control.setSpeed(-80, -80);
            elif k == 66: #curses.KEY_DOWN: 
                self.stdscr.addstr(8, 1, "BACKWARD");
                self.control.setSpeed(80, 80);
            elif k == 67: #curses.KEY_RIGHT: 
                self.stdscr.addstr(8, 1, "RIGHT   ");
                self.control.setSpeed(-80, 80);
            elif k == 68: #curses.KEY_LEFT: 
                self.stdscr.addstr(8, 1, "LEFT    ");
                self.control.setSpeed(80, -80);
            elif k == ord(' '):
                self.stdscr.addstr(8, 1, "STOP    ");
                self.control.idle()


