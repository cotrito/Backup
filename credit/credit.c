#include <cs50.h>
#include <stdio.h>

int get_lenght(long n);
int get_brand(int n , long cred);
int get_valid(long cred);

int main(void)
{
    long cred = get_long("credit card number :");
    int len = get_lenght(cred);
    int brand = get_brand(len, cred);
    int fin = get_valid(cred);
    if (fin == 0)
    {
        if (brand == 1)
        {
            printf("VISA\n");
        }
        else if (brand == 2)
        {
            printf("AMEX\n");
        }
        else if (brand == 3)
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

int get_lenght(long n)
{

    int count = 0;
    do
    {
        n/=10;
        ++count;
    }
    while (n != 0);
    return count;
}

int get_brand(int n , long cred)
{
    if (n == 13)
    {
        int sd = cred/1000000000000;
        if (sd == 4)
        {
            return 1;
        }
        else
        {
            return 0;
        }

    }
    else if (n == 15)
    {
        int sd = cred/10000000000000;
        if (sd == 34)
        {
            return 2;
        }
        else if (sd == 37)
        {
            return 2;
        }
        else
        {
            return 0;
        }
    }
    else if (n == 16)
    {
        int sd = cred/100000000000000;
        int sdd = cred/1000000000000000;
        if (sdd == 4)
        {
            return 1;
        }
        else if (sd < 56 && sd >50)
        {
            return 3;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        return 0;
    }
}
int get_valid(long cred)
{
    int su = 0;
    int sum = 0;
    long cre = cred;
    cred/=10;
    do
    {
        int n = cred%10;
        n*=2;
        cred/=100;

        do
        {
            su = su + n%10;
            n/=10;
        }
        while (n != 0);

    }
    while (cred != 0);
    do
    {
        int l = cre%10;
        sum+=l;
        cre/=100;
    }
    while (cre != 0);
    int fin = (sum+su)%10;
    return fin;

}