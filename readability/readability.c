#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int book[3];

void book_count(string text);

int main(void)
{
    string text = get_string("Text : ");

    book_count(text);

    float let = book[0];
    float wor = book[1];
    float set = book[2];

    float l = let/wor * 100.00;
    float s =  set/wor * 100.00;
    int grade = round(0.0588 * l - 0.296 * s - 15.8);

    if (grade > 16)
    {
    printf("Grade 16+\n");
    }
    else if(grade < 1)
    {
    printf("Before Grade 1\n");
    }
     else
     {
    printf("Grade %i\n", grade);
     }

}

void book_count(string text)
{
    int le = 0;
    int wo = 0;
    int se = 0;
    for (int i = 0 , n = strlen(text) ; i < n ; i++)
    {
       int val = text[i];

       if(val >64 && val <91 )
       {
            le++;
       }
       else if(val >96 && val <123 )
       {
            le++;
       }
        else if(val  == 32 )
       {
            wo++;
       }
        else if(val  == 46 ||  val  == 33 || val  == 63 )
       {
            se++;
       }
       else
       {
       }
    }
    wo++;
    book[0] = le;
    book[1] = wo;
    book[2] = se;
}