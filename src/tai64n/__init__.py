""" Module to read and convert TAI64(n) hex strings as used by DJBDNS.

    decode_tai64n("hex_string")
        decodes a hex string representing a TAI64(n) external date and returns
        a datetime.datetime object at UTC.
    utc2tai(datetime.datetime.now())
        returns a datetime.datetime object representing TAI from a datetime.datetime
        object at UTC. 
    """
from tai64n import decode_tai64n, utc2tai