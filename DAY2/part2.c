#include <stdio.h>
int main(void) {
	FILE *input;
	int i, x = 0, y = 0, a = 0;
	char buff[255];
	input = fopen("input.txt", "r");
	while (fscanf(input, "%s %d", &buff, &i)) {
		if (feof(input)) {
			break;
		}
		//printf("%s, %d\n", buff, i);
		if (buff[0] == 'f') {
			x += i;
			y += a*i;
		}
		if (buff[0] == 'd') {
			a += i;
		}
		if (buff[0] == 'u') {
			a -= i;
		}
	}
	//Don't really need a lld but just to be safe since my answer was near
	//the maximum range of int
	printf("%lld\n", x*y);
	return 0;
}
			
			

