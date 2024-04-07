import os
import requests
from bs4 import BeautifulSoup
import threading

def extract_article(input_html):
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(input_html, 'html.parser')

    # Find the div with id "article"
    article_div = soup.find('div', id='article')

    if article_div:
        # Remove all other elements except the article div and its descendants
        for element in soup.find_all(True):
            if element != article_div and not is_descendant(element, article_div):
                element.extract()
        
        return str(article_div)
    else:
        print("Div with id 'article' not found in the input HTML file.")
        return None

def is_descendant(element, ancestor):
    """
    Checks if the given element is a descendant of the specified ancestor.
    """
    for parent in element.parents:
        if parent == ancestor:
            return True
    return False

def process_links(links_file):
    # Read links from the file
    with open(links_file, 'r') as f:
        links = f.read().splitlines()

    threads = []
    for link in links:
        thread = threading.Thread(target=pull, args=(link,))
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

def pull(link): 
    # Extract the article name from the link
    article_name = link.split('/')[-2]
    output_file = f"book/OPS/{article_name}.html"

    if os.path.exists(output_file):
        print("Article already downloaded.")
        return 

    # Download HTML content from the link
    response = requests.get(link)
    if response.status_code == 200:
        input_html = response.content

        # Extract article div and its sub divs
        article_content = extract_article(input_html)
        if article_content:
            # Write modified HTML to file
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(article_content)
            print(f"Article extracted and saved successfully to {output_file}")
    else:
        print(f"Failed to download HTML content from {link}")
        
    return

if __name__ == '__main__':

    # Usage example:
    links_file = 'links.txt'
    process_links(links_file)
