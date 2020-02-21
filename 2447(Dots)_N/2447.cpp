#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

void solve(int line, char **n);

int main(void) {
	int line;
	char 	**n;
	scanf_s("%d", &line);
	n = (char**)malloc(sizeof(line) * sizeof(char));//2차원 배열 할당

	for (int i = 0; i < line; i++)
		n[i] = (char*)malloc(sizeof(line) * sizeof(char));

	solve(line, &(*n));//배열 n의 주소 반환

}

void solve(int line, char **n) {
	int i, j, k = 0;

	while (line==3**k){

		
	}
	for (i=0;i<k - 1;i++)
		for (j = 0; j < k**(k - i - 1); j++) {
			if (*(n+i)+j)>3**i+j*(3**(i+1))-1 && *(n + i) + j)<2*3**i+j*(3**(i+1))) // 
				*(*(n+i)+j) = ' ';
			else *(*(n + i) + j) = '*';
		}
}
