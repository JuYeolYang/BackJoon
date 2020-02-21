#include <stdio.h>
int factorial(int n) {
	if (n == 1)
		return 1;
	return n * factorial(n - 1);
}

int main(void) {
	float r_m, r_d;
	int t, mul, div;
	scanf_s("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf_s("%d", &div);
		scanf_s("%d", &mul);
		r_m = factorial(mul);
		r_d = factorial(mul - div);

		printf("%.0f\n",  r_m / r_d);
	}
}