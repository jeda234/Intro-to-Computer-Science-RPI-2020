"""
HW 5 Fall 2020

Utility functions to access the grid, the start locations and a test
path.

Prof. Chuck Stewart

Here is an overview of the grid file.  Minimal error checking is
performed. 

For each grid there is,

1. The grid itself, one line per row, and the same number of integers
on each line 

2. A line with the word "start_locations" followed an even number of
positive integers giving starting row/col coordinates in the grid.

3. A line with the word "path" followed by an even number of integers
giving row/col locations on a path on the grid.

There is a blank line between each grid.
"""


"""
The grids, start locations and paths are stored in three lists.
These are global variables that are modified when the grid file is
read.  Global variables are used to store information about the data
between function calls that users of the utility do not need to know
about. Programs that students write for CS 1 do not need to use global
variables, so they aren't emphasized in the course.
"""

grids = []
start_locations = []
paths = []
grid_file = "hw5_grids.txt"


def num_grids():
    """  Access and return the number of grids that have been input.
    If the grids have not been input - the global grids list is empty
    - they are input now before the result is returned.
    """
    global grids
    if grids == []:
        read_grids()
    return len(grids)


def get_grid(n):
    """  Access and return the grid n (numbering starts at 1). If the
    grids have not been input - the global grids list is empty - they
    are input now before the result is returned. If the grid number is
    too large or too small an empty list is silently returned. 
    """
    global grids
    if grids == []:
        read_grids()
    if n <= 0 or n > len(grids):
        return []
    else:
        return grids[n-1]


def get_start_locations(n):
    """Access and return the starting locations for grid n (numbering
    starts at 1). If the grids and starting locations have not been
    input - the global list is empty - they are input now before the
    result is returned. If the grid number is too large or too small
    an empty list is silently returned.

    """
    global start_locations
    if start_locations == []:
        read_grids()
    if n <= 0 or n > len(grids):
        return []
    else:
        return start_locations[n-1]


def get_path(n):
    """ Access and return the example path for for grid n (numbering starts
    at 1). If the grids and paths have not been input - the global
    path list is empty - they are input now before the result is
    returned. If the grid number is too large or too small an empty
    list is silently returned.
    """
    global paths
    if paths == []:
        read_grids()
    if n < 0 or n > len(grids):
        return []
    else:
        return paths[n-1]

   
"""
The rest of this file contains internal functions for use in
parsing the grid, paths and locations file.
"""


def clear_all():
    """
    Clear and reset the global lists.
    """
    global grids
    global start_locations
    global paths
    grids = []
    start_locations = []
    paths = []


def skip_to_non_blank(gf):
    """
    Skip over lines in grid file gf containing only whitespace
    character. When a line is returned it is split up first and
    returned as a list. If the file is exhausted, an empty list is
    returned. 
    """
    for line in gf:
        if not line.isspace():
            as_list = line.strip().split()
            return as_list
    empty_list = []
    return empty_list


def all_ints(line_as_list):
    """ Return True if the line (a list of strings) contains only
    positive integers.
    """
    num_ints = sum(v.isdigit() for v in line_as_list)
    return num_ints == len(line_as_list)


def parse_locations(nrows, ncols, expected_string, as_list):
    """  Given a line as a list of strings that should contain a
    string and some number of pairs of locations, convert it to a list
    of pairs of integer tuples. Each tuple should be a pair of
    non-negative integers that are withing the row/column bounds of
    the grid we are working with.
    """
    global grid_file

    #  Make sure the line starts with the string we expect
    if expected_string != as_list[0].lower():
        print("Expected to see '%s' at start of line" % expected_string)
        return None

    #  Strip off the front of the list. The rest should be integers in
    #  pairs. 
    ll = as_list[1:]
    if not all_ints(ll):
        print("Expected integers after", expected_string)
        return None
    elif len(ll) % 2 != 0:
        print("Expected even number of digits after", expected_string)
        return None

    #  After error checking on the types of values in the list,
    #  convert safely to integers.
    ll = [int(v) for v in ll]
    locs = []

    #  For the integers into pairs and check to make sure they are
    #  inside the list.
    for i in range(0, len(ll), 2):
        r, c = ll[i], ll[i+1]
        if r < 0 or r >= nrows or c < 0 or c >= ncols:
            print("Out of range location (%d, %d)" % (r, c))
            print("Has file", grid_file, "been corrupted?")
            return None
        else:
            locs.append((r, c))

    return locs


def read_grids():
    """  Read the grid information storing the results in the three
    global lists.  
    """
    global grids
    global start_locations
    global paths
    global grid_file

    #  Start by opening the grid file which is expected to be sitting
    #  in the current working directory.
    gf = open(grid_file, "r")
    if not gf:
        print("Can't open", grid_file, "to read grids. Please check")
        print("that this file is in the same folder as your code!")
        clear_all()
        return 0

    ngrid = 0
    while True:
        #  Skip over blank lines. If there are no more lines, the
        #  function is done and should return the number of grids.
        as_list = skip_to_non_blank(gf)
        if len(as_list) == 0:
            return ngrid
            break

        # We have a real line, so it is the first row of the next grid.
        if not all_ints(as_list):
            print("Grid line has non integer. Here is the split line")
            print("Has file", grid_file, "been corrupted?")
            clear_all()
            return 0

        # Convert to integers and store.
        as_ints = [int(v) for v in as_list]
        next_grid = [as_ints]

        # Read the rest of the grid, ending when a blank line or a
        # line that starts with a non-digit is reached. Check for
        # irregular size.
        for line in gf:
            as_list = line.strip().split()
            if len(as_list) == 0 or not as_list[0].isdigit():  # reached end of grid
                break
            elif len(as_list) != len(next_grid[-1]):
                print("Irregular rows in grid %d" % (ngrid + 1))
                print("Has file", grid_file, "been corrupted?")
                clear_all()
                return 0
            elif not all_ints(as_list):
                print("Grid line has non integer. Here is the split line")
                print("Has file", grid_file, "been corrupted?")
                clear_all()
                return 0
            else:
                # Convert to integers and store
                as_ints = [int(v) for v in as_list]
                next_grid.append(as_ints)
            as_list = []

        nrows = len(next_grid)
        ncols = len(next_grid[0])

        #  If we have a blank line skip to the next non-blank
        if len(as_list) == 0:
            as_list = skip_to_non_blank(gf)

        #  The line
        locs = parse_locations(nrows, ncols, 'start_locations', as_list)
        if locs is None:
            print("Has file", grid_file, "been corrupted?")
            clear_all()
            return 0

        as_list = skip_to_non_blank(gf)
        path = parse_locations(nrows, ncols, 'path', as_list)
        if not path:
            print("Has file", grid_file, "been corrupted?")
            clear_all()
            return 0

        # Add the grid
        grids.append(next_grid)
        start_locations.append(locs)
        paths.append(path)
        ngrid += 1
