class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented on parent class")

    def props_to_html(self):
        if not self.props:
            return ""
        props_string = [f'{key}="{value}"' for key,
                        value in self.props.items()]
        return f' {" ".join(props_string)}'

    def __repr__(self):
        return(
            f"tag: {self.tag} \n" 
            f"value: {self.value} \n" 
            f"children: {self.children} \n" 
            f"props: {self.props}"
            )

