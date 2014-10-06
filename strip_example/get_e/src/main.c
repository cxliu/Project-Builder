#include <stdio.h>

#include "strip_example.h"
#include "get_e.h"

int main(int argc, char *argv[]) {
	printf("%s %s\n", STRIP_EXAMPLE_TEXT, get_flavour());
#ifdef ROUND
	printf("e to 2 places = %1.2f", E);
#else
	printf("e with default formatting = %f", E);
#endif
	return 0;
}
