from display import *
from draw import *
from parser import parse_file
from matrix import *

screen = new_screen()
color = [50,160,209]
edges = []
transform = new_matrix()
parse_file( 'script', edges, transform, screen, color )
