from typing import Any, List, Optional, Union
from cripy.async.protocol.page import types as Page
from cripy.async.protocol.applicationcache import events as Events
from cripy.async.protocol.applicationcache import types as Types


class ApplicationCache(object):

    def __init__(self, chrome):
        self.chrome = chrome

    async def enable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("ApplicationCache.enable")
        return mayberes

    async def getApplicationCacheForFrame(self, frameId: str) -> Optional[dict]:
        """
        :param frameId: Identifier of the frame containing document whose application cache is retrieved.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        mayberes = await self.chrome.send(
            "ApplicationCache.getApplicationCacheForFrame", msg_dict
        )
        res = await mayberes
        res["applicationCache"] = Types.ApplicationCache.safe_create(
            res["applicationCache"]
        )
        return res

    async def getFramesWithManifests(self) -> Optional[dict]:
        mayberes = await self.chrome.send("ApplicationCache.getFramesWithManifests")
        res = await mayberes
        res["frameIds"] = Types.FrameWithManifest.safe_create_from_list(res["frameIds"])
        return res

    async def getManifestForFrame(self, frameId: str) -> Optional[dict]:
        """
        :param frameId: Identifier of the frame containing document whose manifest is retrieved.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        mayberes = await self.chrome.send(
            "ApplicationCache.getManifestForFrame", msg_dict
        )
        res = await mayberes
        return res

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS
