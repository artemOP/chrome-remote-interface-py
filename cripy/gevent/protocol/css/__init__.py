from cripy.gevent.protocol.page import types as Page
from cripy.gevent.protocol.dom import types as DOM
from cripy.gevent.protocol.css import events as Events
from cripy.gevent.protocol.css import types as Types

__all__ = ["CSS"] + Events.__all__ + Types.__all__


class CSS(object):
    """
    This domain exposes CSS read/write operations. All CSS objects (stylesheets, rules, and styles)
have an associated `id` used in subsequent operations on the related object. Each object type has
a specific `id` structure, and those are not interchangeable between objects of different kinds.
CSS objects can be loaded using the `get*ForNode()` calls (which accept a DOM node id). A client
can also keep track of stylesheets via the `styleSheetAdded`/`styleSheetRemoved` events and
subsequently load the required stylesheet contents using the `getStyleSheet[Text]()` methods.
    """

    dependencies = ["DOM"]

    def __init__(self, chrome):
        self.chrome = chrome

    def addRule(self, styleSheetId, ruleText, location):
        """
        :param styleSheetId: The css style sheet identifier where a new rule should be inserted.
        :type styleSheetId: str
        :param ruleText: The text of a new rule.
        :type ruleText: str
        :param location: Text position of a new rule in the target style sheet.
        :type location: dict
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict["styleSheetId"] = styleSheetId
        if ruleText is not None:
            msg_dict["ruleText"] = ruleText
        if location is not None:
            msg_dict["location"] = location
        wres = self.chrome.send("CSS.addRule", msg_dict)
        res = wres.get()
        res["rule"] = Types.CSSRule.safe_create(res["rule"])
        return res

    def collectClassNames(self, styleSheetId):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict["styleSheetId"] = styleSheetId
        wres = self.chrome.send("CSS.collectClassNames", msg_dict)
        res = wres.get()
        return res

    def createStyleSheet(self, frameId):
        """
        :param frameId: Identifier of the frame where "via-inspector" stylesheet should be created.
        :type frameId: str
        """
        msg_dict = dict()
        if frameId is not None:
            msg_dict["frameId"] = frameId
        wres = self.chrome.send("CSS.createStyleSheet", msg_dict)
        res = wres.get()
        return res

    def disable(self):
        wres = self.chrome.send("CSS.disable")
        return wres.get()

    def enable(self):
        wres = self.chrome.send("CSS.enable")
        return wres.get()

    def forcePseudoState(self, nodeId, forcedPseudoClasses):
        """
        :param nodeId: The element id for which to force the pseudo state.
        :type nodeId: int
        :param forcedPseudoClasses: Element pseudo classes to force when computing the element's style.
        :type forcedPseudoClasses: List[str]
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        if forcedPseudoClasses is not None:
            msg_dict["forcedPseudoClasses"] = forcedPseudoClasses
        wres = self.chrome.send("CSS.forcePseudoState", msg_dict)
        return wres.get()

    def getBackgroundColors(self, nodeId):
        """
        :param nodeId: Id of the node to get background colors for.
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        wres = self.chrome.send("CSS.getBackgroundColors", msg_dict)
        res = wres.get()
        return res

    def getComputedStyleForNode(self, nodeId):
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        wres = self.chrome.send("CSS.getComputedStyleForNode", msg_dict)
        res = wres.get()
        res["computedStyle"] = Types.CSSComputedStyleProperty.safe_create_from_list(
            res["computedStyle"]
        )
        return res

    def getInlineStylesForNode(self, nodeId):
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        wres = self.chrome.send("CSS.getInlineStylesForNode", msg_dict)
        res = wres.get()
        res["inlineStyle"] = Types.CSSStyle.safe_create(res["inlineStyle"])
        res["attributesStyle"] = Types.CSSStyle.safe_create(res["attributesStyle"])
        return res

    def getMatchedStylesForNode(self, nodeId):
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        wres = self.chrome.send("CSS.getMatchedStylesForNode", msg_dict)
        res = wres.get()
        res["inlineStyle"] = Types.CSSStyle.safe_create(res["inlineStyle"])
        res["attributesStyle"] = Types.CSSStyle.safe_create(res["attributesStyle"])
        res["matchedCSSRules"] = Types.RuleMatch.safe_create_from_list(
            res["matchedCSSRules"]
        )
        res["pseudoElements"] = Types.PseudoElementMatches.safe_create_from_list(
            res["pseudoElements"]
        )
        res["inherited"] = Types.InheritedStyleEntry.safe_create_from_list(
            res["inherited"]
        )
        res["cssKeyframesRules"] = Types.CSSKeyframesRule.safe_create_from_list(
            res["cssKeyframesRules"]
        )
        return res

    def getMediaQueries(self):
        wres = self.chrome.send("CSS.getMediaQueries")
        res = wres.get()
        res["medias"] = Types.CSSMedia.safe_create_from_list(res["medias"])
        return res

    def getPlatformFontsForNode(self, nodeId):
        """
        :param nodeId: The nodeId
        :type nodeId: int
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        wres = self.chrome.send("CSS.getPlatformFontsForNode", msg_dict)
        res = wres.get()
        res["fonts"] = Types.PlatformFontUsage.safe_create_from_list(res["fonts"])
        return res

    def getStyleSheetText(self, styleSheetId):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict["styleSheetId"] = styleSheetId
        wres = self.chrome.send("CSS.getStyleSheetText", msg_dict)
        res = wres.get()
        return res

    def setEffectivePropertyValueForNode(self, nodeId, propertyName, value):
        """
        :param nodeId: The element id for which to set property.
        :type nodeId: int
        :param propertyName: The propertyName
        :type propertyName: str
        :param value: The value
        :type value: str
        """
        msg_dict = dict()
        if nodeId is not None:
            msg_dict["nodeId"] = nodeId
        if propertyName is not None:
            msg_dict["propertyName"] = propertyName
        if value is not None:
            msg_dict["value"] = value
        wres = self.chrome.send("CSS.setEffectivePropertyValueForNode", msg_dict)
        return wres.get()

    def setKeyframeKey(self, styleSheetId, range, keyText):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param range: The range
        :type range: dict
        :param keyText: The keyText
        :type keyText: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict["styleSheetId"] = styleSheetId
        if range is not None:
            msg_dict["range"] = range
        if keyText is not None:
            msg_dict["keyText"] = keyText
        wres = self.chrome.send("CSS.setKeyframeKey", msg_dict)
        res = wres.get()
        res["keyText"] = Types.Value.safe_create(res["keyText"])
        return res

    def setMediaText(self, styleSheetId, range, text):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param range: The range
        :type range: dict
        :param text: The text
        :type text: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict["styleSheetId"] = styleSheetId
        if range is not None:
            msg_dict["range"] = range
        if text is not None:
            msg_dict["text"] = text
        wres = self.chrome.send("CSS.setMediaText", msg_dict)
        res = wres.get()
        res["media"] = Types.CSSMedia.safe_create(res["media"])
        return res

    def setRuleSelector(self, styleSheetId, range, selector):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param range: The range
        :type range: dict
        :param selector: The selector
        :type selector: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict["styleSheetId"] = styleSheetId
        if range is not None:
            msg_dict["range"] = range
        if selector is not None:
            msg_dict["selector"] = selector
        wres = self.chrome.send("CSS.setRuleSelector", msg_dict)
        res = wres.get()
        res["selectorList"] = Types.SelectorList.safe_create(res["selectorList"])
        return res

    def setStyleSheetText(self, styleSheetId, text):
        """
        :param styleSheetId: The styleSheetId
        :type styleSheetId: str
        :param text: The text
        :type text: str
        """
        msg_dict = dict()
        if styleSheetId is not None:
            msg_dict["styleSheetId"] = styleSheetId
        if text is not None:
            msg_dict["text"] = text
        wres = self.chrome.send("CSS.setStyleSheetText", msg_dict)
        res = wres.get()
        return res

    def setStyleTexts(self, edits):
        """
        :param edits: The edits
        :type edits: List[dict]
        """
        msg_dict = dict()
        if edits is not None:
            msg_dict["edits"] = edits
        wres = self.chrome.send("CSS.setStyleTexts", msg_dict)
        res = wres.get()
        res["styles"] = Types.CSSStyle.safe_create_from_list(res["styles"])
        return res

    def startRuleUsageTracking(self):
        wres = self.chrome.send("CSS.startRuleUsageTracking")
        return wres.get()

    def stopRuleUsageTracking(self):
        wres = self.chrome.send("CSS.stopRuleUsageTracking")
        res = wres.get()
        res["ruleUsage"] = Types.RuleUsage.safe_create_from_list(res["ruleUsage"])
        return res

    def takeCoverageDelta(self):
        wres = self.chrome.send("CSS.takeCoverageDelta")
        res = wres.get()
        res["coverage"] = Types.RuleUsage.safe_create_from_list(res["coverage"])
        return res

    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
