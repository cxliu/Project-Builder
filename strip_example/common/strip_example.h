#if !defined(STRIP_EXAMPLE_H)
#define STRIP_EXAMPLE_H

#include <math.h>

#ifdef DEBUG
#define STRIP_EXAMPLE_TEXT "Debug code..."
#else
#define STRIP_EXAMPLE_TEXT "Release code..."
#endif

#define PI (acos(-1))
#define E (exp(1))

#endif

