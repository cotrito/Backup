#include "helpers.h"
#include <stdio.h>

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0 ; i < height ; i++)
    {
            for(int j = 0 ; j < width ; j++)
            {
                int b = image[i][j].rgbtBlue;
                int g = image[i][j].rgbtGreen;
                int r = image[i][j].rgbtRed;
                if(b == 255)
                {
                    BYTE *x = &image[i][j].rgbtBlue;
                    BYTE *y = &image[i][j].rgbtGreen;
                    BYTE *z = &image[i][j].rgbtRed;
                    *x = 50;
                    *y = 100;
                    *z = 20;
                }
                //int b2 = image[i][j].rgbtBlue;
                //printf("b: %i ,g: %i ,r: %i   \n", b2,g,r);

            }
    }
}
