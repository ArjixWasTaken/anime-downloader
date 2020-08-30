import logging
from anime_downloader.sites.anime import Anime, AnimeEpisode, SearchResult
from anime_downloader.sites import helpers

logger = logging.getLogger(__name__)

database = helpers.get('https://private.fastani.net/database.json').json()

def search_anilist(search, max_results=50):
    query = """
    query ($id: Int, $page: Int, $search: String, $type: MediaType) {
            Page (page: $page, perPage: 50) {
                    media (id: $id, search: $search, type: $type) {
                            id
                            title {
                                    english
                                    romaji
                            }
                            
                    }
            }
    }
    """
    variables = {
            'search': search,
            'page': 1,
            'perPage': max_results,
            'type': 'ANIME'
    }
    url = 'https://graphql.anilist.co'

    results = helpers.post(url, json={'query': query, 'variables': variables}).json()
    
    result_list = results['data']['Page']['media']
    final_result = []

    for anime in result_list:
        jp_title = anime['title']['romaji']
        ani_id = str(anime['id'])

        entry = [jp_title, ani_id]
        final_result.append(entry)

    return final_result

def exists(key, database):
    try:
        database[key]
        return True
    except KeyError:
        return False
results = {}
class FastAni(Anime, sitename = 'fastani'):
    sitename = 'fastani'

    @classmethod
    def search(cls, query):

        
        ani_search = search_anilist(query)
        for item in ani_search:
            if exists(item[1], database):
                results[item[1]] = item[0]

        search_results = [
            SearchResult(
                title = b,
                url = 'https://fastani/' + a
                )
            for a, b in results.items()
            ]
        return search_results

    def _scrape_episodes(self):
        ani_id = self.url.replace('https://fastani/', '')
        db = database
        db = db[ani_id]['Seasons']
        eps = []
        for array in db:
            eps.extend(array['Episodes'])
        episodes = []
        for i in eps:
            episodes.append(i['file'])
        episodes.sort()
        return episodes

    def _scrape_metadata(self):
        self.title = results[self.url.replace('https://fastani/', '')]

class FastAniEpisode(AnimeEpisode, sitename='fastani'):
    def _get_sources(self):
        return [('no_extractor', self.url)]