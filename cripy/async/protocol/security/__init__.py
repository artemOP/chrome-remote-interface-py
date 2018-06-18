from typing import Any, List, Optional, Union
from cripy.async.protocol.security import events as Events
from cripy.async.protocol.security import types as Types


class Security(object):
    """
    Security
    """

    def __init__(self, chrome):
        self.chrome = chrome

    async def disable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Security.disable")
        return mayberes

    async def enable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Security.enable")
        return mayberes

    async def setIgnoreCertificateErrors(self, ignore: bool) -> Optional[dict]:
        """
        :param ignore: If true, all certificate errors will be ignored.
        :type ignore: bool
        """
        msg_dict = dict()
        if ignore is not None:
            msg_dict["ignore"] = ignore
        mayberes = await self.chrome.send(
            "Security.setIgnoreCertificateErrors", msg_dict
        )
        return mayberes

    async def handleCertificateError(self, eventId: int, action: str) -> Optional[dict]:
        """
        :param eventId: The ID of the event.
        :type eventId: int
        :param action: The action to take on the certificate error.
        :type action: str
        """
        msg_dict = dict()
        if eventId is not None:
            msg_dict["eventId"] = eventId
        if action is not None:
            msg_dict["action"] = action
        mayberes = await self.chrome.send("Security.handleCertificateError", msg_dict)
        return mayberes

    async def setOverrideCertificateErrors(self, override: bool) -> Optional[dict]:
        """
        :param override: If true, certificate errors will be overridden.
        :type override: bool
        """
        msg_dict = dict()
        if override is not None:
            msg_dict["override"] = override
        mayberes = await self.chrome.send(
            "Security.setOverrideCertificateErrors", msg_dict
        )
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS
