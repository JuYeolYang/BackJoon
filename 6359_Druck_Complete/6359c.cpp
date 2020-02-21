#include <stdio.h>
#include <malloc.h>

int main(void) {
	int t, n, j, k, count = 0;
	char * room;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%d", &n);
		room = (char*)malloc(sizeof(char) * (n + 1));
		for (j = 1; j <= n; j++) room[j] = 'c'; //c == door close, o == door open
		for (j = 1; j <= n; j++) {
			int q = n / j;
			for (k = 1; k <= q; k++) {
				if (room[j * k] == 'c') room[j * k] = 'o';
				else room[j * k] = 'c';
				printf("%s", room);
			}
		}
		for (j = 1; j <= n; j++) {
			if (room[j] == 'o') count++;
		}
		printf("%d\n", count);
		count = 0;
	}
	return 0;
}