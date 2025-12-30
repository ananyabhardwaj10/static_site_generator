from htmlnode import HTMLNode 

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError()

        if self.tag == None:
            return self.value

        res = ""
        if self.props:
            for keys, values in self.props.items():
                res += f" {keys}={values}"
        
        return f"<{self.tag}{res}>{self.value}</{self.tag}>"