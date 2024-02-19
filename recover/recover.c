#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <sys/stat.h>
#include <stdbool.h>

typedef uint8_t BYTE;

bool file_exists(const char *filename);

int main(int argc, char *argv[])
{

if (argc != 2)
{
    printf("Incorrect number of parameters.\n");
    return 1;
}
else if(file_exists(argv[1]) == false)
{
    printf("file don't exist.\n");
    return 1;
}

 FILE *file = fopen(argv[1], "r");
 BYTE buffer[512];
 int BLOCK_SIZE = 512;
 int blocks = 0;
 int b = 0;
 int f = 0;
 int im = 0;
 char filename[8];
 FILE *img = NULL;

 while (fread(buffer, 1, BLOCK_SIZE, file) == BLOCK_SIZE)
{
    if(buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {
        if(b == 0 && f == 0)
        {

            //printf("Beginning writing file %i \n",im);
            sprintf(filename,"%03i.jpg",im);
            img = fopen(filename,"w");
            fwrite(&buffer,1,BLOCK_SIZE,img);
            b = blocks;
            im++;
        }
        else
        {
            //printf("Ending writing file %i \n",im);
            fclose(img);
            sprintf(filename,"%03i.jpg",im);
            img = fopen(filename,"w");
            fwrite(&buffer,1,BLOCK_SIZE,img);
            f = blocks;
            im++;

        }
            b = blocks;
            f = 0;
    }
    else if (b > 0)
    {
        //printf("writing file %i \n",im);
        fwrite(&buffer,1,BLOCK_SIZE,img);
    }
        blocks++;
}
    fclose(file);
    fclose(img);
}

bool file_exists(const char *filename)
{
    FILE *fp = fopen(filename, "r");
    bool is_exist = false;
    if (fp != NULL)
    {
        is_exist = true;
        fclose(fp); 
    }
    return is_exist;
}
