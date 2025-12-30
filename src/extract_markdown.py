import re 
from textnode import TextNode, TextType

def extract_markdown_images(text):
    img_list = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return img_list

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.TEXT:
            original_text = old_node.text
            images = extract_markdown_images(original_text)
            if len(images) == 0:
                new_nodes.append(old_node)
                continue

            for image in images:
                image_alt, image_link = image
                sections = original_text.split(f"![{image_alt}]({image_link})", 1)

                if sections[0].strip() != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))

                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))

                original_text = sections[1]

            if original_text != "":
                    new_nodes.append(TextNode(original_text, TextType.TEXT))

        else:
            new_nodes.append(old_node)

    return new_nodes

            

def extract_markdown_links(text):
    link_list = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_list

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type == TextType.TEXT:
            original_text = old_node.text
            links = extract_markdown_links(original_text)
            if len(links) == 0:
                new_nodes.append(old_node)
                continue

            for link in links:
                link_text, link_url = link
                sections = original_text.split(f"[{link_text}]({link_url})", 1)

                if sections[0].strip() != "":
                    new_nodes.append(TextNode(sections[0], TextType.TEXT))

                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

                original_text = sections[1]

            if original_text != "":
                    new_nodes.append(TextNode(original_text, TextType.TEXT))

        else:
            new_nodes.append(old_node)

    return new_nodes
