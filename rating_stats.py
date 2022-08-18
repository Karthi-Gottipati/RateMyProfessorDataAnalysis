"""
File: rating_stats.py
----------------------
This file defines a program that allows a user to calculate
baseline summary statistics about a datafile of professor review
data. 
"""


def calculate_rating_stats(filename):
    """
    This function analyzes the professor review data in the given
    file to calculate the percentage of reviews for both men and
    women that fall in the "high rating" bucket, which is a numerical
    rating that is greater than 3.5.

    The resulting information is printed to the console.
    """
    with open(filename, 'r') as file:
        next(file)
        male_count = 0
        male_hi_count = 0
        female_count = 0
        female_hi_count = 0
        for line in file:
            l = line.split(',')
            if l[1] == "M":
                male_count += 1
                if float(l[0]) > 3.5:
                    male_hi_count += 1
            else:
                female_count += 1
                if float(l[0]) > 3.5:
                    female_hi_count += 1

        male_percent = male_hi_count/male_count*100
        print(male_percent)

        female_percent = female_hi_count/female_count*100
        print(female_percent)

def main():
    # Ask the user to input the name of a file
    filename = input("Which data file would you like to load? ")

    # Calculate review distribution statistics by gender for
    # that file. This function should print out the results of
    # the analysis to the console.
    calculate_rating_stats(filename)


if __name__ == '__main__':
    main()
