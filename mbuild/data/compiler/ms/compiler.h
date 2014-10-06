/**
 * @note  Confidential Information - Limited distribution to authorized persons
 *        only. This material is protected under international copyright laws as
 *        an unpublished work. Do not copy.
 *        Copyright (C) 2004-2009 Dolby Laboratories Inc. All rights reserved.
 *
 */ 

#ifndef COMPILER_H
#define COMPILER_H

#if 0
/* Disable dumb Microsoft warnings about potential buffer overruns */
#ifndef _CRT_SECURE_NO_WARNINGS
#define _CRT_SECURE_NO_WARNINGS
#endif
#ifndef _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_DEPRECATE
#endif
#ifndef _USE_MATH_DEFINES
#define _USE_MATH_DEFINES
#endif

#include <stdlib.h> /* for malloc, etc */
#include <string.h> /* for memset, etc */
#include <assert.h> 
#include <float.h> 
 
#pragma warning(disable : 4514) /* disable warning for unused inlines */
#pragma warning(disable : 4310) /* disable warning for truncation of constants */
#pragma warning(disable : 981)  /* disable warning for unspecified operand order */
#pragma warning(disable : 279)  /* disable warning for constant macros at run time */

#define inline __forceinline

//#define restrict __restrict

/* The alloca (allocate memory from stack) is pretty standard on unix platforms.
 * However, the MSVC CRT calls it _alloca because it's not in the ANSI standard.
 */
#define alloca _alloca

/* Likewise snprintf (secure string printf) is also pretty standard on unix
 * platforms and again the MSVC CRT calls it _snprintf because it's not in
 * the ANSI standard
 */
#define snprintf _snprintf

#define int16_t __int16 
#define int32_t __int32 
#define INT64_TYPE __int64 
#define UINT16_TYPE unsigned __int16 
#define UINT32_TYPE unsigned __int32 
#define UINT64_TYPE unsigned __int64 
#define FLOAT_TYPE float 
#define DOUBLE_TYPE double 

#define PADDED_STRUCT(def) \
struct def

/* Helper to check that a float is not a NaN or a denorm */
static inline
void
DLB_checkF(double x)
{
    const __int64* s = (const __int64*) &x;
    __int64 exponent, fraction;

    exponent = *s & (((1i64<<12) - 1) << 52);
    fraction = *s & ((1i64<<52) - 1);

    /* Check for denormal */
    assert(exponent || !fraction);

    /* Check for NaN/infinity */
    assert(exponent != (2047i64 << 52));
}

/* Show a variable is (possibly) unused */
#define UNUSED(x) (void)x

#define _USE_MATH_DEFINES           /* Bring in maths constants */
#endif
#endif /* COMPILER_H */
