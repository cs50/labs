#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // get two strings
    char *s = get_string("s: ");
    char *t = get_string("t: ");

    // compare strings' addresses
    if (s == t)
    {
        printf("same\n");
    }
    else
    {
        printf("not same\n");
    }
}

