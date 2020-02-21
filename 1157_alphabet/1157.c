#include <stdio.h>
#include <ctype.h>

int main(void){
    char alphabet[100];
    char check[100][2];
    int check_count = 0, temp = 0;

    printf("영어 단어 입력: "); scanf("%s", alphabet);
    
    for(int i = 0;i < 100; i++)
        check[i][1] = 0;

    check[0][0] = alphabet[0];

    for(int i = 0;i < 100; i++){
        if(isalpha(alphabet[i])){
            alphabet[i] = toupper(alphabet[i]);
            for(int j = 0; j <= temp; j++){
                if(check[j][0] == alphabet[i])
                    check[j][1]++;
                if(j == (check_count)){
                    check[j + 1][0] = alphabet[i];
                    check[j + 1][1]++;
                    check_count++;
                }
            }
            temp = check_count;
        }
        else break;
    }


    int max_count = 0;
    char result[50];
    int next = 0;

    for(int i = 0; i < check_count; i++){
        if(max_count < check[i][1]){
            result[next] = check[i][0];
            max_count = check[i][1];
        }
    }
    for(int i = 0; i < check_count; i++){
        if(max_count == check[i][1])
            if(result[next] != check[i][0]){
                result[next + 1] = check[i][0];
                next++;
            }
    }

    printf("가장 많이 입력된 알파벳: %s");
    for(int i = 0; i < next; i++)
        printf("%c", result[i]);
}