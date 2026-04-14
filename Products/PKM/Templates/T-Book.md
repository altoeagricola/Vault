---
tags: Book
title: "{{title}}"
subtitle: "{{subtitle}}"
author: [{{author}}]
category: [{{category}}]
publish: {{publishDate}}
pages: {{totalPage}}
isbn: {{isbn13}}
cover: {{coverUrl}}
localCover: {{localCoverImage}}
updated: {{DATE:YYYY-MM-DD HH:mm:ss}}
---

<%* if (tp.frontmatter.localCover && tp.frontmatter.localCover.trim() !== "") { tR += `![[${tp.frontmatter.localCover}|150]]` } %>

# {{title}}
