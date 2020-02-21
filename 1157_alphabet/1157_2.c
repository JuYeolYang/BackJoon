#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void){
    char alpha[100];
    char dict[100][2]; //중복된 알파벳 저장, dict[i][0] = 알파벳 저장, dict[i][1] = 중복 횟수
    //char count_alpha[100];
    int len, next_store = 0;


    printf("알파벳 입력: "); scanf("%s", alpha);
    len = strlen(alpha);

    //dict[i][1] = 0 초기화
    for(int i = 0; i < len; i++){
        dict[i][1] = 0;
        alpha[i] = toupper(alpha[i]);
    }

    for(int i = 0; i < len; i++){
        for(int j = 0; j <= next_store; j++){

            //j가 next_store까지 왔을 때 dict_alpha에 없는 것으로 판단한
            if(j == next_store){
                dict[j][0] = alpha[i];
                dict[j][1]++;
                next_store++;
                break;
            }

            //dict[j][1]이 동일하면 중복 횟수를 1 증가시킨다.
            if(alpha[i] == dict[j][0]){
                dict[j][1]++;
                break;
            }
        }
    }

    int len_dict = next_store;
    char result[50];
    int max = 0, next = 0;
    for(int i = 0; i < len_dict; i++){
        if(max < dict[i][1])
            max = dict[i][1];
    }
    for(int i = 0; i < len_dict; i++){
        if(max == dict[i][1]){
            result[next] = dict[i][0];
            next++;
        }
    }
    printf("가장 많이 중복된 알파벳: ");
    for(int i = 0; i < next; i++){
        printf("%c", result[i]);
    }
}
/*
for(int j = 0; j < next_store + 1; j++){
            if(alpha[i] == dict[j][0])
                dict[j][1]++;
        }

        for(int j = 0; j < next_store + 1; j++){
            if(alpha[i] != dict[j][0]){
                dict[next_store][0] = alpha[i];
                dict[next_store][1]++;
                next_store++;
                break;
            }
        }
*/