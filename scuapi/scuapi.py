"""
    StreamingCommunity API for Python
"""
# import time
# import hashlib
# import base64
import json
import re
import html
import logging
from bs4 import BeautifulSoup
import requests

REQ_TIMEOUT = 5


def _wbpage_as_text(url):
    try:
        response = requests.get(url, timeout=REQ_TIMEOUT)
    except requests.exceptions.Timeout:
        logging.error("""
        Impossibile raggiungere '%s'
        Unable to reach '%s'
        """, url, url)
    if response.status_code == 200:
        return html.unescape(response.text)
    else:
        logging.error("Failed to fetch the website.")


class API:
    """
    Una classe che interagisce con l'API di StreamingCommunity, gestendo le operazioni di ricerca e recupero dei dati.
    A class to interact with the StreamingCommunity API, handling search and data retrieval operations.

    Attributes:
        user_agent (str): La stringa User-Agent da usare nelle intestazioni HTTP per le richieste.
            The User-Agent string to be used in HTTP headers for requests.
        domain (str): Il nome di dominio dell'API.
            The domain name of the API.
        _url (str): L'URL completo costruito dal nome di dominio per effettuare le richieste API.
            The full URL constructed from the domain name for making API requests.

    Args:
        domain (str): Il nome di dominio dell'API.
            The domain name of the API.
        user_agent (str, optional):  La stringa User-Agent da usare nelle intestazioni HTTP. Per impostazione predefinita, è una stringa User-Agent Edge browser in esecuzione su Windows 7.
            The User-Agent string to be used in HTTP headers. Defaults to a standard User-Agent Edge browser running on Windows 7.
    """

    def __init__(
        self,
        domain,
        user_agent="Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    ):
        self.user_agent = user_agent
        self.domain = domain
        self._url = "https://" + self.domain

    def search(self, query):
        """
        Cerca nell'API una determinata query e restituisce un dizionario di risultati.
        Searches the API for a given query and returns a dictionary of results.

        Args:
            query (str): La query di ricerca.
                The search query.

        Returns:
            dict: Un dizionario in cui le chiavi sono i nomi dei risultati della ricerca e i valori sono dizionari contenenti i dettagli di ciascun risultato.
                A dictionary where keys are the names of the search results and values are dictionaries containing details about each result.

        Example:
        ```
        search_result = search('something')
        ```
        """

        headers = {"user-agent": self.user_agent}
        try:
            # Ottenere l'URL principale di StreamingCommunity
            # Get the main  StreamingCommunity URL
            main_url = requests.get(
                self._url, headers=headers, timeout=REQ_TIMEOUT).url
        except requests.exceptions.Timeout:
            logging.error(
                """
            Impossibile raggiungere '%s'
            Unable to reach '%s'
            """, self._url, self._url)
        query_formatted = query.replace(" ", "%20")
        url = f"{main_url}api/search?q={query_formatted}"

        try:
            # Ottenere i risultati della ricerca
            # Getting the research results
            document = requests.get(url, headers=headers, timeout=REQ_TIMEOUT)
        except requests.exceptions.Timeout:
            logging.error("""
            Impossibile raggiungere '%s'
            Unable to reach '%s'
            """, url, url)

        # Estrarre i risultati della ricerca
        # Extract the research results
        search_results = document.json()["data"]
        output_dict = {}
        for result in search_results:
            result["url"] = f"{self._url}/titles/{result['id']}-{result['slug']}"
            output_dict[result["name"]] = result

        return output_dict  # [result for result in search_results]

    def load(self, url):
        """
        Carica informazioni dettagliate su un elemento specifico in base al suo URL.
        Loads detailed information about a specific item by its URL.

        Args:
            url (str): L'URL dell'elemento da caricare per i dettagli.
                The URL of the item to load details for.

        Returns:
            dict: Un dizionario contenente informazioni dettagliate sull'articolo, come il tipo, l'anno, la trama, le valutazioni e altro ancora.
                A dictionary containing detailed information about the item, such as type, year, plot, ratings, and more.

        Example:
        ```
        film_info = load('https://StreamingCommunity.esempio/watch/6203')
        ```
        """
        headers = {"user-agent": self.user_agent}
        try:
            # Ottenere la risposta dell'url dell'elemento
            # Get the response of the item's url
            document = requests.get(url, headers=headers, timeout=REQ_TIMEOUT)
        except requests.exceptions.Timeout:
            logging.error("""
            Impossibile raggiungere '%s'
            Unable to reach '%s'
            """, url, url)
        soup = BeautifulSoup(document.content, "html.parser")
        poster = re.search(
            r"url\((.*)\)", soup.find("div", class_="title-container")["style"]
        ).group(1)

        # Estrarre l'ID dell'elemento dall'URL
        # Extract the item ID from the URL
        item_id = "".join(filter(str.isdigit, url.split("-")[0]))
        try:
            # Ottenere i dati dell'elemento
            # Get the item's data
            datajs = requests.post(
                f"{self._url}/api/titles/preview/{item_id}", headers=headers, timeout=REQ_TIMEOUT
            ).json()
        except requests.exceptions.Timeout:
            logging.error("""
            Impossibile raggiungere '%s'
            Unable to reach '%s'
            """, self._url, self._url)

        # Estrarre i vari dati
        # Extract the various data
        media_type = "Movie" if datajs["type"] == "movie" else "TvSeries"

        year = datajs["release_date"].split("-")[0]

        pagedata = soup.find(id="app")["data-page"]

        props = json.loads(pagedata)["props"]

        trailer_info = props["title"]["trailers"]
        trailer_url = (
            f"https://www.youtube.com/watch?v={trailer_info[0]['youtube_id']}"
            if trailer_info
            else None
        )

        correlates = props["sliders"][0]["titles"]
        size = min(len(correlates), 15)
        correlates_list = correlates[:size]

        plot = props["title"]["plot"]

        score = props["title"]["score"]

        tmdb_id = props["title"]["tmdb_id"]
        imdb_id = props["title"]["imdb_id"]
        netflix_id = props["title"]["netflix_id"]
        prime_id = props["title"]["prime_id"]
        disney_id = props["title"]["disney_id"]
        release_date = props["title"]["release_date"]
        sub_ita = props["title"]["sub_ita"]

        # Estrarre i dati degli episodi per le serie
        # Extract episode data for series.
        if media_type == "TvSeries":

            name = props["title"]["name"]

            seasons = props["title"]["seasons"]

            seasons_count = int(props["title"]["seasons_count"])

            episode_list = []
            for se in seasons:
                season = int(se["number"])
                try:
                    document = requests.get(
                        f"{url}/stagione-{season}", headers=headers, timeout=REQ_TIMEOUT)
                except requests.exceptions.Timeout:
                    logging.error("""
                    Impossibile raggiungere '%s'
                    Unable to reach '%s'
                    """, url, url)
                soup = BeautifulSoup(document.content, "html.parser")
                pagedata = soup.find(id="app")["data-page"]
                episodes = json.loads(pagedata)[
                    "props"]["loadedSeason"]["episodes"]
                sid = se["title_id"]
                for ep in episodes:
                    scws_id = ep["scws_id"]
                    href = f"{self._url}/watch/{sid}?e={ep['id']}"
                    post_image = (
                        "https://cdn."
                        + self.domain
                        + "/images/"
                        + ep["images"][0]["filename"]
                        if ep["images"]
                        else None
                    )

                    episode = {
                        "name": ep["name"],
                        "season": season,
                        "episode": int(ep["number"]),
                        "description": ep["plot"],
                        "duration": int(ep["duration"]),
                        "posterUrl": post_image,
                        "url": href,
                        "scws_id": scws_id,
                    }
                    episode_list.append(episode)

            if not episode_list:
                logging.error("""
                Nessuna stagione trovata
                No Seasons Found
                """)

            return {
                "name": name,
                "url": url,
                "type": media_type,
                "episodeList": episode_list,
                "posterUrl": poster,
                "year": int("".join(filter(str.isdigit, year))),
                "plot": plot,
                "tmdb_id": tmdb_id,
                "imdb_id": imdb_id,
                "netflix_id": netflix_id,
                "prime_id": prime_id,
                "disney_id": disney_id,
                "release_date": release_date,
                "sub_ita": bool(sub_ita),
                "rating": int(float(score) * 1000),
                "seasons_count": seasons_count,
                "tags": [genre["name"] for genre in datajs["genres"]],
                "trailerUrl": trailer_url,
                "recommendations": correlates_list,
            }

        return {
            "name": soup.select_one("div > div > h1").text,
            "url": f"{self._url}/watch/{props['title']['id']}",
            "scws_id": props["title"]["scws_id"],
            "type": media_type,
            "posterUrl": poster,
            "year": int("".join(filter(str.isdigit, year))),
            "plot": plot,
            "tmdb_id": tmdb_id,
            "imdb_id": imdb_id,
            "netflix_id": netflix_id,
            "prime_id": prime_id,
            "disney_id": disney_id,
            "release_date": release_date,
            "sub_ita": bool(sub_ita),
            "rating": int(float(score) * 1000),
            "tags": [genre["name"] for genre in datajs["genres"]],
            "duration": int(props["title"]["runtime"]),
            "trailerUrl": trailer_url,
            "recommendations": correlates_list,
        }

    def get_links(self, url):
        """
        Estrai la playlist m3u8
        Get the m3u8 playlist

        Args:
        - url (str): L'url dell'episodio o del film dalla funzione load().
            The url of the episode or film from the load() function.

        Returns:
        - tuple: Una tupla contenente il contenuto dell'iframe da incorporare e l'URL scaricabile.
            A tuple containing the iframe content for embedding and the downloadable URL.

        Example:
        ```
        iframe, m3u8_playlist = get_links('https://StreamingCommunity.esempio/watch/7540?e=50636')
        ```

        """

        webpage = (_wbpage_as_text(url))

        info = json.loads(re.search(
            r'data-page="([\s\S]+})"', webpage).group(1))
        iframe = _wbpage_as_text(info['props']['embedUrl'])
        iframeinfo_url = re.search(
            r'<iframe[^>]+src="([^"]+)', iframe).group(1)
        vixcloud_iframe = _wbpage_as_text(iframeinfo_url)
        playlist_info = json.loads(re.sub(r',[^"]+}', '}', re.search(
            r'window\.masterPlaylist[^:]+params:[^{]+({[^<]+?})', vixcloud_iframe).group(1).replace('\'', '"')))
        playlist_url = re.search(
            r'window\.masterPlaylist[^<]+url:[^<]+\'([^<]+?)\'', vixcloud_iframe).group(1)
        # video_info = json.loads(self._html_search_regex(r'window\.video[^{]+({[^<]+});',vixcloud_iframe,'iframe info'))
        tokens_url = ''
        for x, y in playlist_info.items():
            if y and x == 'token':
                tokens_url = x + '=' + y
            if y and 'token' in x:
                tokens_url = tokens_url + '&' + x + '=' + y

        dl_url = playlist_url + '?' + tokens_url + \
            '&expires=' + playlist_info.get('expires')

        return iframeinfo_url, dl_url

    # Old method
    #     ip = requests.get("https://api.ipify.org/").text

    #     media_type = 'Movie' if data['type'] == 'Movie' else 'TvSeries'

    #     return 'Still working on it!'

    #     if media_type == 'TvSeries':
    #         links = []
    #         for ep in data['episodeList']:
    #             scwsid = ep['scws_id']

    #             expire = str(int(time.time()) + 172800)
    #             token0 = (expire + ip + " Yc8U6r8KjAKAepEA").encode()
    #             token1 = hashlib.md5(token0).digest()
    #             token2 = base64.b64encode(token1).decode()
    #             token = token2.replace("=", "").replace("+", "-").replace("/", "_")

    #             link = f'https://vixcloud.co/v2/playlist/{scwsid}?token={token}&token480p={token}&expires={expire}&n=1'

    #             links.append(link)

    #         return links

    #     else:
    #         scwsid = data['scws_id']

    #         expire = str(int(time.time()) + 172800)

    #         token0 = (expire + ip + " Yc8U6r8KjAKAepEA").encode()
    #         token1 = hashlib.md5(token0).digest()
    #         token2 = base64.b64encode(token1).decode()
    #         token = token2.replace("=", "").replace("+", "-").replace("/", "_")

    #         #link = f'https://scws.work/master/{scwsid}?token={token}&expires={expire}&n=1'
    #         link = f'https://vixcloud.co/v2/playlist/{scwsid}?token={token}&token480p={token}&expires={expire}&n=1'
    #                 #https://vixcloud.co/v2/playlist/159536?token=t5OmJHPGf9Ti3DXdd0l_AQ&token360p=&token480p=cEjEiuArJcYsrbPzksSQTQ&token720p=n-00eKBvOxqRh0ISQjbu3Q&token1080p=&expires=1695317130&canCast=1&n=1&b=1

    #         #https://vixcloud.co/v2/playlist/159536?type=video&rendition=1080p&token=&expires=1695316859&canCast=1&b=1&n=1
    #         #https://vixcloud.co/v2/playlist/159536?type=video&rendition=1080p&token=HjLZ1Qbx0oNt7u7DbDHM3w&expires=1690305563&n=1

    #         return link
