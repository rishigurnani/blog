#!/usr/bin/env python3
import os
import json
import glob
import frontmatter
from dateutil import parser as date_parser
import datetime  # needed for type checking

def default_converter(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")

def main():
    # Define the directory where your Markdown blog posts are stored
    blog_dir = os.path.join("content", "blog")
    
    posts = []
    
    # Loop through all Markdown files in the blog directory
    for md_file in glob.glob(os.path.join(blog_dir, "*.md")):
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                post = frontmatter.load(f)
                if "date" in post:
                    # Parse the date string into a datetime object for sorting
                    post_date = date_parser.parse(str(post["date"]))
                    posts.append((post_date, post))
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    if not posts:
        print("No posts found.")
        return

    # Sort posts in descending order (newest first) by date
    posts.sort(key=lambda x: x[0], reverse=True)
    
    # Select the latest post (only its front matter is needed)
    latest_post = posts[0][1].metadata  # using .metadata to get just the front matter

    # Define the output directory and file path (make sure it is inside your Eleventy output)
    output_dir = os.path.join("_site", "api")
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "latest-content.json")

    # Write the JSON file with pretty formatting and our custom default converter
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(latest_post, f, indent=2, default=default_converter)
    
    print("Latest content generated at", output_file)

if __name__ == "__main__":
    main()
