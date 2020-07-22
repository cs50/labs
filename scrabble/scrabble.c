#include <cs50.h>
#include <stdio.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int score(string s);

int main(void)
{
    // Get input words from both players
    string p1 = get_string("Player 1: ");
    string p2 = get_string("Player 2: ");

    // Score both words
    int s1 = score(p1);
    int s2 = score(p2);

    // TODO: Print the winner
}

int score(string s)
{
    // TODO: Compute and return score for string
}
