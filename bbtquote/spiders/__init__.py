# -*- coding: utf-8 -*-
import re
from collections import defaultdict


class Character:
    CHARACTER_NAME = ["Sheldon", "Leonard",
                      "Penny", "Howard", "Raj", "Amy", "Bernadette"]

    def __init__(self):
        self._phrase = defaultdict(dict)
        for name in self.CHARACTER_NAME:
            self._phrase[name] = []

    def append_phrase(self, contents):
        elements_count = len(contents)
        for (i, content) in enumerate(contents):
            extracted_phrase = re.search(r"[a-z]+:", content)
            if extracted_phrase:
                name_point = extracted_phrase.end() - 1
                phrase_point = extracted_phrase.end() + 1
                if content[:name_point] == "Sheldon":
                    self._phrase["Sheldon"].append(content[phrase_point:].strip())
                elif content[:name_point] == "Leonard":
                    self._phrase["Leonard"].append(content[phrase_point:].strip())
                elif content[:name_point] == "Penny":
                    self._phrase["Penny"].append(content[phrase_point:].strip())
                elif content[:name_point] == "Howard":
                    self._phrase["Howard"].append(content[phrase_point:].strip())
                elif content[:name_point] == "Raj":
                    self._phrase["Raj"].append(content[phrase_point:].strip())
                elif content[:name_point] == "Amy":
                    self._phrase["Amy"].append(content[phrase_point:].strip())
                elif content[:name_point] == "Bernadette":
                    self._phrase["Bernadette"].append(content[phrase_point:].strip())
                else:
                    continue
            else:
                if i != elements_count - 1:
                    contents[i+1] = contents[i].strip() + contents[i+1]
