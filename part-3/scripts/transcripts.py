import srsly
from pathlib import Path 
from re import compile


regex = compile("([0-9][0-9]:[0-9][0-9]:[0-9][0-9])")

def episode_lines(path:Path):
    """Go over all lines in a transcript file, also generate metadata"""
    i = 0
    for line in path.read_text().split("\n"):
        if regex.match(line):
            without_time = regex.sub("", line[8:])
            without_name = without_time[without_time.find(":") + 1: ]
            speaker = without_time[:without_time.find(":")].strip() if (":" in without_time) else ""
            i += 1
            yield {
                "text": without_name.strip().replace("\xa0", " "), 
                "meta": {
                    "speaker": speaker,
                    "file": str(path),
                    "turn": i
                }
            }

def all_episode_lines(input_folder):
    """Go over all lines in all files in a folder"""
    for path in reversed(sorted(Path(input_folder).glob("*.txt"))):
        for line in episode_lines(path):
            yield line

if __name__ == "__main__":
    lines = all_episode_lines("../transcripts")
    srsly.write_jsonl("data/lines.jsonl", lines)
