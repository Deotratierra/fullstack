#ifndef __GET_OS__H_
#define __GET_OS__H_

#ifdef _WIN32  /* Windows */
#define OS "Windows"

double os_version_num();

void os_version_name(double num);

/* __ Windows __ */

#endif

#endif /* __GET_OS__ */
