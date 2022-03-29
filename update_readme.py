"""
This file updates the README.md file for me everytime I made a new file in the
Easy, Medium, Hard
Folder
"""
from os import listdir
from typing import List


def format_question(lst: List[str]) -> List[str]:
    """Returns the list with the correct format that can be appended into the README.md file
    AND also returns in the correct sorted number order
    """
    new_lst = []

    for question in lst:
        hash_index = question.index('#')
        space_index = question.index(' ')
        number = int(question[hash_index + 1:space_index])
        new_lst.append((number, question))

    new_lst.sort()

    return [f'- \\{s[1]}\n' for s in new_lst]


if __name__ == '__main__':
    easy = format_question(listdir('Easy'))
    medium = format_question(listdir('Medium'))
    hard = format_question(listdir('Hard'))

    # Copy all the content first, then look for the segment of easy, medium, and hard
    # This template file is the file that I've manually inputted up until February 2022.
    with open('README_template.md', 'r') as f:
        contents = f.readlines()

    # Parse content
    easy_index = contents.index('## Easy\n')
    medium_index = contents.index('## Medium\n')
    hard_index = contents.index('## Hard\n')

    # # This plus 2 is so that it goes after the new line character
    contents[hard_index + 2:] = hard
    contents[medium_index + 2:hard_index - 1] = medium
    contents[easy_index + 2:medium_index - 1] = easy

    with open('README.md', 'w') as f:
        f.writelines(contents)
