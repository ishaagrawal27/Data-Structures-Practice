#
# Simple Data Structures Practice
# 
# This program demonstrates basic operations using:
# 1. Lists
# 2. Dictionaries
# 3. Sets
#
# Problems:
# 1. Word Frequency Counter
# 2. Duplicate Remover
# 3. Student Marks & Average
# 4. Common Elements Between Two Lists
# 


# 
# Problem 1: Word Frequency Counter
#
# Count how many times each word appears in a paragraph.

text = """
Python is a popular programming language.
Python is easy to learn and Python is widely used.
Many students learn Python for data analysis.
Python can also be used for automation and machine learning.
Learning Python requires regular practice.
Practice helps students understand Python better.
Python programming is useful for beginners and professionals.
Students can use Python to solve problems and analyze data.
"""

# Convert the text to lowercase so that
# "Python" and "python" are treated as the same word.
text = text.lower()

# Remove punctuation marks
punctuation = ".,!?;:"
for symbol in punctuation:
    text = text.replace(symbol, "")

# Convert the paragraph into a list of words
words = text.split()

# Dictionary to store word frequency
word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print("=" * 60)
print("PROBLEM 1: WORD FREQUENCY COUNTER")
print("=" * 60)

print("Total number of words:", len(words))
print("\nWord Frequency:")

for word, frequency in sorted(word_frequency.items()):
    print(word, ":", frequency)

print()


# 
# Problem 2: Duplicate Remover
#
# Remove duplicate values from a list using a set.

numbers = [
    12, 25, 18, 30, 45, 12, 56, 25,
    67, 30, 78, 45, 89, 90, 18, 100,
    67, 34, 56, 23, 45, 78, 90, 12,
    34, 100, 25, 67, 89, 30, 56, 23,
    18, 45, 78, 90, 34, 100, 12, 67
]

# Convert the list to a set.
# A set automatically removes duplicate values.
unique_numbers = set(numbers)

# Convert the set back into a sorted list
# so that the output is easier to read.
unique_numbers = sorted(list(unique_numbers))

print("=" * 60)
print("PROBLEM 2: DUPLICATE REMOVER")
print("=" * 60)

print("Original List:")
print(numbers)

print("\nNumber of values in original list:", len(numbers))

print("\nList Without Duplicates:")
print(unique_numbers)

print("\nNumber of unique values:", len(unique_numbers))

print()


# 
# Problem 3: Student Marks & Average
# 
# Store marks of multiple students using a dictionary.
# Calculate the total and average marks for each student.

student_marks = {
    "Aarav": [85, 78, 92, 88, 76],
    "Ananya": [91, 87, 89, 94, 90],
    "Rahul": [72, 68, 75, 80, 74],
    "Priya": [88, 92, 85, 90, 87],
    "Rohan": [65, 70, 68, 72, 75],
    "Sneha": [95, 91, 93, 89, 96],
    "Aditya": [78, 82, 80, 85, 79],
    "Kavya": [90, 88, 92, 86, 91],
    "Arjun": [74, 79, 77, 81, 73],
    "Meera": [86, 84, 89, 91, 88],
    "Vikram": [69, 75, 71, 78, 73],
    "Neha": [93, 95, 90, 92, 94]
}

print("=" * 60)
print("PROBLEM 3: STUDENT MARKS & AVERAGE")
print("=" * 60)

print("Student Performance:\n")

for student, marks in student_marks.items():

    # Calculate total marks
    total_marks = sum(marks)

    # Calculate average marks
    average_marks = total_marks / len(marks)

    print("Student:", student)
    print("Marks:", marks)
    print("Total:", total_marks)
    print("Average:", round(average_marks, 2))
    print("-" * 40)

print()


# 
# Problem 4: Common Elements Between Two Lists
# 
# Find the values that appear in both lists.

list1 = [
    10, 15, 20, 25, 30, 35, 40, 45,
    50, 55, 60, 65, 70, 75, 80, 85,
    90, 95, 100, 105, 110, 115, 120
]

list2 = [
    5, 10, 15, 22, 30, 35, 42, 45,
    50, 58, 60, 65, 72, 75, 80, 88,
    90, 95, 100, 108, 115, 120, 125
]

# Convert both lists into sets
set1 = set(list1)
set2 = set(list2)

# Find common elements using intersection
common_elements = set1.intersection(set2)

print("=" * 60)
print("PROBLEM 4: COMMON ELEMENTS BETWEEN TWO LISTS")
print("=" * 60)

print("List 1:")
print(list1)

print("\nList 2:")
print(list2)

print("\nCommon Elements:")
print(sorted(common_elements))

print("\nNumber of common elements:", len(common_elements))

print()


# 
# End of Program
# 

print("=" * 60)
print("ALL 4 PROBLEMS COMPLETED SUCCESSFULLY")
print("=" * 60)