#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // get a string named plaintext
    string plaintext = get_string("plaintext: ");
    
    // output the string
    for (int i = 0; i < strlen(plaintext); i++)
    {
        printf("%c", plaintext[i]);
    }
    
    printf("\n");
}
