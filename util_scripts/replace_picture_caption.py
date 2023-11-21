# Convert the original markdown image to html, to visually display the caption

import os
import re
import shutil


def convert_markdown_to_html(markdown_text:str):
    pattern = r'!\[([^\]]+)(?:\\\[.*?\\\])?.*?\]\(([^ ]+?)(?: \"([^\"]+)\")?\)'
    match = re.search(pattern, markdown_text)

    if not match: return

    alt_text = match.group(1)
    src = match.group(2)

    # Special case. will occur on pic 5.9 etc, which end with '\[xxx]'
    if(alt_text.endswith("\\")):
        alt_text = alt_text.replace("\\", "")
        alt_text += "]"

    html_structure = f'''
<div style="text-align: center;">
    <img style="border-radius: 0.3125em; box-shadow: 0 2px 4px 0 rgba(34,36,38,.12),0 2px 10px 0 rgba(34,36,38,.08);" src="{src}">
</div>
<div style="color:orange;display: block;color: #999;padding: 2px; text-align: left;">
    {alt_text}
</div>
<br><br>
'''
    return html_structure


def main():
    if os.path.exists("./output"): shutil.rmtree("output")
    os.mkdir("./output")
    shutil.copytree("./sourceFile/images", "output/images")

    md_files = [f for f in os.listdir('./sourceFile') if f.endswith('.md')]

    for md_file in md_files:
        with open(f"./sourceFile/{md_file}", 'r', encoding="utf-8") as f:
            lines = f.readlines()

            with open(f"./output/{md_file}", 'w', encoding="utf-8") as f:
                for line in lines:
                    if line.startswith('![图'):
                        line = convert_markdown_to_html(line)
                    f.write(line)

if __name__ == '__main__':
    main()

