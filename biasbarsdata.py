"""
File: biasbarsdata.py
------------------
Add your comments here
"""

KEY_WOMEN = "W"
KEY_MEN = "M"


def convert_rating_to_index(rating):
    """
    Converts the specified numerical rating into a "bucket"
    index for the three groups of review buckets (low reviews, 
    medium reviews, and high reviews). The rules for this 
    conversion are specified in the assignment handout.

    Input:
        rating (float): The numerical rating associated with 
                        a review

    Output: 
        bucket_index (int): The index of the "bucket" into which 
                          the review falls
    """
    if rating < 2.5:
        index = 0
    elif rating > 3.5:
        index = 2
    else:
        index = 1
    return index



def add_data_for_word(word_data, word, gender, rating):
    if word not in word_data:
        word_data[word] = {
                  KEY_WOMEN: [0, 0, 0],
                  KEY_MEN: [0, 0, 0]
               }


    word_data[word][gender][rating] += 1

def read_file(filename):

    '''
    Open file, loop through every line in the file and every word of the review
    split string on spaces to loop through words
    make sure to index rating and not raw rating
    '''
    word_data = {}
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            l = line.split(',')
            rating = float(l[0])
            rating = convert_rating_to_index(rating)
            gender = l[1]
            text = l[2]
            text_list = text.split(' ')
            for word in text_list:
                word = word.strip()
                add_data_for_word(word_data, word, gender, rating)

    return word_data


def search_words(word_data, target):
    """
    Given a word_data dictionary that stores word frequency information and a target string,
    returns a list of all words in the dictionary that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        word_data (dictionary): a dictionary containing word frequency data
        target (str): a string to look for in the names contained within word_data

    Returns:
        matching_words (List[str]): a list of all words from word_data that contain
                                    the target string
    """

    """
    You fill this in.  Don't forget to remove the 'pass' statement above.
    """
    words_list = []
    target = target.lower()
    for key in word_data.keys():
        if target in key:
            words_list.append(key)
    return words_list

def print_words(word_data):
    """
    (This function is provided for you)
    Given a word_data dictionary, print out all its data, one word per line.
    The words are printed in alphabetical order,
    with the corresponding frequency data displayed in order
    of associated review quality for each gender.

    This code makes use of the sorted function, which is given as input a 
    list of elements and returns a list containing the same elements sorted in
    increasing order. For strings, "increasing" order maps to alphabetical 
    ordering.

    Input:
        word_data (dictionary): a dictionary containing word frequency data organized by gender and rating quality
    """
    for key, value in sorted(word_data.items()):
        print(key, end=" ")
        for gender, counts in sorted(value.items()):
            print(gender, counts, end=" ")
        print("")


def main():
    # (This function is provided for you)
    import sys
    args = sys.argv[1:]

    if len(args) == 0:
        return
    # Two command line forms
    # 1. data_file
    # 2. -search target data_file

    # Assume no search, so filename to read
    # is the first argument
    filename = args[0]

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filename = args[2]  # Update filename to skip first 2 args

    # Read in the data from the file name
    word_data = read_file(filename)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_words(word_data, target)
        for word in search_results:
            print(word)
    else:
        print_words(word_data)


if __name__ == '__main__':
    main()
