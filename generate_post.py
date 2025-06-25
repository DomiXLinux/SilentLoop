import os
from datetime import datetime

def create_post(title):
    slug = title.lower().replace(" ", "-")
    date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    content = f"""---
title: "{title}"
date: {date}
draft: false
---

This is an auto-generated post about {title}.
"""
    path = f"content/posts/{slug}.md"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"Post created: {path}")

if __name__ == "__main__":
    title = input("Enter post title: ")
    create_post(title)
