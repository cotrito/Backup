// Implements a dictionary's functionality}
#include <string.h>
#include <strings.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>


#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

//total number of words aded from diccionary
int total = 0;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false (4)
bool check(const char *word)
{
    // TODO
    int p = hash(word);
    //node *cn = malloc(sizeof(node));
    node *cn = table[p];

    while (cn != NULL)
    {
        // compare 2 words case insensitive strcasecmp
        if(strcasecmp(cn -> word, word) == 0)
        {
            return true;
        }
        else
        {
            cn = cn -> next;
        }
    }

    return false;
}

// Hashes word to a number (2)
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false (1)
bool load(const char *dictionary)
{
    // TODO
        //open file
    //char *text = (argc == 3) ? argv[2] : argv[1];
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        printf("Could not open %s.\n", dictionary);
        return false;
    }
    //read strings from file
    char wr[45];
    while (fscanf(file, "%s", wr) != EOF){
        //printf("%s\n", wr);
        //hash word
        int p = hash(wr);
        //printf("%i\n", p);
        // create new node
        node *n = malloc(sizeof(node));
        total ++;
        strcpy(n -> word, wr);
        n -> next = NULL;
        //insert new node
            //check if first node is empty
            if (table[p] == NULL)
            {
            table[p] = n ;
            }
            else
            {
            // set the nex node from new node to the first node
            n->next = table[p];
            // set nex node from first element to new node
            table[p] = n ;
            }


    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded (3)
unsigned int size(void)
{
    // TODO
    //printf("number of words %i\n",total);
    return total;
}

// Unloads dictionary from memory, returning true if successful, else false (5)
bool unload(void)
{
    // TODO
    for(int i = 0 ; i < N ; i++)
    {
        node *tmp = table[i];
        node *nex = table[i];
        while(nex != NULL)
        {
            nex = nex -> next;
            free(tmp);
            tmp = nex;
        }
    }

    return true;
}
