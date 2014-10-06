#include <stdio.h>

#include "strip_example.h"
#include "get_pi.h"

int main(int argc, char *argv[]) {
	printf("%s %s\n", STRIP_EXAMPLE_TEXT, get_flavour());
#if defined(ROUND)
	printf("Pi to 2 places = %1.2f", PI);
#else /* defined(ROUND) */
	printf("Pi with default formatting = %f", PI);
#endif /* defined(ROUND) */
	return 0;
}
