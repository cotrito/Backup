#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

string cipher_text(string word, string key);
bool count_uval(string word);
int dupl_char(string key);

int main(int argc, string argv[])
{

    string ci = argv[1];
    if(argc != 2)
    {
    printf("Usage: ./substitution key\n");
    return 1;
    }
    else if(dupl_char(ci) >0)
    {
    printf("Duplicated characters\n");
    return 1;
    }
    else if(count_uval(ci)== 1)
    {
        if(strlen(ci) != 26)
        {
        printf("Key must contain 26 characters.\n");
        return 1;
        }
        else
        {
        string text = get_string("plaintext:");
        string ct = cipher_text(text,ci);
        printf("ciphertext: %s\n", ct);
        }
    }
    else
    {
        return 1;
    }
}

string cipher_text(string word, string key)
{
        for (int i = 0, n = strlen(word); i < n; i++)
        {
        int val = word[i];
        if(val >64 && val <91 )
        {
        int z =  word[i] - 65;
        word[i] =  toupper(key[z]);
        }
        else if(val >96 && val <123 )
        {
        int z =  word[i] - 97;
            word[i] =  tolower(key[z]);
        }
        else
        {
        }
        }
        return word;
}

bool count_uval(string word)
{
    int su =0;
    int suttl=0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
    int val = toupper(word[i]);
    if(val >64 && val <91)
        {
        su++;
        suttl +=val;
        }
    else
        {

        }

    }
    if (su == 26 && suttl == 2015)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int dupl_char(string key)
{
    int su =0;
    for(int i = 0 , n = strlen(key); i < n; i++)
    {
        int val = key[i];
        for(int j = 0 , m = strlen(key)-i; j < m; j++)
        {
            int val2 =key[i+j+1];
            if(val2 == val)
            {
                su++;
            }
            else
            {

            }
        }

    }
    return su;
}