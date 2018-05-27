# noinspection PyPep8
# noinspection PyArgumentList

"""
AUTO-GENERATED BY `scripts/generate_protocol.py` using `data/browser_protocol.json`
and `data/js_protocol.json` as inputs! Please do not modify this file.
"""

import logging
from typing import Any, Optional, Union

from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from cripy.protocol import runtime as Runtime

# StreamHandle: This is either obtained from another method or specifed as `blob:&lt;uuid&gt;` where`&lt;uuid&gt` is an UUID of a Blob.
StreamHandle = str

class IO(PayloadMixin):
    """ Input/Output operations for streams produced by DevTools.
    """
    @classmethod
    def close(cls,
              handle: Union['StreamHandle'],
              ):
        """Close the stream, discard any temporary backing storage.
        :param handle: Handle of the stream to close.
        :type handle: StreamHandle
        """
        return (
            cls.build_send_payload("close", {
                "handle": handle,
            }),
            None
        )

    @classmethod
    def read(cls,
             handle: Union['StreamHandle'],
             offset: Optional['int'] = None,
             size: Optional['int'] = None,
             ):
        """Read a chunk of the stream
        :param handle: Handle of the stream to read.
        :type handle: StreamHandle
        :param offset: Seek to the specified offset before reading (if not specificed, proceed with offset
following the last read). Some types of streams may only support sequential reads.
        :type offset: int
        :param size: Maximum number of bytes to read (left upon the agent discretion if not specified).
        :type size: int
        """
        return (
            cls.build_send_payload("read", {
                "handle": handle,
                "offset": offset,
                "size": size,
            }),
            cls.convert_payload({
                "base64Encoded": {
                    "class": bool,
                    "optional": True
                },
                "data": {
                    "class": str,
                    "optional": False
                },
                "eof": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def resolveBlob(cls,
                    objectId: Union['Runtime.RemoteObjectId'],
                    ):
        """Return UUID of Blob object specified by a remote object id.
        :param objectId: Object id of a Blob object wrapper.
        :type objectId: Runtime.RemoteObjectId
        """
        return (
            cls.build_send_payload("resolveBlob", {
                "objectId": objectId,
            }),
            cls.convert_payload({
                "uuid": {
                    "class": str,
                    "optional": False
                },
            })
        )

