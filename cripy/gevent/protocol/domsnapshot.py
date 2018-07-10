__all__ = ["DOMSnapshot"]


class DOMSnapshot(object):
    """
    This domain facilitates obtaining document snapshots with DOM, layout, and style information.
    """

    dependencies = ['CSS', 'DOM', 'DOMDebugger', 'Page']

    def __init__(self, chrome):
        """
        Construct a new DOMSnapshot object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    def disable(self):
        """
        Disables DOM snapshot agent for the given page.
        """
        wres = self.chrome.send('DOMSnapshot.disable')
        return wres.get()

    def enable(self):
        """
        Enables DOM snapshot agent for the given page.
        """
        wres = self.chrome.send('DOMSnapshot.enable')
        return wres.get()

    def getSnapshot(self, computedStyleWhitelist, includeEventListeners=None, includePaintOrder=None, includeUserAgentShadowTree=None):
        """
        Returns a document snapshot, including the full DOM tree of the root node (including iframes,
template contents, and imported documents) in a flattened array, as well as layout and
white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
flattened.

        :param computedStyleWhitelist: Whitelist of computed styles to return.
        :type computedStyleWhitelist: List[str]
        :param includeEventListeners: Whether or not to retrieve details of DOM listeners (default false).
        :type includeEventListeners: Optional[bool]
        :param includePaintOrder: Whether to determine and include the paint order index of LayoutTreeNodes (default false).
        :type includePaintOrder: Optional[bool]
        :param includeUserAgentShadowTree: Whether to include UA shadow tree in the snapshot (default false).
        :type includeUserAgentShadowTree: Optional[bool]
        """
        msg_dict = dict()
        if computedStyleWhitelist is not None:
            msg_dict['computedStyleWhitelist'] = computedStyleWhitelist
        if includeEventListeners is not None:
            msg_dict['includeEventListeners'] = includeEventListeners
        if includePaintOrder is not None:
            msg_dict['includePaintOrder'] = includePaintOrder
        if includeUserAgentShadowTree is not None:
            msg_dict['includeUserAgentShadowTree'] = includeUserAgentShadowTree
        wres = self.chrome.send('DOMSnapshot.getSnapshot', msg_dict)
        return wres.get()

