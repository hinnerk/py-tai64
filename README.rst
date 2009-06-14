py-tai64
================

A module to convert hex encoded tai64n to datetime.datetime objects and
to convert between TAI and UTC standard time.


Functions
*********

decode_tai64n - convert 16 or 24 char long hex encoded TAI64(n) to datetime.datetime
tai2utc - convert datetime.datetime TAI to datetime.datetime UTC
utc2tai - convert datetime.datetime UTC to datetime.datetime TAI