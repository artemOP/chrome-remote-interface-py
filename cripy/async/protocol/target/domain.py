from typing import Any, List, Optional, Union
from cripy.async.protocol.target import events as Events
from cripy.async.protocol.target import types as Types

__all__ = ["Target"]


class Target(object):
    """
    Supports additional targets discovery and allows to attach to them.
    """

    events = Events.TARGET_EVENTS_NS

    def __init__(self, chrome):
        """
        Construct a new Target object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def activateTarget(self, targetId: str) -> Optional[dict]:
        """
        Activates (focuses) the target.

        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict['targetId'] = targetId
        mayberes = await self.chrome.send('Target.activateTarget', msg_dict)
        return mayberes

    async def attachToTarget(self, targetId: str) -> Optional[dict]:
        """
        Attaches to the target with given id.

        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict['targetId'] = targetId
        mayberes = await self.chrome.send('Target.attachToTarget', msg_dict)
        res = await mayberes
        return res

    async def closeTarget(self, targetId: str) -> Optional[dict]:
        """
        Closes the target. If the target is a page that gets closed too.

        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict['targetId'] = targetId
        mayberes = await self.chrome.send('Target.closeTarget', msg_dict)
        res = await mayberes
        return res

    async def exposeDevToolsProtocol(self, targetId: str, bindingName: Optional[str] = None) -> Optional[dict]:
        """
        Inject object to the target's main frame that provides a communication
channel with browser target.

Injected object will be available as `window[bindingName]`.

The object has the follwing API:
- `binding.send(json)` - a method to send messages over the remote debugging protocol
- `binding.onmessage = json => handleMessage(json)` - a callback that will be called for the protocol notifications and command responses.

        :param targetId: The targetId
        :type targetId: str
        :param bindingName: Binding name, 'cdp' if not specified.
        :type bindingName: Optional[str]
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict['targetId'] = targetId
        if bindingName is not None:
            msg_dict['bindingName'] = bindingName
        mayberes = await self.chrome.send('Target.exposeDevToolsProtocol', msg_dict)
        return mayberes

    async def createBrowserContext(self) -> Optional[dict]:
        """
        Creates a new empty BrowserContext. Similar to an incognito profile but you can have more than
one.
        """
        mayberes = await self.chrome.send('Target.createBrowserContext')
        res = await mayberes
        return res

    async def getBrowserContexts(self) -> Optional[dict]:
        """
        Returns all browser contexts created with `Target.createBrowserContext` method.
        """
        mayberes = await self.chrome.send('Target.getBrowserContexts')
        res = await mayberes
        return res

    async def createTarget(self, url: str, width: Optional[int] = None, height: Optional[int] = None, browserContextId: Optional[str] = None, enableBeginFrameControl: Optional[bool] = None) -> Optional[dict]:
        """
        Creates a new page.

        :param url: The initial URL the page will be navigated to.
        :type url: str
        :param width: Frame width in DIP (headless chrome only).
        :type width: Optional[int]
        :param height: Frame height in DIP (headless chrome only).
        :type height: Optional[int]
        :param browserContextId: The browser context to create the page in.
        :type browserContextId: Optional[str]
        :param enableBeginFrameControl: Whether BeginFrames for this target will be controlled via DevTools (headless chrome only, not supported on MacOS yet, false by default).
        :type enableBeginFrameControl: Optional[bool]
        """
        msg_dict = dict()
        if url is not None:
            msg_dict['url'] = url
        if width is not None:
            msg_dict['width'] = width
        if height is not None:
            msg_dict['height'] = height
        if browserContextId is not None:
            msg_dict['browserContextId'] = browserContextId
        if enableBeginFrameControl is not None:
            msg_dict['enableBeginFrameControl'] = enableBeginFrameControl
        mayberes = await self.chrome.send('Target.createTarget', msg_dict)
        res = await mayberes
        return res

    async def detachFromTarget(self, sessionId: Optional[str] = None, targetId: Optional[str] = None) -> Optional[dict]:
        """
        Detaches session with given id.

        :param sessionId: Session to detach.
        :type sessionId: Optional[str]
        :param targetId: Deprecated.
        :type targetId: Optional[str]
        """
        msg_dict = dict()
        if sessionId is not None:
            msg_dict['sessionId'] = sessionId
        if targetId is not None:
            msg_dict['targetId'] = targetId
        mayberes = await self.chrome.send('Target.detachFromTarget', msg_dict)
        return mayberes

    async def disposeBrowserContext(self, browserContextId: str) -> Optional[dict]:
        """
        Deletes a BrowserContext. All the belonging pages will be closed without calling their
