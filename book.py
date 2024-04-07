from bs4 import BeautifulSoup

def extract_article(input_file, output_file):
    # Read the input HTML file
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the div with id "article"
    article_div = soup.find('div', id='article')

    if article_div:
        # Remove all other elements except the article div and its descendants
        for element in soup.find_all(True):
            if element != article_div and not is_descendant(element, article_div):
                element.extract()

        # Write the content of the article div to the output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(article_div))
        print("Article extracted and saved successfully to", output_file)
    else:
        print("Div with id 'article' not found in the input HTML file.")

def is_descendant(element, ancestor):
    """
    Checks if the given element is a descendant of the specified ancestor.
    """
    for parent in element.parents:
        if parent == ancestor:
            return True
    return False

# Usage example:
input_file = 'index.html'
output_file = 'article.html'
extract_article(input_file, output_file)
