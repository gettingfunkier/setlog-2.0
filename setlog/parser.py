def split_markdown(content: str):
    parts = content.split('---')
    frontmatter = parts[1].strip()
    body = parts[3].strip()
    notes = parts[4].strip() if len(parts) > 4 else None
    return frontmatter, body, notes

def parse_file(filepath: str):
    with open(filepath, 'r', encoding = 'utf-8') as file:
        content = file.read()

    frontmatter, body, notes = split_markdown(content)  
    print("FRONTMATTER:")
    print(frontmatter)
    print("\nBODY:")
    print(body)
    if notes:
        print("\nNOTES:")
        print(notes)

if __name__ == "__main__":
    parse_file("logs/05-19.md")