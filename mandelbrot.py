# Renders the Mandelbrot Set in ASCII art. This version of the code
# runs with Python 3. 
# Claire C.C., 2016
# With special thanks to pjdelport for her help with optimizing.

import curses

ITOCHAR = {5:'@', 4:'O', 3:'*', 2:'.', 1:'`', 0:' '} 

def mandelbrotTest(c):
    ''''Tests to see if a point is is the mandelbrot set, and assigns it
    a character based on how quickly it escaped, if at all.'''

    Z = c
    i = 0
    
    while abs(Z) <= 2:
        if i > 500:
            break
        Z = Z ** 2 + c
        i += 1
    
    return ITOCHAR[i // 100]



def main(stdscr):
    C = curses.COLS
    R = curses.LINES

    X = C - 1 if C % 2 == 0 else C    # Resolution. Should be an odd number.
    Y = R - 1 if R % 2 == 0 else R
    
    xMid = X // 2  # This represents the axes on a complex plane.
    yMid = Y // 2
    
    dx = 2 / xMid  # How much each cell represents in the context 
    dy = 2 / yMid  # of the complex plane.
   
    stdscr.clear()
    stdscr.refresh()
    
    for row in range(Y):
        for col in range(X):
            x, y = (-2 + dx * col), (2 - dy * row)
            c = complex(x, y)
            stdscr.addstr(row, col, mandelbrotTest(c))
        stdscr.refresh()
    
    stdscr.getkey()


if __name__ == "__main__":
    curses.wrapper(main)
