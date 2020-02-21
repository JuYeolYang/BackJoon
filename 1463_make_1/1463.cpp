#include <stdio.h>

int Number[1000001];	// 인덱스 값이 숫자이다.

int min(int a, int b) {
	return a > b ? b : a;
}

int main(void) {

	int N;
	printf("숫자를 입력하시오: "); scanf("%d", &N);

	Number[1] = 0;	// 1일 때는 횟수는 0이다.

	for (int i = 2; i <= N; i++)
	{
		// i - 1, i/2, i/3 한것 중 가장 작은 값을 대입한다.
		Number[i] = Number[i - 1] + 1;
		if (i % 2 == 0)
			Number[i] = min(Number[i], Number[i / 2] + 1);
		if (i % 3 == 0)
			Number[i] = min(Number[i], Number[i / 3] + 1);
	}

	printf("연산 시행회수 최소값: %d\n", Number[N]);
	return 0;
}
