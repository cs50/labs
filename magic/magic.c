
#include <cs50.h>
#include <stdio.h>  

#define ONE_YEAR 1

int main(void)
{
    // Prompt user for age
    int age = get_int("Enter your age: ");
    
    // My age next year
    printf("Next year I'll be %i years old.\n", 17 + ONE_YEAR);
    
    // My age in 10 years
    printf("In 10 years, I'll be %i!\n", 17 + 10);
    
    // My age in 50 years!
    printf("In 50 years, I'll be %i! Wow!\n", 17 + 50);
}
