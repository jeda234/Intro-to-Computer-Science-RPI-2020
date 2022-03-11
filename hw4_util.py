"""
Utility functions to support file input and formatted output for HW 4.
Written by: Prof. Chuck Stewart
2020-09-29
"""


def part1_get_top():
    """
    Return a list of strings representing the top 100 passwords.
    These are read from a file that must be in the same folder as this
    utility function.
    """
    fn = "password_list_top_100.txt"
    in_f = open(fn)
    if not in_f:
        print("Can't open", fn)
        print("Is it in the same folder as the file containing your HW 4 code?")
        return []

    common = []
    for line in in_f:
        line = line.strip()
        if len(line) > 0:
            common.append(line)
    return common


MAX_WEEK = 29
NUM_STATES = 52


def part2_get_week(w):
    """
    Return a list of lists of COVID test data for the given week.
    See HW 04 description for formatting details.
    """
    if type(w) != int or w < 1 or w > MAX_WEEK:
        # print('part2_get_week: Week must be a postive integer less than or equal', MAX_WEEK)
        # print('part2_get_week: Returning an empty list')
        return []
        
    in_f = open("prob2_data.csv")
    if not in_f:
        print("Can't open the data file 'prob2_data.csv'.\n"
              "Is it in the same folder as the file containing your HW 4 code?")
        return []

    for _ in range(0, (w-1)*NUM_STATES):
        _ = in_f.readline()

    results = []
    for _ in range(NUM_STATES):
        line = in_f.readline()
        line = line.strip().split(',')
        v = [line[0].strip()] + [int(i) for i in line[1:]]
        results.append(v)

    return results


def print_abbreviations(states):
    """
    Given a list of state abbreviations, output them 10 per line with
    a single space between each. Output a new-line character at the
    end of the 10th, 20th, etc. At the end, output a newline
    character, but only if we did not just do this for the 10th, 20th,
    etc. 
    """
    count = 0
    for s in states:
        count += 1
        if count % 10 == 0:
            print(s)
        else:
            print(s, end=' ')
    if len(states) % 10 != 0:
        print()


if __name__ == "__main__":
    """
    The main program contains some simple testing code.
    """
    words = part1_get_top()
    print("part1_get_top: returned %d passwords" % len(words))
    print("part1_get_top: first five passwords are:", words[:5])
    print("part1_get_top: last five passwords are:", words[-5:])

    print("\n")
    print("part2_get_week(0):", part2_get_week(0))
    print("part2_get_week('1'):", part2_get_week('1'))
    print("part2_get_week(27):", part2_get_week(27))
    print("part2_get_week(3):", part2_get_week(3))

    print("\n")
    states = ["GA", "ND", "DC", "MI", "MN", "MO", "MT", "VT", "NH",
              "RI", "NV"]
    print_abbreviations(states)
    states = ["ME", "AK", "NY", "NJ", "PA", "MD", "TX", "TN", "SD", "FL",
              "NC", "NE", "CO", "CA", "OR", "WA", "WI", "WV", "UT", "PR"]
    print_abbreviations(states)
