from textnode import TextType, TextNode

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props == None or len(self.props) == 0:
            return ""
        result = ""
        for keys, values in self.props.items():
            result += f' {keys}= "{values}"'

        return result


    def __repr__(self):
        h1 = HTMLNode(self.tag, self.value, self.children, self.props)
        print(h1)

