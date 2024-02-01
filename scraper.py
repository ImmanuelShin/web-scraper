from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Bosnian_uprising_(1831%E2%80%931832)'

def get_citations_needed_count(url):
  """
  Count the number of 'Citation needed' links on a Wikipedia page.

  Parameters:
  - url (str): The URL of the Wikipedia page.

  Returns:
  - int: The count of 'Citation needed' links.
  """
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')

  citations = soup.find_all('a', attrs={"title": "Wikipedia:Citation needed"})

  return len(citations)

def get_citations_needed_report(url):
  """
  Generate a report of 'Citation needed' instances and their context on a Wikipedia page.

  Parameters:
  - url (str): The URL of the Wikipedia page.

  Returns:
  - str: A string containing the report of 'Citation needed' instances and their context.
  """
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')

  citations = soup.find_all('a', attrs={"title": "Wikipedia:Citation needed"})
  string = ""

  for link in citations:
    parent_sup_tag = link.find_parent('sup')

    if parent_sup_tag:
      parent_p_tag = parent_sup_tag.find_parent('p')
      if parent_p_tag:
        string += "Citation needed for: " + parent_p_tag.get_text().strip() + "\n\n"
  return string

def driver(url):
    """
    Allow the user to interact by copying and pasting a Wikipedia URL to scrape.

    Parameters:
    - url (str): The Wikipedia URL to scrape.

    Returns:
    - None: Prints the count and report of 'Citation needed' instances.
    """
    print("Scraping Wikipedia page:", url)
    
    citations_count = get_citations_needed_count(url)
    print("Number of 'Citation needed' instances:", citations_count)

    citations_report = get_citations_needed_report(url)
    
    if citations_report:
        print("\nCitation needed report:")
        print(citations_report)
    else:
        print("\nNo 'Citation needed' instances found.")
        
if __name__ == "__main__":
    user_input_url = input("Enter the Wikipedia URL: ")
    driver(user_input_url)