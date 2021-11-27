from django import template
from ..models import LogMetrics, ComparisonMetrics, LogObjectHandler, Log
import json
from helpers.g6_helpers import dfg_dict_to_g6, highlight_nonstandard_activities
from helpers.dfg_helper import convert_dfg_to_dict

register = template.Library()

@register.filter
def get_metrics(log, initial):
    if initial == log:
        return LogMetrics(initial.pm4py_log()).get_metrics()
    else:
        return ComparisonMetrics(initial, log).get_comparison()


@register.filter
def get_graph(log):
    return json.dumps(
        highlight_nonstandard_activities(
            dfg_dict_to_g6(
                convert_dfg_to_dict(
                    LogObjectHandler(log).generate_dfg()))))
