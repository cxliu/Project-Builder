#include "helloworld.h"

const char *helloworld_get_greeting(void)
{
	static const char hello_world[] = "Hello world";
	return hello_world;
}

