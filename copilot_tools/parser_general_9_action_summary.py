import os
import sys
from collections import OrderedDict

from copilot_tools.parser_0920_summary import Parser0920Summary
from copilot_front_end.pu_frontend_executor import step_api_to_frontend_action
current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)
sys.path.append(current_dir)

class ParserGeneral9actionSummary(Parser0920Summary):

    def str2action(self, json_str):

        actions = json_str['actions']
        action_part = actions[0]
        args_part = action_part['args']
        action = OrderedDict()
        # action = step_api_to_frontend_action(action_part)
        action['cot'] = ""
        action['action'] = action_part['action_type'].upper()
        if "SCROLL" == action['action']:
            action['action'] = "SLIDE"
        if "POP" == action['action']:
            action['action'] = "INFO"
        action['action_type'] = action['action']
        action['summary'] = action_part['reasoning']
        action['explain'] = action_part['reasoning']
        if "text" in args_part:
            action['value'] = args_part['text']
        if "duration" in args_part:
            action['value'] = args_part['duration']
            action['seconds'] = args_part['duration']
        if "normalized_point" in args_part:
            point_part = args_part['normalized_point']
            x = point_part[0] * 1000
            y = point_part[1] * 1000
            action['point'] = [x, y]
        if "normalized_path" in args_part:
            path_part = args_part['normalized_path']
            x1 = path_part[0][0] * 1000
            y1 = path_part[0][1] * 1000
            x2 = path_part[1][0] * 1000
            y2 = path_part[1][1] * 1000
            action['point1'] = [x1, y1]
            action['point2'] = [x2, y2]
        # ordered_action = OrderedDict(action)
        return action
            
