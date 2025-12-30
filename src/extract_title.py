from blocks import markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("#") and not line.startswith("##"):
            return line.strip("#").strip()
    raise Exception("Invalid Heading. Provide a valid heading.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    f.closed

    with open(template_path) as f:
        template = f.read()
    f.closed

    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()

    title = extract_title(markdown)

    full_html = template.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", html_content)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(full_html)
    to_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, filename)

        if os.path.isfile(full_path):
            with open(full_path) as f:
                markdown = f.read()
            f.closed

            html_node = markdown_to_html_node(markdown)
            html_content = html_node.to_html() 

            with open(template_path) as f:
                template = f.read()

            name, ext = os.path.splitext(filename)
            dest_file_path = os.path.join(dest_dir_path, name + ".html")
            title = extract_title(markdown)

            full_html = template.replace("{{ Title }}", title)

            full_html = full_html.replace("{{ Content }}", html_content)

            with open(dest_file_path, "w") as f:
                f.write(full_html)

        else:
            dest_subdir = os.path.join(dest_dir_path, filename)
            os.makedirs(dest_subdir, exist_ok=True)
            generate_pages_recursive(full_path, template_path, dest_subdir)
        