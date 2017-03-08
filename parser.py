from display import *
from matrix import *
from draw import *
import time

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 translate: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 yrotate: create an y-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 zrotate: create an z-axis rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 1 argument (theta)
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, edges, transform, screen, color ):
    f = open(fname, 'r')
    tr = transform
    commands = ['line','scale','move','rotate']
    lines =  f.read().splitlines()
    for i in range(len(lines)):
        line = lines[i]
        if line in commands:
            i = lines[i+1].split(" ")
        if line == 'line':
            add_edge(edges,float(i[0]),float(i[1]),float(i[2]),float(i[3]),float(i[4]),float(i[5]))
        elif line == 'ident':
            ident(tr)
        elif line == 'scale':
            s = make_scale(float(i[0]),float(i[1]),float(i[2]))
            matrix_mult(s,tr)
        elif line == 'move':
            t = make_translate(float(i[0]),float(i[1]),float(i[2]))
            matrix_mult(t,tr)
        elif line == 'rotate':
            if i[0] == 'x':
                rot = make_rotX(float(i[1]))
            elif i[0] == 'y':
                rot = make_rotY(float(i[1]))
            else:
                rot = make_rotZ(float(i[1]))
            matrix_mult(rot, tr)
            #tr = normalize(tr)
        elif line == 'apply':
            matrix_mult(transform,edges)
        elif line == 'display':
            clear_screen(screen)
            draw_lines( edges, screen, color )
            display(screen)
            time.sleep(0.2)
        elif line == 'save':
            fname = lines[i+1]
            draw_lines( edges, screen, color )
            save_extension( screen, fname )
        elif line == 'quit':
            f.close()
            exit

'''
def normalize ( matrix ):
    for r in range(len(matrix[0])):
        for c in range(len(matrix)):
            matrix[c][r] = int(round(matrix[c][r]))
    return matrix
'''
