#include <math.h>
#include "strip_example.h"
#include "get_e.h"

#ifdef DEBUG
#define LOG_LEVEL 2
#else
#define LOG_LEVEL 0
#endif

#ifdef OSX
#define GUI_STYLE "cocoa"
#else
#define GUI_STYLE "xfree86"
#endif

#ifdef ARM
#define ARM_STUFF 1
#else
#define ARM_STUFF 0
#endif

double get_e(void) {
	return E;
}
