#include <stdio.h>

void hello(char *output)
{

    printf("You are %s.\n",output);

    return;

}

int main(int argc, char *argv[])
{

    int i;

    for(i=1; i<argc; i++){

        hello(argv[i]);
    }

    printf("がんばれ\n");

    return 0;

}