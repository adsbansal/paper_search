from serpapi import GoogleSearch

def search_scholar(topic):
    params = {
    "engine": "google_scholar",
    # "q": "Solving the Markovitz Problem in a Bayesian setting",
    "q" : topic, 
    "hl": "en",
    "as_ylo": "2020",
    "num": "15",
    "api_key": "85962f1bba972bf8ace3e9d0e965f604d0021725bc86edd76e7848a76bee7499"
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    results = results["organic_results"]

    full_parse = []
    just_cite = []
    for i in results: 
        ex = i["inline_links"]
        if "cited_by" in ex:
            ex = ex['cited_by']["total"]
        else: 
            ex = 0
        just_cite.append(ex)
        full_parse.append([ex, i["title"], i["link"], i["snippet"], i["publication_info"]["summary"]])

    full_parse.sort(key=lambda x: x[0], reverse=True)
    full_parse = full_parse[:7]

    return full_parse
