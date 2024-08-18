"""
@author: Khoa Tran
@title: Handy-Nodes-ComfyUI
@nickname: Handy-Nodes-ComfyUI
@description: This extension offers various handy nodes.
"""

version_code = [1, 0, 0]
version_str = f"V{version_code[0]}.{version_code[1]}" + (f'.{version_code[2]}' if len(version_code) > 2 else '')
print(f"### Loading: Handy Nodes ComfyUI ({version_str})")

from .MaskNodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
