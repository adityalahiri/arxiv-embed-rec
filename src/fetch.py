import feedparser
import re


# Function to fetch abstract and related papers' abstracts
def fetch_abstracts_and_related(paper_id, max_related=5):
    # Fetch paper information
    paper_info = feedparser.parse(f"http://export.arxiv.org/api/query?id_list={paper_id}")
    paper = paper_info.entries[0]
    primary_category = paper.arxiv_primary_category["term"]

    # Search for related papers
    related_papers_info = feedparser.parse(f"http://export.arxiv.org/api/query?search_query=cat:{primary_category}&max_results={max_related}")
    related_papers = related_papers_info.entries

    return related_papers

