# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import board
# https://github.com/napolux/paroleitaliane

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    b = board.Board()
    b.init_graph()
    edges = b.generate_edges()
    vertices = b.vertices()

    vertices_sum = 0

    for e1 in vertices:
        for e2 in vertices:
            if e1 != e2:
                paths = b.find_all_paths(e1, e2)
                vertices_sum = vertices_sum + len(paths)
                print("Paths between edges " +  str( e1 ) + " " + str( e2 ) + " found " + str( len(paths) ) + ". Total: " + str(vertices_sum) )


    print( vertices_sum )
