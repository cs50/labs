#include <stdio.h>
#include <cs50.h>
#include <math.h>

#define BASE 2

// returns true if binary, false if not binary
bool check_binary(int b)
{
    while (b > 0)
    {
        if (b % 10 > 1)
        {
            return false;
        }
        b = b / 10;
    }
    return true;
}

// calculates decimal equivalent of binary number
int bin_to_dec(int b)
{
    // declare a variable to hold decimal value
    int d = 0;

    // iterate through each binary digit
    while (b > 0)
    {
        d += b % 10 * BASE;
        b = b / 10;
    }

    // when loop finishes return decimal value
    return d;
}

int main(void)
{
    int binary = get_int("Enter Binary Number: ");

    if (check_binary(binary) == false)
    {
        printf("Invalid input. Try again!\n");
        return 1;
    }

    int decimal = bin_to_dec(binary);
    printf("%i in binary is %i in decimal\n", binary, decimal);
    return 0;
}
