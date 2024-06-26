"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    """Get a numeric score and display its status"""
    score = float(input("Enter score: "))
    print(determine_status(score))


def determine_status(score):
    """Determine the status of a given score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()


random_score = random.randint(0, 100)
print(f"\nRandom score: {random_score} Status: {determine_status(random_score)}")
