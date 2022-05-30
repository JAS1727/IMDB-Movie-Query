"""
CSAPX Project 1: Movies

A program that receives large or small datasets of movies and ratings and prints an output
based on the inputted queries.

Author: Jack Schneider
"""


import read_datasets
import process_queries


def main():
    """
    The main program calls the functions to read each piece data into its dictionary, print the total
    movies and ratings, and process each query. These functions are called from their respective
    modules.
    :return: None
    """
    movieDict = read_datasets.readMovies()
    ratingDict = read_datasets.readRatings(movieDict)
    read_datasets.getTotals(movieDict, ratingDict)
    typeDict = read_datasets.createTypeDict(movieDict)
    process_queries.performQueries(movieDict, ratingDict, typeDict)


if __name__ == '__main__':
    main()
