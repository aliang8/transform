from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
ident(transform)

print('Original matrix: \n')
print_matrix(transform)

print('Translation matrix by (1,2,3): \n')
print_matrix(make_translate(1,2,3))

print('Scale matrix by (1,2,3): \n')
print_matrix(make_scale(1,2,3))

print('Rotation matrix by 60 degrees about X-axis: \n')
print_matrix(make_rotX(60))

print('Rotation matrix by 60 degrees about Y-axis: \n')
print_matrix(make_rotY(60))

print('Rotation matrix by 60 degrees about Z-axis: \n')
print_matrix(make_rotZ(60))

'''
Diamond 
add_edge(edges,250,100,0,125,250,0)
add_edge(edges,250,100,0,375,250,0)

add_edge(edges,125,250,0,375,250,0)

add_edge(edges,125,250,0,195,315,0)
add_edge(edges,375,250,0,305,315,0)

add_edge(edges,195,315,0,250,100,0)
add_edge(edges,305,315,0,250,100,0)

add_edge(edges,210,250,0,250,315,0)
add_edge(edges,290,250,0,250,315,0)

add_edge(edges,195,315,0,305,315,0)
'''

parse_file( 'script', edges, transform, screen, color )
