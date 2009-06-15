========
py-tai64
========

A module to convert a hex encoded tai64n string to a datetime.datetime object and
to convert between TAI and UTC standard time.


TAI, TAI64, TAI64n
==================

    TAI stands for Temps Atomique International, the current international real-time standard. One TAI second is defined as the duration of 9192631770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the cesium atom.

http://cr.yp.to/libtai/tai64.html#tai64n


Module Functions
================

``decode_tai64n("400000004a3239350292c294")``
    converts a 16 or 24 bytes long hex TAI64(n) string to a datetime.datetime UTC object
``utc2tai(datetime.datetime.now())``
    converts datetime.datetime UTC object to a datetime.datetime TAI object