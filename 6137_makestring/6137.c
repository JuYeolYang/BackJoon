#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int main(void){
    char Input[100];
    char result[100];
    int len, sp, bp;

    printf("문자열 입력: "); scanf("%s", Input);
    len = strlen(Input);
    sp = 0; bp = len - 1;
    for(int i = 0; i < len; i++){
        if(Input[sp] < Input[bp]){
            result[i] = Input[sp];
            sp++;
        }
        else{
            result[i] = Input[bp];
            bp--;
        }
    }
    printf("새로운 문자열: %s", result);

    return 0;
}