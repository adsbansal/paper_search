from serpapi import GoogleSearch


def search_youtube(topic):
    params = {
    "api_key": "85962f1bba972bf8ace3e9d0e965f604d0021725bc86edd76e7848a76bee7499",
    "engine": "youtube",
    "search_query": topic
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    results = results["video_results"]

    ans = []
    cnt = 0
    for dict in results:
        if(cnt>4):
            break
        cnt += 1
        ans.append([dict["title"], dict["link"], dict["length"], dict["description"]])

    return ans