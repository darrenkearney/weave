import re

link_tags = re.compile(r'\[\[.*?\]\]')

def extract_link_tags(text):
    return link_tags.findall(text)

def non_empty_links(link):
    return link != ''

def remove_enclosing_brackets(link):
    return link[2:-2]

"""
Split the link by the separator and return the field in the
given index. Negative indices start from the end of the array.
"""
def get_field(link, seperator, index):
    fields = link.split(seperator)

    if (len(fields) == 1):
        # Seperator not present
        return False

    if (index < 0):
        return fields[len(fields) + index]
    else:
        return fields[index]

def extract_link(tag_content):
    """
	Arrow links:
	[[display text->link]] format
	[[link<-display text]] format
	
	Interpret the rightmost '->' and the leftmost '<-' as the divider.
    """
    if get_field(tag_content, '->', -1):
        return get_field(tag_content, '->', -1)
    elif get_field(tag_content, '<-', 0):
        return get_field(tag_content, '<-', 0)
    elif get_field(tag_content, '|', -1):
        return get_field(tag_content, '|', -1)
    else:
        return tag_content

def link_parser(text):
    result = extract_link_tags(text)
    result = list(map( remove_enclosing_brackets, result))
    result = list(map( extract_link, result))
    result = filter( non_empty_links, result)
    result = set(result)
    return result