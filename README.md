# Lab - Class 17

## Project: Web Scraper

### Author: Immanuel Shin

## Setup

To use the Web Scraper, follow the steps below:

1. Clone the repository to your local machine.
2. Navigate to the project directory.

### User Interaction

1. Execute the program by running `python scraper.py`.
2. Enter the Wikipedia URL when prompted.
3. View the count and report of 'Citation needed' instances.

### Developer Usage

If you're a developer looking to integrate the Web Scraper functions into your project, you can use the following functions:

- `get_citations_needed_count(url)`: Returns the count of 'Citation needed' links on a Wikipedia page.
- `get_citations_needed_report(url)`: Returns a report of 'Citation needed' instances and their context on a Wikipedia page.

Example:

```python
from file_path_to.scraper import get_citations_needed_count, get_citations_needed_report

url = 'https://en.wikipedia.org/wiki/Your_Wikipedia_Page'
count = get_citations_needed_count(url)
report = get_citations_needed_report(url)

print(f"Number of 'Citation needed' instances: {count}")
print("Citation needed report:")
print(report)
