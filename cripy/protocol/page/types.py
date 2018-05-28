from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.network import types as Network

# Resource type as it was perceived by the rendering engine.
ResourceType = str

# Unique frame identifier.
FrameId = str

# Unique script identifier.
ScriptIdentifier = str

# Transition type.
TransitionType = str

# Javascript dialog type.
DialogType = str


class Frame(ChromeTypeBase):
    """Information about the Frame on the page."""

    def __init__(self, id: str, loaderId: 'Network.LoaderId', url: str, securityOrigin: str, mimeType: str, parentId: Optional[str] = None, name: Optional[str] = None, unreachableUrl: Optional[str] = None) -> None:
        """
        :param id: Frame unique identifier.
        :type str:
        :param parentId: Parent frame identifier.
        :type str:
        :param loaderId: Identifier of the loader associated with this frame.
        :type Network.LoaderId:
        :param name: Frame's name as specified in the tag.
        :type str:
        :param url: Frame document's URL.
        :type str:
        :param securityOrigin: Frame document's security origin.
        :type str:
        :param mimeType: Frame document's mimeType as determined by the browser.
        :type str:
        :param unreachableUrl: If the frame failed to load, this contains the URL that could not be loaded.
        :type str:
        """
        super().__init__()
        self.id: str = id
        self.parentId: Optional[str] = parentId
        self.loaderId: Network.LoaderId = loaderId
        self.name: Optional[str] = name
        self.url: str = url
        self.securityOrigin: str = securityOrigin
        self.mimeType: str = mimeType
        self.unreachableUrl: Optional[str] = unreachableUrl


class FrameResource(ChromeTypeBase):
    """Information about the Resource on the page."""

    def __init__(self, url: str, type: 'ResourceType', mimeType: str, lastModified: Optional['Network.TimeSinceEpoch'] = None, contentSize: Optional[float] = None, failed: Optional[bool] = None, canceled: Optional[bool] = None) -> None:
        """
        :param url: Resource URL.
        :type str:
        :param type: Type of this resource.
        :type ResourceType:
        :param mimeType: Resource mimeType as determined by the browser.
        :type str:
        :param lastModified: last-modified timestamp as reported by server.
        :type Network.TimeSinceEpoch:
        :param contentSize: Resource content size.
        :type float:
        :param failed: True if the resource failed to load.
        :type bool:
        :param canceled: True if the resource was canceled during loading.
        :type bool:
        """
        super().__init__()
        self.url: str = url
        self.type: ResourceType = type
        self.mimeType: str = mimeType
        self.lastModified: Optional[Network.TimeSinceEpoch] = lastModified
        self.contentSize: Optional[float] = contentSize
        self.failed: Optional[bool] = failed
        self.canceled: Optional[bool] = canceled


class FrameResourceTree(ChromeTypeBase):
    """Information about the Frame hierarchy along with their cached resources."""

    def __init__(self, frame: 'Frame', resources: List['FrameResource'], childFrames: Optional[List['FrameResourceTree']] = None) -> None:
        """
        :param frame: Frame information for this tree item.
        :type Frame:
        :param childFrames: Child frames.
        :type array:
        :param resources: Information about frame resources.
        :type array:
        """
        super().__init__()
        self.frame: Frame = frame
        self.childFrames: Optional[List[FrameResourceTree]] = childFrames
        self.resources: List[FrameResource] = resources


class FrameTree(ChromeTypeBase):
    """Information about the Frame hierarchy."""

    def __init__(self, frame: 'Frame', childFrames: Optional[List['FrameTree']] = None) -> None:
        """
        :param frame: Frame information for this tree item.
        :type Frame:
        :param childFrames: Child frames.
        :type array:
        """
        super().__init__()
        self.frame: Frame = frame
        self.childFrames: Optional[List[FrameTree]] = childFrames


class NavigationEntry(ChromeTypeBase):
    """Navigation history entry."""

    def __init__(self, id: int, url: str, userTypedURL: str, title: str, transitionType: 'TransitionType') -> None:
        """
        :param id: Unique id of the navigation history entry.
        :type int:
        :param url: URL of the navigation history entry.
        :type str:
        :param userTypedURL: URL that the user typed in the url bar.
        :type str:
        :param title: Title of the navigation history entry.
        :type str:
        :param transitionType: Transition type.
        :type TransitionType:
        """
        super().__init__()
        self.id: int = id
        self.url: str = url
        self.userTypedURL: str = userTypedURL
        self.title: str = title
        self.transitionType: TransitionType = transitionType


