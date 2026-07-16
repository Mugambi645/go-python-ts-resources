from textnode import TextNode, TextType



def main():
    # Instantiate a dummy anchor node
    node = TextNode(
        "This is some anchor text", 
        TextType.LINK, 
        "https://www.boot.dev"
    )
    print(node)


if __name__ == "__main__":
    main()