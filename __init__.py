# __init__.py

from .nodes import StringListSplitter

NODE_CLASS_MAPPINGS = {
    "StringListSplitter": StringListSplitter
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StringListSplitter": "String List Splitter"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']