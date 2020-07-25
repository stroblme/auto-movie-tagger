from imdbpie import Imdb


imdb = Imdb()
movie_results = []
results = imdb.search_for_title("Hell Boy II")
for result in results:
    if result['type'] == "feature":
        movie_results.append(result)
        print(result)
