import logging
import re
from anime_downloader.sites.anime import Anime, AnimeEpisode, SearchResult
from anime_downloader.sites import helpers
from urllib.parse import unquote

logger = logging.getLogger(__name__)


class An1menl(Anime, sitename='an1me'):
    sitename = 'an1me'

    @classmethod
    def search(cls, query):
        params = {
            's': query
        }

        soup = helpers.soupify(helpers.get('https://an1me.nl/', params=params))
        results = dict([(x.get("title"), x.get("href")) for x in soup.select("[href*=https\:\/\/an1me\.nl\/f\/][title]")])

        search_results = [
            SearchResult(
                title=key,
                url=value
            )
            for key, value in results.items()
        ][::-1]
        return search_results

    def _scrape_episodes(self):
        anime_slug = re.search(r"an1me\.nl/f/(.*?)[\/]", self.url)[1]
        ep_regex = fr"\"(https://an1me\.nl/f/{anime_slug}/episode.*)\""
        episodes = [x[1] for x in re.finditer(ep_regex, helpers.get(self.url).text)][::-1]  # noqa
        return episodes

    def _scrape_metadata(self):
        self.title = re.search(r"og:title\" content=\"(.*?) - Anime", helpers.get(self.url).text)[1]  # noqa


class An1menlEpisode(AnimeEpisode, sitename='an1me'):
    def _get_sources(self):
        source_regex = r"source src='(.*?)' size='(.*?)'"
        sources = [x[1] for x in re.finditer(source_regex, helpers.get(self.url).text)]  # noqa
        return [
            ('no_extractor', x)
            for x in sources
        ]
