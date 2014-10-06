#include "example-2/include/get_name.h"

const char *get_name_raw(void) {
	static char name[] = "unknown";
	return name;
}
