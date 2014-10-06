#include <ctype.h>
#include "example-2/include/get_name.h"

const char *get_name_raw(void);

void get_name(char *buffer, size_t size)
{
    unsigned i;
    const char *raw_name = get_name_raw();
    
    for (i = 0; i < size; i++)
    {
        buffer[i] = GET_NAME_TRANSFORM(raw_name[i]);
        if (buffer[i] == '\0')
        {
            break;
        }
    }
    /* Ensure we are always null terminated */
    buffer[size - 1] = '\0';
}