beforeunload hooks.

        :param browserContextId: The browserContextId
        :type browserContextId: str
        """
        msg_dict = dict()
        if browserContextId is not None:
            msg_dict['browserContextId'] = browserContextId
        mayberes = await self.chrome.send('Target.disposeBrowserContext', msg_dict)
        return mayberes

    async def getTargetInfo(self, targetId: str) -> Optional[dict]:
        """
        Returns information about a target.

        :param targetId: The targetId
        :type targetId: str
        """
        msg_dict = dict()
        if targetId is not None:
            msg_dict['targetId'] = targetId
        mayberes = await self.chrome.send('Target.getTargetInfo', msg_dict)
        res = await mayberes
        res['targetInfo'] = Types.TargetInfo.safe_create(res['targetInfo'])
        return res

    async def getTargets(self) -> Optional[dict]:
        """
        Retrieves a list of available targets.
        """
        mayberes = await self.chrome.send('Target.getTargets')
        res = await mayberes
        res['targetInfos'] = Types.TargetInfo.safe_create_from_list(res['targetInfos'])
        return res

    async def sendMessageToTarget(self, message: str, sessionId: Optional[str] = None, targetId: Optional[str] = None) -> Optional[dict]:
        """
        Sends protocol message over session with given id.

        :param message: The message
        :type message: str
        :param sessionId: Identifier of the session.
        :type sessionId: Optional[str]
        :param targetId: Deprecated.
        :type targetId: Optional[str]
        """
        msg_dict = dict()
        if message is not None:
            msg_dict['message'] = message
        if sessionId is not None:
            msg_dict['sessionId'] = sessionId
        if targetId is not None:
            msg_dict['targetId'] = targetId
        mayberes = await self.chrome.send('Target.sendMessageToTarget', msg_dict)
        return mayberes

    async def setAutoAttach(self, autoAttach: bool, waitForDebuggerOnStart: bool) -> Optional[dict]:
        """
        Controls whether to automatically attach to new targets which are considered to be related to
this one. When turned on, attaches to all existing related targets as well. When turned off,
automatically detaches from all currently attached targets.

        :param autoAttach: Whether to auto-attach to related targets.
        :type autoAttach: bool
        :param waitForDebuggerOnStart: Whether to pause new targets when attaching to them. Use `Runtime.runIfWaitingForDebugger` to run paused targets.
        :type waitForDebuggerOnStart: bool
        """
        msg_dict = dict()
        if autoAttach is not None:
            msg_dict['autoAttach'] = autoAttach
        if waitForDebuggerOnStart is not None:
            msg_dict['waitForDebuggerOnStart'] = waitForDebuggerOnStart
        mayberes = await self.chrome.send('Target.setAutoAttach', msg_dict)
        return mayberes

    async def setDiscoverTargets(self, discover: bool) -> Optional[dict]:
        """
        Controls whether to discover available targets and notify via
`targetCreated/targetInfoChanged/targetDestroyed` events.

        :param discover: Whether to discover available targets.
        :type discover: bool
        """
        msg_dict = dict()
        if discover is not None:
            msg_dict['discover'] = discover
        mayberes = await self.chrome.send('Target.setDiscoverTargets', msg_dict)
        return mayberes

    async def setRemoteLocations(self, locations: List[dict]) -> Optional[dict]:
        """
        Enables target discovery for the specified locations, when `setDiscoverTargets` was set to
`true`.

        :param locations: List of remote locations.
        :type locations: List[dict]
        """
        msg_dict = dict()
        if locations is not None:
            msg_dict['locations'] = locations
        mayberes = await self.chrome.send('Target.setRemoteLocations', msg_dict)
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        """
        Retrieve a dictionary of events emitted by the  domain to their python class

        If  has events this method returns a dictionary of
        fully qualified event name (str) to it python class

        :return: Dictionary of the  domain event classes
        :retype: Optional[dict]
        """
        return Events.TARGET_EVENTS_TO_CLASS
