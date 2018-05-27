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

# Metric: Run-time execution metric.
class Metric(ChromeTypeBase):
    def __init__(self,
                 name: Union['str'],
                 value: Union['float'],
                 ):

        self.name = name
        self.value = value


class Performance(PayloadMixin):
    """ 
    """
    @classmethod
    def disable(cls):
        """Disable collecting and reporting metrics.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def enable(cls):
        """Enable collecting and reporting metrics.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def getMetrics(cls):
        """Retrieve current values of run-time metrics.
        """
        return (
            cls.build_send_payload("getMetrics", {
            }),
            cls.convert_payload({
                "metrics": {
                    "class": [Metric],
                    "optional": False
                },
            })
        )



class MetricsEvent(BaseEvent):

    js_name = 'Performance.metrics'
    hashable = []
    is_hashable = False

    def __init__(self,
                 metrics: Union['[Metric]', dict],
                 title: Union['str', dict],
                 ):
        if isinstance(metrics, dict):
            metrics = [Metric](**metrics)
        elif isinstance(metrics, list):
            metrics = [Metric(**item) for item in metrics]
        self.metrics = metrics
        if isinstance(title, dict):
            title = str(**title)
        elif isinstance(title, list):
            title = [str(**item) for item in title]
        self.title = title

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')
