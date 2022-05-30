"""
CSAPX Project 1: Movies

A program that performs queries from the input using the movie, rating, and title type dictionaries.

Author: Jack Schneider
"""


from timeit import default_timer as timer
import sys


def performQueries(movieDict, ratingDict, typeDict):
    """
    Performs the requested query for each line of input.
    :param movieDict: the movie dictionary
    :param ratingDict: the rating dictionary
    :param typeDict: the title type dictionary
    :return: None
    """
    for line in sys.stdin:
        line = line.strip().split(" ")
        query = line[0]
        if query == "LOOKUP":
            lookup(line[1], movieDict, ratingDict)
        elif query == "CONTAINS":
            contains(line[1], str(line[2:]).strip("[").strip("]").replace("'", "").replace(",", ""), typeDict)
        elif query == "YEAR_AND_GENRE":
            year_and_genre(line[1], line[2], line[3], typeDict)
        elif query == "RUNTIME":
            runtime(line[1], line[2], line[3], typeDict)
        elif query == "MOST_VOTES":
            most_votes(line[1], line[2], typeDict, ratingDict, movieDict)
        elif query == "TOP":
            top(line[1], line[2], line[3], line[4], typeDict, ratingDict, movieDict)


def lookup(lookup_tconst, movieDict, ratingDict):
    """
    Looks up and prints a movie and rating by its t constant.
    :param lookup_tconst: the inputted t constant
    :param movieDict: the movie dictionary
    :param ratingDict: the rating dictionary
    :return: None
    """
    print("processing: LOOKUP " + lookup_tconst)
    start = timer()
    currentMovie = movieDict.get(lookup_tconst)
    currentRating = ratingDict.get(lookup_tconst)
    if currentMovie != None and currentRating != None:
        print("\tMOVIE: Identifier: " + movieDict[lookup_tconst].tconst + ", Title: " +
              movieDict[lookup_tconst].primaryTitle + ", Type: " + movieDict[lookup_tconst].titleType +
              ", Year: " + movieDict[lookup_tconst].startYear + ", Runtime: " +
              movieDict[lookup_tconst].runtimeMinutes + ", Genres: " +
              str(movieDict[lookup_tconst].genres).strip("[").strip("]").replace("'", ""))
        print("\tRATING: Identifier: " + ratingDict[lookup_tconst].tconst + ", Rating: " +
              ratingDict[lookup_tconst].averageRating + ", Votes: " + ratingDict[lookup_tconst].numVotes)
    else:
        print("\tMovie not found!")
        print("\tRating not found!")
    print("elapsed time (s): " + str(timer()-start), "\n")



def contains(title_type, title_name, typeDict):
    """
    Prints all movies of the inputted title type that also contain the inputted title name.
    :param title_type: the inputted title type
    :param title_name: the inputted title name
    :param typeDict: the title type dictionary
    :return: None
    """
    print("processing: CONTAINS", title_type, title_name)
    start = timer()
    found = False
    current_type = typeDict.get(title_type)
    if current_type != None:
        for i in range(len(typeDict[title_type])):
            if title_name in typeDict[title_type][i].primaryTitle:
                found = True
                print("\tIdentifier: " + typeDict[title_type][i].tconst + ", Title: " +
                      typeDict[title_type][i].primaryTitle
                      + ", Type: " + typeDict[title_type][i].titleType + ", Year: " +
                      typeDict[title_type][i].startYear
                       + ", Runtime: " + typeDict[title_type][i].runtimeMinutes + ", Genres: " +
                     str(typeDict[title_type][i].genres).strip("[").strip("]").replace("'", ""))
    if not found:
        print("\tNo match found!")
    print("elapsed time (s): " + str(timer() - start), "\n")


def year_and_genre(title_type, year, genre, typeDict):
    """
    Prints all movies of the inputted title type and inputted year that match a genre.
    :param title_type: the inputted title type
    :param year: the inputted year
    :param genre: the inputted genre
    :param typeDict: the title type dictionary
    :return: None
    """
    print("processing: YEAR_AND_GENRE", title_type, year, genre)
    found = False
    start = timer()
    current_type = typeDict.get(title_type)
    alphabet_list = []
    if current_type != None:
        for i in range(len(typeDict[title_type])):
            if year == typeDict[title_type][i].startYear and genre in typeDict[title_type][i].genres:
                found = True
                alphabet_list.append(typeDict[title_type][i])
        alphabet_list.sort(key=lambda a: [a.primaryTitle])
        for obj in alphabet_list:
            print("\tIdentifier: " + obj.tconst + ", Title: " +
                  obj.primaryTitle
                  + ", Type: " + obj.titleType + ", Year: " +
                  obj.startYear
                  + ", Runtime: " + obj.runtimeMinutes + ", Genres: " +
                  str(obj.genres).strip("[").strip("]").replace("'", ""))
    if not found:
        print("\tNo match found!")
    print("elapsed time (s): " + str(timer() - start), "\n")


