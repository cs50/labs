#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get grade as a number
    int grade = get_int("Enter your grade: ");
                   
    // grades between 90 and 100 get an A                    
    printf("You get an A!\n");
                        
    // grades between 80 and 89 get a B                    
    printf("You get a B!\n");
                        
    // only grades between 70 and 79 get a C                   
    printf("You get a C!\n");  
                        
    // all other need improvement
    printf("You need to work harder to pass this class!\n");                                      
}
