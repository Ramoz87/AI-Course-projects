import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    distribution = dict()
    
    links = corpus[page]
    n = len(corpus)
    n_links = len(links)
    if n_links > 0:
        for link in corpus:
            distribution[link] = (1 - damping_factor) / n
        for link in links:
            distribution[link] += damping_factor / n_links
    else:
        for link in corpus:
            distribution[link] = 1 / n
    
    return distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_ranks = dict()
    next_page = random.choice(list(corpus.keys()))

    for _ in range(n):
        page_ranks[next_page] = page_ranks.get(next_page, 0) + 1/n
        model = transition_model(corpus, next_page, damping_factor)
        population = list(model.keys())
        weights = list(model.values())
        next_page = random.choices(population, weights=weights, k=1)[0]

    return page_ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_ranks = dict()
    n = len(corpus)
    for page in corpus:
        page_ranks[page] = 1 / n

    converged = False
    while not converged:
        new_ranks = dict()
        for page in corpus:
            sum = sum_probability(corpus, page, page_ranks)
            new_ranks[page] = (1 - damping_factor) / n + damping_factor * sum

        converged = isConverged(corpus, page_ranks, new_ranks)
        page_ranks = new_ranks

    return page_ranks

def sum_probability(corpus, page, page_ranks):
    sum = 0
    for i in corpus:
        links = corpus[i]
        num_links = len(links)
        if num_links == 0:
            sum += page_ranks[i] / len(corpus)
        elif page in links:                
            sum += page_ranks[i] / num_links
    return sum


def isConverged(corpus, old_ranks, new_ranks):
    for page in corpus:
        if abs(new_ranks[page] - old_ranks[page]) > 0.001:
            return False
    return True

if __name__ == "__main__":
    main()
