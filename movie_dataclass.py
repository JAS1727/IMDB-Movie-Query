"""
CSAPX Project 1: Movies

A program that creates the Movie dataclass.

Author: Jack Schneider
"""


from dataclasses import dataclass


@dataclass
class Movie:
    """A dataclass to represent a movie"""
    tconst: str
    titleType: str
    primaryTitle: str
    originalTitle: str
    isAdult: str
    startYear: str
    endYear: str
    runtimeMinutes: str
    genres: list
