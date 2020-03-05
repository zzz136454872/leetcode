#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char * convert(char * s, int numRows){
    int len=strlen(s);
    char *out=(char*)malloc(sizeof(char)*(len+1000));
    if(numRows == 1)
    {
        strcpy(out,s);
        return out;
    }

    char (*tmp)[len] = (char(*)[len])malloc(sizeof(char)*len*numRows);
    int i,j;

    for(i=0;i<numRows;i++)
    {
        for(j=0;j<len;j++)
            tmp[i][j]=0;
        out[i]=0;
    }

    int loc=0;
    int count=0;
    int row;
    int col;

    for(i=0;i<len;i++)
    {
        loc = i % (2*numRows-2);
        count = i /(2*numRows-2);
        if(loc < numRows)
        {
           tmp[loc][(numRows-1)*count]=s[i];
           //printf("%d, %d, %c\n",loc,(numRows-1)*count,s[i]);
        }
        else
        {
            loc -= numRows;
            row = numRows - 2- loc;
            col=loc+1+(numRows-1)*count;
            tmp[row][col]=s[i];
            //printf("%d, %d, %c\n",row, col, s[i]);
        }
    }
    loc=0;
    
    for(i=0;i<numRows;i++)
    {
        for(j=0;j<len;j++)
        {
            if(tmp[i][j])
            {
                //printf("%c",tmp[i][j]);
                out[loc++]=tmp[i][j];
            }
        }
    }
    free(tmp);
    out[loc]=0;
    return out;
}

int main()
{
    char test[]="A";
    char *out=convert(test,3);
    printf("%s\n",out);
    free(out);
    return 0;
}
