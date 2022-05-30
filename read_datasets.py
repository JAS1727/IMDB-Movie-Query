"""
CSAPX Project 1: Movies

A program that reads either small or large datasets into their respective movie, rating, and type dictionaries.

Author: Jack Schneider
"""


from timeit import default_timer as timer
import sys
from movie_dataclass import Movie
from rating_dataclass import Rating


def readMovies():
    """
    Reads movies from either the small or large movie dataset into a movie dictionary.
    :return: the movie dictionary
    """
    movieDict = {}
    if len(sys.argv) == 2:
        print("reading data/small.basics.tsv into dict...")
        start = timer()
        with open("data/small.basics.tsv", encoding="utf-8") as f:
            f.readline()
            for line in f:
                line = line.strip().split("\t")
                if int(line[4]) == 0:
                    for i in range(0,len(line)-1):
                        if line[i] == "\\N":
                            line[i] = "0"
                    movieDict[line[0]] = Movie(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],
                                               line[8].split(","))
    else:
        print("reading data/title.basics.tsv into dict...")
        start = timer()
        with open("data/title.basics.tsv", encoding="utf-8") as f:
            f.readline()
            for line in f:
                line = line.strip().split("\t")
                if int(line[4]) == 0:
                    for i in range(0, len(line)):
                        if line[i] == "\\N":
                            if i == 8:
                                line[i] = "None"
                            else:
                                line[i] = "0"
                    movieDict[line[0]] = Movie(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],
                                               line[8].split(","))
    stop = timer()
    print("elapsed time (s): " + str(stop-start), "\n")
    return movieDict


def readRatings(movieDict):
    """
    Reads ratings that have a corresponding movie from either the small or large ratings dataset into
    a rating dictionary.
    :param movieDict: the movie dictionary
    :return: the rating dictionary
    """
    ratingDict = {}
    if len(sys.argv) == 2:
        print("reading data/small.ratings.tsv into dict...")
        start = timer()
        with open("data/small.ratings.tsv", encoding="utf-8") as f:
            f.readline()
            for line in f:
                line = line.strip().split("\t")
                if line[0] in movieDict:
                    ratingDict[line[0]] = Rating(line[0],line[1],line[2])
    else:
        print("reading data/title.ratings.tsv into dict...")
        start = timer()
        with open("data/title.ratings.tsv", encoding="utf-8") as f:
            f.readline()
            for line in f:
                line = line.strip().split("\t")
                if line[0] in movieDict:
                    ratingDict[line[0]] = Rating(line[0],line[1],line[2])
    stop = timer()
    print("elapsed time (s): " + str(stop-start), "\n")
    return ratingDict


def getTotals(movieDict, ratingDict):
    """
    Prints the total movies and ratings.
    :param movieDict: the movie dictionary
    :param ratingDict:the rating dictionary
    :return: None
    """
    print("Total movies: " + str(len(movieDict)))
    print("Total ratings: " + str(len(ratingDict)), "\n")


def createTypeDict(movieDict):
    """
    Creates a dictionary with title types for keys and a list of movie objects
    of the movie type for values.
    :param movieDict: the movie dictionary
    :return: the title type dictionary
    """
    typeDict = {}
    for key in movieDict:
        if typeDict.get(movieDict[key].titleType):
            # appends a movie object to its corresponding list value
            typeDict[movieDict[key].titleType].append(movieDict[key])
        else:
            # creates a list of movie objects as a value for each type key in typeDict
            typeDict[movieDict[key].titleType] = [movieDict[key]]
    return typeDict
