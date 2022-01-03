# Lee
import csv

"""
Read in socks.csv
"""


def read_socks_csv():
    with open("socks.csv") as f:
        return list(csv.DictReader(f))


socks = read_socks_csv()

"""
Find names of socks with most variations
"""

# Count variations
variation_counts = {}
for sock in socks:
    name = sock["Name"]
    variation_counts[name] = variation_counts.get(name, 0) + 1

# Build list of variation multimodes
most_variations = (0, [])
for sock in variation_counts:
    count = variation_counts[sock]
    if count > most_variations[0]:
        most_variations = (count, [sock])
    elif count == most_variations[0]:
        most_variations[1].append(sock)

print(f"The list of socks with the most variations is {most_variations}.")

"""
Find counts of each color
"""
color_counts = {}
for sock in socks:
    c1 = sock["Color 1"]
    c2 = sock["Color 2"]
    color_counts[c1] = color_counts.get(c1, 0) + 1
    if c1 != c2:
        color_counts[c2] = color_counts.get(c2, 0) + 1

print(f"The counts of socks of each color is: {color_counts}.")


"""
Do it all in one for loop!
"""

# Count variations and colors
counts = {
    "variations": {},
    "colors": {}
}
for sock in socks:
    name = sock["Name"]
    c1 = sock["Color 1"]
    c2 = sock["Color 2"]

    counts["variations"][name] = counts["variations"].get(name, 0) + 1

    counts["colors"][c1] = counts["colors"].get(c1, 0) + 1
    if c1 != c2:
        counts["colors"][c2] = counts["colors"].get(c2, 0) + 1
