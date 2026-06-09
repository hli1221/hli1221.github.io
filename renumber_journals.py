#!/usr/bin/env python3
"""
Invert journal numbering: top entry (newest) gets largest number.
新编号 = 43 - 旧编号
"""
import re, os

BASE = "/Users/lihui/Documents/GitHub/hli1221.github.io-codex"
IMG_DIR = os.path.join(BASE, "images", "journal")
MD_PATH = os.path.join(BASE, "journal-publication", "index.md")

disk_files = set()
for f in os.listdir(IMG_DIR):
    if not f.startswith("tmp_") and re.match(r'\d+-', f):
        disk_files.add(f)

with open(MD_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = []
for m in re.finditer(r'/images/journal/([\w.-]+)', content):
    old_ref = m.group(1)
    suffix_match = re.match(r'\d+-(.+)', old_ref)
    if not suffix_match:
        continue
    suffix = suffix_match.group(1)
    matching = [f for f in disk_files if f.endswith(suffix)]
    if len(matching) == 1:
        new_ref = matching[0]
        if old_ref != new_ref:
            replacements.append((f'/images/journal/{old_ref}', f'/images/journal/{new_ref}'))

for old_path, new_path in replacements:
    content = content.replace(old_path, new_path)

with open(MD_PATH, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Fixed {len(replacements)} image references.")
