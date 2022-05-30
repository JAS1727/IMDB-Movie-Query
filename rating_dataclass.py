"""
CSAPX Project 1: Movies

A program that creates the Rating dataclass.

Author: Jack Schneider
"""


from dataclasses import dataclass


@dataclass
class Rating:
    """A dataclass to represent a rating"""
    tconst: str
    averageRating: str
    numVotes: str
