#!/usr/bin/env python3
import json
import sys

tools = """[{'name': 'click', 'parameters': {'type': 'object', 'properties': {'button': {'type': 'string', 'description': 'Button to click. Defaults to \"left\".'}, 'x': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'description': 'X coordinate to move to, if not provided it will click on current location. Defaults to None.'}, 'y': {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'description': 'Y coordinate to move to, if not provided it will click on current location. Defaults to None.'}}, 'required': []}, 'description': 'Click mouse button'}, {'name': 'double_click', 'parameters': {'type': 'object', 'properties': {}, 'required': []}, 'description': 'Double click the mouse'}, {'name': 'drag_mouse', 'parameters': {'type': 'object', 'properties': {'x': {'type': 'integer', 'description': 'x coordinate'}, 'y': {'type': 'integer', 'description': 'y coordinate'}}, 'required': ['x', 'y']}, 'description': 'Drag the mouse'}, {'name': 'exec', 'parameters': {'type': 'object', 'properties': {'cmd': {'type': 'string', 'description': 'Command to execute'}}, 'required': ['cmd']}, 'description': 'Execute a command'}, {'name': 'hot_key', 'parameters': {'type': 'object', 'properties': {'keys': {'type': 'array', 'items': {'type': 'string'}, 'description': 'Which keys to press. Options are:\\n[ \"\\\\t\", \"\\\\n\", \"\\\\r\", \" \", \"!\", \\'\\\\\"\\', \"\\\\#\", \"\\\\$\", \"\\\\%\", \"\\\\&\", \"\\\\\\'\",\\n\"\\\\(\", \"\\\\)\", \"\\\\*\", \"\\\\+\", \",\", \"-\", \"\\\\.\", \"/\", \"0\", \"1\", \"2\", \"3\",\\n\"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \":\", \";\", \"<\", \"=\", \">\", \"\\\\?\", \"@\",\\n\"\\\\[\", \"\\\\\\\\\", \"\\\\]\", \"\\\\^\", \"\\\\_\", \"\\\\`\", \"a\", \"b\", \"c\", \"d\", \"e\",\\n\"f\", \"g\", \"h\", \"i\", \"j\", \"k\", \"l\", \"m\", \"n\", \"o\", \"p\", \"q\", \"r\", \"s\",\\n\"t\", \"u\", \"v\", \"w\", \"x\", \"y\", \"z\", \"{\", \"|\", \"}\", \"~\", \"accept\", \"add\",\\n\"alt\", \"altleft\", \"altright\", \"apps\", \"backspace\", \"browserback\",\\n\"browserfavorites\", \"browserforward\", \"browserhome\", \"browserrefresh\",\\n\"browsersearch\", \"browserstop\", \"capslock\", \"clear\", \"convert\", \"ctrl\",\\n\"ctrlleft\", \"ctrlright\", \"decimal\", \"del\", \"delete\", \"divide\", \"down\",\\n\"end\", \"enter\", \"esc\", \"escape\", \"execute\", \"f1\", \"f10\", \"f11\", \"f12\",\\n\"f13\", \"f14\", \"f15\", \"f16\", \"f17\", \"f18\", \"f19\", \"f2\", \"f20\", \"f21\",\\n\"f22\", \"f23\", \"f24\", \"f3\", \"f4\", \"f5\", \"f6\", \"f7\", \"f8\", \"f9\", \"final\",\\n\"fn\", \"help\", \"home\", \"insert\", \"left\", \"numlock\", \"pagedown\", \"pageup\", \"pause\",\\n\"pgdn\", \"pgup\", \"playpause\", \"prevtrack\", \"print\", \"printscreen\",\\n\"prntscrn\", \"prtsc\", \"prtscr\", \"return\", \"right\", \"scrolllock\",\\n\"select\", \"separator\", \"shift\", \"shiftleft\", \"shiftright\", \"sleep\",\\n\"space\", \"stop\", \"subtract\", \"tab\", \"up\", \"volumedown\", \"volumemute\",\\n\"volumeup\", \"win\", \"winleft\", \"winright\", \"yen\", \"command\", \"option\",\\n\"optionleft\", \"optionright\" ]'}}, 'required': ['keys']}, 'description': 'Press a hot key. For example ctrl+c'}, {'name': 'move_mouse', 'parameters': {'type': 'object', 'properties': {'x': {'type': 'integer', 'description': 'x coordinate'}, 'y': {'type': 'integer', 'description': 'y coordinate'}}, 'required': ['x', 'y']}, 'description': 'Move mouse to a position'}, {'name': 'open_url', 'parameters': {'type': 'object', 'properties': {'url': {'type': 'string', 'description': 'URL to open'}}, 'required': ['url']}, 'description': 'Open a URL in chromium'}, {'name': 'press_key', 'parameters': {'type': 'object', 'properties': {'key': {'type': 'string', 'description': 'Which key to press. Options are:\\n[ \"\\\\t\", \"\\\\n\", \"\\\\r\", \" \", \"!\", \\'\\\\\"\\', \"\\\\#\", \"\\\\$\", \"\\\\%\", \"\\\\&\", \"\\\\\\'\",\\n\"\\\\(\", \"\\\\)\", \"\\\\*\", \"\\\\+\", \",\", \"-\", \"\\\\.\", \"/\", \"0\", \"1\", \"2\", \"3\",\\n\"4\", \"5\", \"6\", \"7\", \"8\", \"9\", \":\", \";\", \"<\", \"=\", \">\", \"\\\\?\", \"@\",\\n\"\\\\[\", \"\\\\\\\\\", \"\\\\]\", \"\\\\^\", \"\\\\_\", \"\\\\`\", \"a\", \"b\", \"c\", \"d\", \"e\",\\n\"f\", \"g\", \"h\", \"i\", \"j\", \"k\", \"l\", \"m\", \"n\", \"o\", \"p\", \"q\", \"r\", \"s\",\\n\"t\", \"u\", \"v\", \"w\", \"x\", \"y\", \"z\", \"{\", \"|\", \"}\", \"~\", \"accept\", \"add\",\\n\"alt\", \"altleft\", \"altright\", \"apps\", \"backspace\", \"browserback\",\\n\"browserfavorites\", \"browserforward\", \"browserhome\", \"browserrefresh\",\\n\"browsersearch\", \"browserstop\", \"capslock\", \"clear\", \"convert\", \"ctrl\",\\n\"ctrlleft\", \"ctrlright\", \"decimal\", \"del\", \"delete\", \"divide\", \"down\",\\n\"end\", \"enter\", \"esc\", \"escape\", \"execute\", \"f1\", \"f10\", \"f11\", \"f12\",\\n\"f13\", \"f14\", \"f15\", \"f16\", \"f17\", \"f18\", \"f19\", \"f2\", \"f20\", \"f21\",\\n\"f22\", \"f23\", \"f24\", \"f3\", \"f4\", \"f5\", \"f6\", \"f7\", \"f8\", \"f9\", \"final\",\\n\"fn\", \"help\", \"home\", \"insert\", \"left\", \"numlock\", \"pagedown\", \"pageup\", \"pause\",\\n\"pgdn\", \"pgup\", \"playpause\", \"prevtrack\", \"print\", \"printscreen\",\\n\"prntscrn\", \"prtsc\", \"prtscr\", \"return\", \"right\", \"scrolllock\",\\n\"select\", \"separator\", \"shift\", \"shiftleft\", \"shiftright\", \"sleep\",\\n\"space\", \"stop\", \"subtract\", \"tab\", \"up\", \"volumedown\", \"volumemute\",\\n\"volumeup\", \"win\", \"winleft\", \"winright\", \"yen\", \"command\", \"option\",\\n\"optionleft\", \"optionright\" ]'}}, 'required': ['key']}, 'description': 'Press a key'}, {'name': 'scroll', 'parameters': {'type': 'object', 'properties': {'clicks': {'type': 'integer', 'description': 'Number of clicks, negative scrolls down, positive scrolls up. Defaults to -3.'}}, 'required': []}, 'description': 'Scroll the screen'}, {'name': 'type_text', 'parameters': {'type': 'object', 'properties': {'text': {'type': 'string', 'description': 'Text to type'}}, 'required': ['text']}, 'description': 'Type text'}, {'name': 'mouse_coordinates', 'parameters': {'type': 'object', 'properties': {}, 'required': []}, 'description': 'Get the current mouse coordinates'}, {'name': 'take_screenshots', 'parameters': {'type': 'object', 'properties': {'count': {'type': 'integer'}, 'delay': {'type': 'number'}}, 'required': []}, 'description': 'Take screenshots'}]\n\nI've provided you with the latest screenshot of the computer.\n\nPlease return the action you want to take as a raw JSON object."
"""


