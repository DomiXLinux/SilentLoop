import os
import frontmatter
from datetime import datetime

title = os.getenv("POST_TITLE", "Untitled Post")
slug = title.lower().replace(" ", "-")
date = datetime.now().strftime("%Y-%m-%d")
filename = f"content/posts/{slug}.md"

post = frontmatter.Post("", title=title, date=date)
with open(filename, "w", encoding="utf-8") as f:
    f.write(frontmatter.dumps(post))

print(f"✅ Created new post: {filename}")