class ScreencastFrameMetadata(ChromeTypeBase):
    """Screencast frame metadata."""

    def __init__(self, offsetTop: float, pageScaleFactor: float, deviceWidth: float, deviceHeight: float, scrollOffsetX: float, scrollOffsetY: float, timestamp: Optional['Network.TimeSinceEpoch'] = None) -> None:
        """
        :param offsetTop: Top offset in DIP.
        :type float:
        :param pageScaleFactor: Page scale factor.
        :type float:
        :param deviceWidth: Device screen width in DIP.
        :type float:
        :param deviceHeight: Device screen height in DIP.
        :type float:
        :param scrollOffsetX: Position of horizontal scroll in CSS pixels.
        :type float:
        :param scrollOffsetY: Position of vertical scroll in CSS pixels.
        :type float:
        :param timestamp: Frame swap timestamp.
        :type Network.TimeSinceEpoch:
        """
        super().__init__()
        self.offsetTop: float = offsetTop
        self.pageScaleFactor: float = pageScaleFactor
        self.deviceWidth: float = deviceWidth
        self.deviceHeight: float = deviceHeight
        self.scrollOffsetX: float = scrollOffsetX
        self.scrollOffsetY: float = scrollOffsetY
        self.timestamp: Optional[Network.TimeSinceEpoch] = timestamp


class AppManifestError(ChromeTypeBase):
    """Error while paring app manifest."""

    def __init__(self, message: str, critical: int, line: int, column: int) -> None:
        """
        :param message: Error message.
        :type str:
        :param critical: If criticial, this is a non-recoverable parse error.
        :type int:
        :param line: Error line.
        :type int:
        :param column: Error column.
        :type int:
        """
        super().__init__()
        self.message: str = message
        self.critical: int = critical
        self.line: int = line
        self.column: int = column


class LayoutViewport(ChromeTypeBase):
    """Layout viewport position and dimensions."""

    def __init__(self, pageX: int, pageY: int, clientWidth: int, clientHeight: int) -> None:
        """
        :param pageX: Horizontal offset relative to the document (CSS pixels).
        :type int:
        :param pageY: Vertical offset relative to the document (CSS pixels).
        :type int:
        :param clientWidth: Width (CSS pixels), excludes scrollbar if present.
        :type int:
        :param clientHeight: Height (CSS pixels), excludes scrollbar if present.
        :type int:
        """
        super().__init__()
        self.pageX: int = pageX
        self.pageY: int = pageY
        self.clientWidth: int = clientWidth
        self.clientHeight: int = clientHeight


class VisualViewport(ChromeTypeBase):
    """Visual viewport position, dimensions, and scale."""

    def __init__(self, offsetX: float, offsetY: float, pageX: float, pageY: float, clientWidth: float, clientHeight: float, scale: float) -> None:
        """
        :param offsetX: Horizontal offset relative to the layout viewport (CSS pixels).
        :type float:
        :param offsetY: Vertical offset relative to the layout viewport (CSS pixels).
        :type float:
        :param pageX: Horizontal offset relative to the document (CSS pixels).
        :type float:
        :param pageY: Vertical offset relative to the document (CSS pixels).
        :type float:
        :param clientWidth: Width (CSS pixels), excludes scrollbar if present.
        :type float:
        :param clientHeight: Height (CSS pixels), excludes scrollbar if present.
        :type float:
        :param scale: Scale relative to the ideal viewport (size at width=device-width).
        :type float:
        """
        super().__init__()
        self.offsetX: float = offsetX
        self.offsetY: float = offsetY
        self.pageX: float = pageX
        self.pageY: float = pageY
        self.clientWidth: float = clientWidth
        self.clientHeight: float = clientHeight
        self.scale: float = scale


class Viewport(ChromeTypeBase):
    """Viewport for capturing screenshot."""

    def __init__(self, x: float, y: float, width: float, height: float, scale: float) -> None:
        """
        :param x: X offset in CSS pixels.
        :type float:
        :param y: Y offset in CSS pixels
        :type float:
        :param width: Rectangle width in CSS pixels
        :type float:
        :param height: Rectangle height in CSS pixels
        :type float:
        :param scale: Page scale factor.
        :type float:
        """
        super().__init__()
        self.x: float = x
        self.y: float = y
        self.width: float = width
        self.height: float = height
        self.scale: float = scale