def convert_record(record: dict) -> dict:
    # TODO: we need tools
    # (If you want only one image token, change "<image><image>" to "<image>")
    user_message = {
        "role": "user",
        "content": "<image> You are given a task to complete: "
        + record.get("task", "")
        + f"\nYou have the following tools available: {tools}"
        + "\n\nI've provided you with the latest screenshot of the computer.\n\nPlease return the action you want to take as a raw JSON object."
        + "\n\nPlease think before answering.",
    }

    assistant_message = {
        "role": "assistant",
        "content": f"<think>{record.get('thought', '')}</think><answer>{record.get('action', '')}</answer>",
    }

    ms_swift3_object = {
        "messages": [user_message, assistant_message],
        "images": [record.get("image_before", "")],
    }

    return ms_swift3_object


def main():
    if len(sys.argv) != 3:
        print("Usage: python convert.py input.jsonl output.jsonl")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    converted_records = []

    with open(input_file, "r", encoding="utf-8") as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            try:
                record = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"Error parsing line: {line}\n{e}")
                continue
            converted = convert_record(record)
            converted_records.append(converted)

    with open(output_file, "w", encoding="utf-8") as fout:
        # Write one ms-swift3 JSON object per line
        for rec in converted_records:
            fout.write(json.dumps(rec) + "\n")


if __name__ == "__main__":
    main()
