"""
    StreamingCommunity API for Python
"""

# import time
# import hashlib
# import base64
import json
import re
import html
from urllib.parse import urlparse
import requests

REQ_TIMEOUT = 5


class SCAPIError(Exception):
    """Base exception"""


class WebPageTimeOutError(SCAPIError):
    """Raised when fetching timeouts"""

    def __init__(self, url):
        self.message = f"""
            Impossibile raggiungere '{url}'.
            Unable to reach '{url}'.
            """
        super().__init__(self.message)


class WebPageStatusCodeError(SCAPIError):
    """Raised when status code not 200"""

    def __init__(self, url, status_code):
        self.message = f"""
            '{url}' ha restituito {status_code} http error code.
            '{url}' returned {status_code} http error code.
            """
        super().__init__(self.message)


class MatchNotFound(SCAPIError):
    """Raised when regex match fails"""

    def __init__(self, name):
        self.message = f"""
            Impossibile estrarre {name}.
            Unable to get {name}.
            """
        super().__init__(self.message)


class NoSeasonFoundError(SCAPIError):
    """Raised when regex match fails"""

    def __init__(self, name):
        self.message = f"""
                Nessuna stagione trovata per la serie {name}
                No Seasons Found for the series {name}
                """
        super().__init__(self.message)


class InvalidJSON(SCAPIError):
    """Raised when regex match returns invalid json"""

    def __init__(self, name, e, data):
        self.message = f"""
            {name} contiene JSON non valido:
            {name} contains Invalid JSON data:
            Data: {data}
            Error: {e}
            """
        super().__init__(self.message)


class PreviewError(SCAPIError):
    """Raised when unable to get preview data"""

    def __init__(self, name, e):
        self.message = f"""
            Impossibile ottenere i dati per {name}
            Unable to get preview data for {name}
            Error: {e}
            """
        super().__init__(self.message)


