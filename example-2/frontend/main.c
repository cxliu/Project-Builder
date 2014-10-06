#include <stdio.h>

#include "example-2/include/get_name.h"
#include "example-2/include/foo.h"

int main(int argc, char *argv[]) {
	char buffer[256];
	
	get_name(buffer, sizeof(buffer));
	
	printf("OS name is %s\n", buffer);
	printf("foo(%d) = %d\n", argc, foo(argc));
	printf("foo_cpp(%d) = %d\n", argc, foo_cpp(argc));
	foo_asm();
	return 0;
}
