#include <stdio.h>
int main(void) {
	FILE *input;
	int x, s;
	long long zc, ac=0, nc[9] = {0};
	s = 256;
	input = fopen("input.txt", "r");
	while (fscanf(input, "%d,", &x) && !feof(input)) {	
		nc[x]++;
	}	
	for (int i=0; i<s; i++) {
		zc = nc[0];
		for (int y=0; y<8; y++) {
			nc[y] = nc[y+1];
		}
		nc[6] += zc;
		nc[8] = zc;
	}
	for (int i=0; i<9; i++) {
		ac += nc[i];
	}
	printf("%lld\n", ac);
	return 0;
	
}

		



