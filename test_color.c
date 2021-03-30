#include <conio.h>
#include <stdio.h>
#include <windows.h>

int main(int argc, char *argv[])
{
    HANDLE hOut;
    hOut = GetStdHandle(STD_OUTPUT_HANDLE);
    int i;
    for (i = 1; i < 255 ; i ++ )
    {
        SetConsoleTextAttribute(hOut, i);
        printf("%3d\t",i);
    }
    printf("\n");
    printf("演示结束");
    return 0;
}
