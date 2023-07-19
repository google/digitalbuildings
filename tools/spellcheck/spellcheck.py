import yaml
import os

from pathlib import Path
from textblob import TextBlob

def process_file(path):
    if os.path.splitext(path)[1] != ".yaml":
        return
    structure = None
    try:
        structure = yaml.safe_load(Path(path).read_text())
    except:
        print("[WARN] Failed to load file %s.")
        return
    for key in structure.keys():
        value = structure[key]
        if type(value) != dict:
            continue
        if "description" not in value:
            continue
        description = value["description"]
        text_blob = TextBlob(description)
        corrected = text_blob.correct()
        if corrected != description:
            print("[CORRECTIONS] in file %s at key %s" % (path, key))
            print("  Did you mean '%s' instead of '%s'" % (description, corrected))

def process_directory(path):
    children = os.listdir(path)
    for child in children:
        full_child = path + os.sep + child
        if os.path.isdir(full_child):
            process_directory(full_child)
        else:
            process_file(full_child)



process_directory("ontology/yaml")