def runtime(title_type, min_time, max_time,typeDict):
    """
    Prints all movies of the inputted title type that have a runtime within the inputted min and max times.
    :param title_type: the inputted title type
    :param min_time: the inputted minimum time
    :param max_time: the inputted maximum time
    :param typeDict: the title type dictionary
    :return: None
    """
    print("processing: RUNTIME", title_type, min_time, max_time)
    found = False
    start = timer()
    alphabet_list = []
    if typeDict.get(title_type) != None:
        for i in range(len(typeDict[title_type])):
            if int(min_time) <= int(typeDict[title_type][i].runtimeMinutes) <= int(max_time):
                found = True
                alphabet_list.append(typeDict[title_type][i])
        alphabet_list.sort(key=lambda a: [a.primaryTitle])
        alphabet_list.sort(key=lambda a: [a.runtimeMinutes], reverse=True)
        for obj in alphabet_list:
            print("\tIdentifier: " + obj.tconst + ", Title: " +
                    obj.primaryTitle
                    + ", Type: " + obj.titleType + ", Year: " +
                    obj.startYear
                    + ", Runtime: " + obj.runtimeMinutes + ", Genres: " +
                    str(obj.genres).strip("[").strip("]").replace("'", ""))
    if not found:
        print("\tNo match found!")
    print("elapsed time (s): " + str(timer() - start), "\n")


def most_votes(title_type, num_results, typeDict, ratingDict, movieDict):
    """
    Prints the given number of movies of the inputted title type from most to least votes.
    :param title_type: the inputted title type
    :param num_results: the requested number of results
    :param typeDict: the title type dictionary
    :param ratingDict: the rating dictionary
    :param movieDict: the movie dictionary
    :return: None
    """
    print("processing: MOST_VOTES", title_type, num_results)
    found = False
    start = timer()
    votes_list = []
    if typeDict.get(title_type) != None:
        for i in range(len(typeDict[title_type])):
            if ratingDict.get(typeDict[title_type][i].tconst) != None:
                votes_list.append(ratingDict[typeDict[title_type][i].tconst])
    for i in range(len(votes_list)):
        votes_list[i].numVotes = int(votes_list[i].numVotes)
    votes_list.sort(key=lambda v: [v.numVotes, movieDict.get(v.tconst).primaryTitle], reverse=True)
    for i in range(int(num_results)):
        if i <= len(votes_list)-1:
            found = True
            print("\t" + str(i+1) + ". VOTES: " + str(votes_list[i].numVotes) + ", MOVIE: Identifier: " +
                      movieDict[votes_list[i].tconst].tconst + ", Title: " +
                      movieDict[votes_list[i].tconst].primaryTitle
                      + ", Type: " + movieDict[votes_list[i].tconst].titleType + ", Year: " +
                      movieDict[votes_list[i].tconst].startYear
                      + ", Runtime: " + movieDict[votes_list[i].tconst].runtimeMinutes+ ", Genres: "+
                      str(movieDict[votes_list[i].tconst].genres).strip("[").strip("]").replace("'", ""))
    if not found:
        print("\tNo match found!")
    print("elapsed time (s): " + str(timer() - start), "\n")


def top(title_type, num_results, start_year, end_year, typeDict, ratingDict, movieDict):
    """
    Prints a number of movies of a certain title type that are within a range of years and have at least
    1000 votes, from greatest to least rating.
    :param title_type: the inputted title type
    :param num_results: the requested number of results
    :param start_year: the lowest year in the range
    :param end_year: the highest year in the range
    :param typeDict: the title type dictionary
    :param ratingDict: the rating dictionary
    :param movieDict: the movie dictionary
    :return: None
    """
    print("processing: TOP", title_type, num_results, start_year, end_year)
    start = timer()
    votes_list = []
    if typeDict.get(title_type) != None:
        for i in range(len(typeDict[title_type])):
            if ratingDict.get(typeDict[title_type][i].tconst) != None:
                if int(ratingDict[typeDict[title_type][i].tconst].numVotes) >= 1000:
                    if int(start_year) <= int(typeDict[title_type][i].startYear) <= int(end_year):
                        votes_list.append(ratingDict[typeDict[title_type][i].tconst])
    for i in range(len(votes_list)):
        votes_list[i].numVotes = int(votes_list[i].numVotes)
    for year in range(int(end_year)-int(start_year)+1):
        print("\tYEAR: " + str(year+int(start_year)))
        year_list = []
        found = False
        for ratingObj in votes_list:
            if movieDict[ratingObj.tconst].startYear == str(year+int(start_year)):
                found = True
                year_list.append(ratingObj)
        if found:
            year_list.sort(key=lambda v: [movieDict.get(v.tconst).primaryTitle])
            year_list.sort(key=lambda v: [v.numVotes], reverse=True)
            year_list.sort(key=lambda v: [v.averageRating], reverse=True)
            for i in range(int(num_results)):
                if i <= len(year_list) - 1:
                    found = True
                    print("\t\t" + str(i + 1) + ". RATING: " + str(year_list[i].averageRating) +
                          ", VOTES: " + str(year_list[i].numVotes) + ", MOVIE: Identifier: " +
                          movieDict[year_list[i].tconst].tconst + ", Title: " +
                          movieDict[year_list[i].tconst].primaryTitle
                          + ", Type: " + movieDict[year_list[i].tconst].titleType + ", Year: " +
                          movieDict[year_list[i].tconst].startYear
                          + ", Runtime: " + movieDict[year_list[i].tconst].runtimeMinutes + ", Genres: " +
                          str(movieDict[year_list[i].tconst].genres).strip("[").strip("]").replace("'", ""))
        else:
            print("\t\tNo match found!")
    print("elapsed time (s): " + str(timer() - start), "\n")
