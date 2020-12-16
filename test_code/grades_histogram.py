from tkinter import filedialog

from test_code import grade

a1_filename = filedialog.askopenfilename()
a1_file = open(a1_filename, 'r')

a1_histfilename = filedialog.asksaveasfilename()
a1_histfile = open(a1_histfilename, 'w')

# Read the grades into a list.
grades = grade.read_grades(a1_file)

# Count the grades per range.
range_counts = grade.count_grade_ranges(grades)

# Write the histogram to the file.
grade.write_histogram(range_counts, a1_histfile)

a1_file.close()
a1_histfile.close()
