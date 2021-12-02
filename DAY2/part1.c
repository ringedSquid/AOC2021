#include <stdio.h>
int main(void) {
	FILE *input;
	int i, x = 0, y = 0;
	char buff[255];
	input = fopen("input.txt", "r");
	while (fscanf(input, "%s %d", &buff, &i)) {
		if (feof(input)) {
			break;
		}
		//printf("%s, %d\n", buff, i);
		if (buff[0] == 'f') {
			x += i;
		}
		if (buff[0] == 'd') {
			y += i;
		}
		if (buff[0] == 'u') {
			y -= i;
		}
	}
	printf("%d\n", x*y);
	return 0;
}
			
			

