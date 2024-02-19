#include <cs50.h>
#include <stdio.h>

int main(void)
{
       int n;
   do
   {
        n = get_int("Height:");
   }
   while(n>8 || n<1);

    for(int i = 0 ; i < n ; i++)
    {
        for (int k =1 ; k <n-i; k++)
        {
            printf(" ");
        }
        for (int j = 0 ; j < i +1 ; j++)
        {
            printf("#");
        }
        printf("  ");
        for (int l = 0 ; l < i +1 ; l++)
        {
            printf("#");
        }
        printf("\n");
    }

}