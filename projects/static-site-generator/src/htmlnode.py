class HTMLNode:
    def __init__(self,
                tag: str | None = None,
                value: str | None = None,
                children: list["HTMLNode"] | None = None,
                props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")
    
    def props_to_html(self) -> str:
        if not self.props:
            return ""
        attributes = []
        for key, value in self.props.items():
            attributes.append(f'{key}="{value}"')
        
        # Join with space and add a single leading space
        return " " + " ".join(attributes)
    
    def __repr__(self) -> str:
        return (
            f"HTMLNode(\n"
            f"  tag={repr(self.tag)},\n"
            f"  value={repr(self.value)},\n"
            f"  children={repr(self.children)},\n"
            f"  props={repr(self.props)}\n"
            f")"
        )