class API:
    """
    Una classe che interagisce con l'API di StreamingCommunity, gestendo le operazioni di ricerca e recupero dei dati.
    A class to interact with the StreamingCommunity API, handling search and data retrieval operations.

    Attributes:
        user_agent (str):
            La stringa User-Agent da usare nelle intestazioni HTTP per le richieste.
            The User-Agent string to be used in HTTP headers for requests.
        domain (str):
            Il nome di dominio dell'API.
            The domain name of the API.
        _url (str):
            L'URL completo costruito dal nome di dominio per effettuare le richieste API.
            The full URL constructed from the domain name for making API requests.

    Args:
        domain (str):
            Il nome di dominio dell'API.
            The domain name of the API.
        user_agent (str, optional):
            La stringa User-Agent da usare nelle intestazioni HTTP. Per impostazione predefinita, è una stringa User-Agent Edge browser in esecuzione su Windows 7.
            The User-Agent string to be used in HTTP headers. Defaults to a standard User-Agent Edge browser running on Windows 7.
    """

    def __init__(
        self,
        domain,
        user_agent="Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    ):
        self.user_agent = user_agent
        self.domain = domain
        self._url = urlparse("https://" + self.domain)

    def _wbpage_as_text(self, url):
        try:
            response = requests.get(url, timeout=REQ_TIMEOUT)
        except requests.exceptions.Timeout as e:
            raise WebPageTimeOutError(url) from e
        if response.status_code == 200:
            return html.unescape(response.text)
        else:
            raise WebPageStatusCodeError(url, response.status_code)

    def _html_regex(self, reg, webpage, name):
        match = re.search(reg, webpage)
        if match:
            return match.group(1)
        else:
            raise MatchNotFound(name)

    def search(self, query):
        """
        Cerca nell'API una determinata query e restituisce un dizionario di risultati.
        Searches the API for a given query and returns a dictionary of results.

        Args:
            query (str):
                La query di ricerca.
                The search query.

        Returns:
            dict:
                Un dizionario in cui le chiavi sono i nomi dei risultati della ricerca e i valori sono dizionari contenenti i dettagli di ciascun risultato.
                A dictionary where keys are the names of the search results and values are dictionaries containing details about each result.

        Example:
        ```
        search_result = search('something')
        ```
        """

        headers = {"user-agent": self.user_agent}
        query_formatted = query.replace(" ", "%20")
        url = f"{self._url.geturl()}/api/search?q={query_formatted}"

        try:
            # Ottenere i risultati della ricerca
            # Getting the research results
            document = requests.get(url, headers=headers, timeout=REQ_TIMEOUT)
        except requests.exceptions.Timeout as e:
            raise WebPageTimeOutError(query) from e

        # Estrarre i risultati della ricerca
        # Extract the search results
        try:
            search_results = document.json()["data"]
            output_dict = {}
            for result in search_results:
                result["url"] = f"{self._url}/titles/{result['id']}-{result['slug']}"
                output_dict[result["name"]] = result
        except Exception as e:
            raise InvalidJSON(query, e, document) from e

        return output_dict  # [result for result in search_results]

    def preview(self, content_slug):
        """
        Carica informazioni minime su un elemento specifico in base al suo URL.
        Loads minimal information about a specific item by its URL.

        Args:
            content_slug (str):
                L'ID dell'elemento da caricare per i dettagli.
                The ID of the item to load details for.

        Returns:
            dict:
                Un dizionario contenente informazioni minimali sull'elemento:
                A dictionary containing detailed information about the item:
                    {id, type, runtime, release_date, quality, plot, seasons_count, preview (only for movies), images, generes}.

        Example:
        ```
        film_info = preview('6203-movie-name')
        ```
        """
        headers = {"user-agent": self.user_agent}
        content_id = content_slug.split("-")[0]
        try:
            data = requests.post(
                self._url.geturl() + "/api/titles/preview/" + content_id,
                headers=headers,
                timeout=REQ_TIMEOUT,
            )
        except Exception as e:
            raise PreviewError(content_slug, e) from e
        try:
            data_dict = data.json()
        except Exception as e:
            raise InvalidJSON(content_slug, e, data) from e
        return data_dict

    def load(self, content_slug):
        """
        Carica informazioni dettagliate su un elemento specifico in base al suo URL.
        Loads detailed information about a specific item by its URL.

        Args:
            content_id (str | int):
                L'URL dell'elemento da caricare per i dettagli.
                The URL of the item to load details for.

        Returns:
            dict:
                Un dizionario contenente informazioni dettagliate sull'elemento, come il tipo, l'anno, la trama, le valutazioni e altro ancora.
                A dictionary containing detailed information about the item, such as type, year, plot, ratings, and more.

        Example:
        ```
        film_info = load('6203-movie-name')
        ```
        """
        headers = {
            "user-agent": self.user_agent,
        }
        url = self._url.geturl() + "/titles/" + content_slug
        try:
            # Ottenere la risposta dell'url dell'elemento
            # Get the response of the item's url
            resp = self._wbpage_as_text(url)
            data = json.loads(
                self._html_regex(r'data-page="([\s\S]+})"', resp, "page data")
            )
        except requests.exceptions.Timeout as e:
            raise WebPageTimeOutError(url) from e

        preview_data = self.preview(content_slug)

        # Estrarre i vari dati
        # Extract the various data
        media_type = "Movie" if preview_data["type"] == "movie" else "TvSeries"

        images = preview_data["images"]

        year = preview_data["release_date"].split("-")[0]

        props = data["props"]

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
                se_url = f"{url}/stagione-{season}"
                try:
                    resp = self._wbpage_as_text(url)
                    se_data = json.loads(
                        self._html_regex(r'data-page="([\s\S]+})"', resp, "page data")
                    )
                except requests.exceptions.Timeout as e:
                    raise WebPageTimeOutError(se_url) from e
                episodes = se_data["props"]["loadedSeason"]["episodes"]
                sid = se["title_id"]
                for ep in episodes:
                    scws_id = ep["scws_id"]
                    href = f"{self._url}/watch/{sid}?e={ep['id']}"

                    episode = {
                        "name": ep["name"],
                        "season": season,
                        "episode": int(ep["number"]),
                        "description": ep["plot"],
                        "duration": int(ep["duration"]),
                        "images": ep["images"],
                        "url": href,
                        "scws_id": scws_id,
                    }
                    episode_list.append(episode)

            if not episode_list:
                raise NoSeasonFoundError(name)

            return {
                "name": name,
                "url": url,
                "type": media_type,
                "episodeList": episode_list,
                "images": images,
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
                "tags": [genre["name"] for genre in preview_data["genres"]],
                "trailerUrl": trailer_url,
                "recommendations": correlates_list,
            }

        return {
            "name": props["title"]["name"],
            "url": url,
            "scws_id": props["title"]["scws_id"],
            "type": media_type,
            "images": images,
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
            "tags": [genre["name"] for genre in preview_data["genres"]],
            "duration": int(props["title"]["runtime"]),
            "trailerUrl": trailer_url,
            "recommendations": correlates_list,
        }

    def get_links(self, content_id, episode_id=None):
        """
        Estrai la playlist m3u8
        Get the m3u8 playlist

        Args:
            content_id (str | int):
                L'ID dell'elemento.
                The ID of the item.

            episode_id (str | int | none):
                L'ID dell'episodio se è una serie.
                The ID of the episode if it's a series.

        Returns:
            tuple:
                Una tupla contenente il contenuto dell'iframe da incorporare e l'URL scaricabile.
                A tuple containing the iframe content for embedding and the downloadable URL.

        Example:
        ```
        iframe, m3u8_playlist = get_links(50636)
        ```

        """

        webpage = self._wbpage_as_text(
            self._url.geturl()
            + "/watch/"
            + str(content_id)
            + ("" if episode_id is None else ("&e=" + str(episode_id)))
        )

        # Extract information from data-page attribute
        info = json.loads(
            re.sub(
                r',[^"]+}',
                "}",
                self._html_regex(r'data-page="([\s\S]+})"', webpage, "info"),
            )
        )

        # Extract the video page url
        video_page_url = self._wbpage_as_text(info["props"]["embedUrl"])

        # Get the iframe url and iframe page
        iframe_url = self._html_regex(
            r'<iframe[^>]+src\s*=\s*"([^"]+)', video_page_url, "iframe url"
        )
        iframe_page = self._wbpage_as_text(iframe_url)

        # Extract the playlist params and url from the page js
        playlist_params = json.loads(
            re.sub(
                r',[^"]+}',
                "}",
                self._html_regex(
                    r"window\.masterPlaylist[^:]+params:[^{]+({[^<]+?})",
                    iframe_page,
                    "playlist params",
                ).replace("'", '"'),
            )
        )
        playlist_url = self._html_regex(
            r"window\.masterPlaylist[^<]+url:[^<]+\'([^<]+?)\'",
            iframe_page,
            "playlist url",
        )
        # video_info = json.loads(self._html_regex(r'window\.video[^{]+({[^<]+});',vixcloud_iframe, "video info")

        # Generate the polaylist url
        dl_url = (
            playlist_url
            + ("&" if bool(re.search(r"\?[^#]+", playlist_url)) else "?")
            + "&expires="
            + playlist_params.get("expires")
            + "&token="
            + playlist_params.get("token")
        )

        return iframe_url, dl_url
