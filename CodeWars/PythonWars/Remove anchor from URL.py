
# Complete the function/method so that it returns
# the url with anything after the anchor (#) removed.

def remove_url_anchor(url):
    output = ''
    for char in url:
        if char == '#':
            return output
        else:
            output += char
    return output

