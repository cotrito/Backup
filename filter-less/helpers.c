#include "helpers.h"
#include <stdio.h>
#include<math.h>
#include <stdlib.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
      for(int i = 0 ; i < height ; i++)
    {
            for(int j = 0 ; j < width ; j++)
            {
                int b = image[i][j].rgbtBlue;
                int g = image[i][j].rgbtGreen;
                int r = image[i][j].rgbtRed;
                int grey = round((b*1.00 + g*1.00 + r*1.00)/3);
                BYTE *x = &image[i][j].rgbtBlue;
                BYTE *y = &image[i][j].rgbtGreen;
                BYTE *z = &image[i][j].rgbtRed;
                *x = grey;
                *y = grey;
                *z = grey;
            }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
        for(int i = 0 ; i < height ; i++)
    {
            for(int j = 0 ; j < width ; j++)
            {
                int originalBlue = image[i][j].rgbtBlue;
                int originalGreen = image[i][j].rgbtGreen;
                int originalRed = image[i][j].rgbtRed;

                int sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
                int sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
                int sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);

                if(sepiaRed >255)
                {
                    sepiaRed =255;
                }
                if(sepiaGreen >255)
                {
                    sepiaGreen =255;
                }
                if(sepiaBlue >255)
                {
                    sepiaBlue =255;
                }

                BYTE *x = &image[i][j].rgbtBlue;
                BYTE *y = &image[i][j].rgbtGreen;
                BYTE *z = &image[i][j].rgbtRed;

                *x = sepiaBlue;
                *y = sepiaGreen;
                *z = sepiaRed;

            }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    RGBTRIPLE copy[height][width];

         for(int i = 0 ; i < height ; i++)
    {
            for(int j = 0 ; j < width ; j++)
            {
                int b = image[i][j].rgbtBlue;
                int g = image[i][j].rgbtGreen;
                int r = image[i][j].rgbtRed;

                //printf("i: %i ,j: %i \n",i,j);

                copy[i][width - j - 1].rgbtBlue = b;
                copy[i][width - j - 1].rgbtGreen = g;
                copy[i][width - j - 1].rgbtRed = r;
            }
    }

    for(int i = 0 ; i < height ; i++)
    {
            for(int j = 0 ; j < width ; j++)
            {
                BYTE *x = &image[i][j].rgbtBlue;
                BYTE *y = &image[i][j].rgbtGreen;
                BYTE *z = &image[i][j].rgbtRed;

                *x = copy[i][j].rgbtBlue;
                *y = copy[i][j].rgbtGreen;
                *z = copy[i][j].rgbtRed;
            }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
        RGBTRIPLE copy[height][width];

         for(int i = 0 ; i < height ; i++)
    {
            for(int j = 0 ; j < width ; j++)
            {
                int b = 0;
                int g = 0;
                int r = 0;
                int t = 0;

                for(int y = -1 ; y < 2 ; y++)
                {
                        for(int x = -1 ; x < 2 ; x++)
                        {
                            //printf("i: %i ,j: %i,y: %i , x: %i  \n",i,j,y,x);
                            //l++;
                            //printf("i+y: %i ,j+x: %i \n",i+y,j+x);
                            if(i+y >=0 && i+y < height && j+x >=0 && j+x < width)
                            {
                                b += image[i+y][j+x].rgbtBlue;
                                g += image[i+y][j+x].rgbtGreen;
                                r += image[i+y][j+x].rgbtRed;
                                t++;
                                //printf("t: %i\n",t);
                                //printf("b: %i ,g: %i,r: %i \n",image[i+y][j+x].rgbtBlue,image[i+y][j+x].rgbtGreen,image[i+y][j+x].rgbtRed);
                            }
                        }
                }

                int bf = round(b*1.00/t*1.00);
                int gf = round(g*1.00/t*1.00);
                int rf = round(r*1.00/t*1.00);
                /*
                printf("\n");
                printf("b: %i ,g: %i,r: %i,t: %i  \n",b,g,r,t);
                printf("b: %i ,g: %i,r: %i  \n",bf,gf,rf);
                printf("\n");
                */
                //return;
                copy[i][j].rgbtBlue = bf;
                copy[i][j].rgbtGreen = gf;
                copy[i][j].rgbtRed = rf;
            }
    }
    for(int i = 0 ; i < height ; i++)
    {
            for(int j = 0 ; j < width ; j++)
            {
                BYTE *x = &image[i][j].rgbtBlue;
                BYTE *y = &image[i][j].rgbtGreen;
                BYTE *z = &image[i][j].rgbtRed;

                *x = copy[i][j].rgbtBlue;
                *y = copy[i][j].rgbtGreen;
                *z = copy[i][j].rgbtRed;
            }
    }
    return;
}
