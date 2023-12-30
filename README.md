# SEO Automation in Obsidian.md

This project was created to automate my [Obsidian.md](https://obsidian.md/) workflow for SEO tasks.

Essentially, almost every Obsidian note represents a separate blog post with `status` and `url` metadata.

`Status` indicates the "status" of the selected blog post. It helps me determine if the post is to-write, to-fix, or published.

## Example

Look at the example graph:

![Obsidian graph representing my SEO workflow](https://i.imgur.com/oIxreR3.png)

### Explanation

- `Green dots` - represent post categories
- `Blue dots` - are published blog posts
- `Gray dots` - are **not yet** published or planned blog posts

## How is this app going to automate it?

### Simple Stuff

Firstly, the app will check if a blog post is located on the website at the previously mentioned `url` by sending a simple HTTP request and waiting for 200, 301, or 304 responses.

Then, it will check for potential errors in the blog post, such as:
- No title
- No description
- Multiple \<h1\> tags
- Incorrect canonical URL
- Unwanted noindex/nofollow tags
- Redirection loops
- Page functionality (e.g., 404 errors)
- Broken links on the page
- And possibly more

For more advanced reports, I use [Ahrefs](https://ahrefs.com/), but this app can provide quick and regular notifications about basic issues.

### Advanced Stuff

It would be beneficial to have a module that automates, or at least assists in creating, natural internal links based on semantics, similar words, or phrases.

Since I store most of my blog post content locally in Obsidian, its global search feature through local files (which is really quick) already aids in finding linking opportunities.

Next, it could help me find the best URLs, titles, and descriptions based on content, current topics, and trends to increase SERP clicks.

---

After all, I don't know what this app will be like in the next 6 months, but I plan to keep it public and open-source under the MIT license, so feel free to steal the code.
