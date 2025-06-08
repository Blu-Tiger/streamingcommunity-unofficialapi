"""
    StreamingCommunity API for Python
"""

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
            Impossibile raggiungere "{url}".
            Unable to reach "{url}".
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
            Impossibile estrarre "{name}".
            Unable to get "{name}".
            """
        super().__init__(self.message)


class NoSeasonFoundError(SCAPIError):
    """Raised when regex match fails"""

    def __init__(self, name):
        self.message = f"""
                Nessuna stagione trovata per la serie "{name}".
                No Seasons Found for the series "{name}".
                """
        super().__init__(self.message)


class InvalidJSON(SCAPIError):
    """Raised when regex match returns invalid json"""

    def __init__(self, name, e, data):
        self.message = f"""
            "{name}" contiene JSON non valido:
            "{name}" contains Invalid JSON data:
            Data: {data}
            Error: {e}
            """
        super().__init__(self.message)


class PreviewError(SCAPIError):
    """Raised when unable to get preview data"""

    def __init__(self, name, e):
        self.message = f"""
            Impossibile ottenere i dati per "{name}".
            Unable to get preview data for "{name}".
            Error: {e}
            """
        super().__init__(self.message)
        
class KeyNotFoundOrNone(SCAPIError):
    """Raised when dict key not found or None"""

    def __init__(self, key, name):
        self.message = f"""
            Impossibile estrarre "{key}" da:
                {name}
            Unable to get "{key}" from:
                {name}.
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
        self.session = requests.Session()

    def _wbpage_as_text(self, url):
        try:
            response = self.session.get(
                url, headers={"user-agent": self.user_agent}, timeout=REQ_TIMEOUT
            )
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
            document = self.session.get(url, headers=headers, timeout=REQ_TIMEOUT)
        except requests.exceptions.Timeout as e:
            raise WebPageTimeOutError(query) from e

        # Estrarre i risultati della ricerca
        # Extract the search results
        try:
            search_results = document.json().get("data")
            output_dict = {}
            for result in search_results:
                if (result.get("id") is None or result.get("slug") is None or result.get("name") is None):
                    raise KeyNotFoundOrNone("id or slug", result)
                result["url"] = f"{self._url.geturl()}/it/titles/{result['id']}-{result['slug']}"
                output_dict[result["name"]] = result
        except Exception as e:
            raise InvalidJSON(query, e, document) from e

        return output_dict

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
                    {id, type, runtime, release_date, quality, plot, seasons_count, preview (only for movies), images, genres}.

        Example:
        ```
        film_info = preview('6203-movie-name')
        ```
        """
        headers = {"user-agent": self.user_agent}
        content_id = content_slug.split("-")[0]
        try:
            data = self.session.post(
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
        url = self._url.geturl() + "/it/titles/" + content_slug
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
        if (not preview_data.get("type")):
            raise KeyNotFoundOrNone("type", preview_data)
        media_type = "Movie" if preview_data["type"] == "movie" else "TvSeries"

        images = preview_data.get("images")

        year = preview_data["release_date"].split("-")[0] if preview_data["release_date"] else None
        
        if (data.get("props") is None or data["props"].get("title") is None):
            raise KeyNotFoundOrNone("props or props.title", data)

        props = data["props"]

        trailer_info = props["title"].get("trailers")
        trailer_url = (
            f"https://www.youtube.com/watch?v={trailer_info[0]['youtube_id']}"
            if trailer_info and trailer_info[0]["youtube_id"]
            else None
        )
        if props.get("sliders") is None or len(props["sliders"]) == 0 or props["sliders"][0].get("titles") is None:
            correlates = []
        else:
            correlates = props["sliders"][0]["titles"]
        
        size = min(len(correlates), 15)
        correlates_list = correlates[:size]

        plot = props["title"].get("plot")

        score = props["title"].get("score")

        tmdb_id = props["title"].get("tmdb_id")
        imdb_id = props["title"].get("imdb_id")
        netflix_id = props["title"].get("netflix_id")
        prime_id = props["title"].get("prime_id")
        disney_id = props["title"].get("disney_id")
        release_date = props["title"].get("release_date")
        sub_ita = bool(props["title"]["sub_ita"]) if props["title"].get("sub_ita") else None

        # Estrarre i dati degli episodi per le serie
        # Extract episode data for series.
        if media_type == "TvSeries":

            if (props["title"].get("name") is None):
                raise KeyNotFoundOrNone("name", props["title"])

            name = props["title"]["name"]

            seasons = props["title"]["seasons"] if props["title"]["seasons"] else []

            seasons_count = int(props["title"]["seasons_count"]) if props["title"]["seasons_count"] else None

            episode_list = []
            for se in seasons:
                if (se.get("number") is None or se.get("title_id") is None):
                    raise KeyNotFoundOrNone("number or title_id", se)
                season = int(se["number"])
                se_url = f"{url}/season-{season}"
                try:
                    resp = self._wbpage_as_text(se_url)
                    se_data = json.loads(
                        self._html_regex(r'data-page="([\s\S]+})"', resp, "page data")
                    )
                except requests.exceptions.Timeout as e:
                    raise WebPageTimeOutError(se_url) from e
                if (se_data.get("props") is None or se_data["props"].get("loadedSeason") is None):
                    raise KeyNotFoundOrNone("props or props.loadedSeason", se_data)
                episodes = se_data["props"]["loadedSeason"]["episodes"] if se_data["props"]["loadedSeason"].get("episodes") else []
                sid = se["title_id"]
                for ep in episodes:
                    if (ep.get("id") is None):
                        raise KeyNotFoundOrNone("id", ep)
                    href = f"{self._url.geturl()}/it/watch/{sid}?e={ep['id']}"

                    episode = {
                        "name": ep.get("name"),
                        "season": season,
                        "episode": int(ep["number"]) if ep.get("number") else None,
                        "description": ep.get("plot"),
                        "duration": int(ep["duration"]) if ep.get("duration") else None,
                        "images": ep.get("images"),
                        "url": href,
                        "id": ep.get("id"),
                    }
                    episode_list.append(episode)

            if not episode_list:
                raise NoSeasonFoundError(name)

            return {
                "name": name,
                "url": url,
                "id": props["title"].get("id"),
                "type": media_type,
                "episodeList": episode_list,
                "images": images,
                "year": int("".join(filter(str.isdigit, year))) if year else None,
                "plot": plot,
                "tmdb_id": tmdb_id,
                "imdb_id": imdb_id,
                "netflix_id": netflix_id,
                "prime_id": prime_id,
                "disney_id": disney_id,
                "release_date": release_date,
                "sub_ita": sub_ita,
                "rating": int(float(score) * 1000) if score else None,
                "seasons_count": seasons_count,
                "tags": [genre.get("name") for genre in preview_data["genres"]] if preview_data.get("genres") else None,
                "trailerUrl": trailer_url,
                "recommendations": correlates_list,
            }

        return {
            "name": props["title"].get("name"),
            "url": url,
            "id": props["title"].get("id"),
            "type": media_type,
            "images": images,
            "year": int("".join(filter(str.isdigit, year))) if year else None,
            "plot": plot,
            "tmdb_id": tmdb_id,
            "imdb_id": imdb_id,
            "netflix_id": netflix_id,
            "prime_id": prime_id,
            "disney_id": disney_id,
            "release_date": release_date,
            "sub_ita": sub_ita,
            "rating":  int(float(score) * 1000) if score else None,
            "tags": [genre["name"] for genre in preview_data["genres"]] if preview_data.get("genres") else None,
            "duration": int(props["title"]["runtime"]) if props["title"].get("runtime") else None,
            "trailerUrl": trailer_url,
            "recommendations": correlates_list,
        }

    def get_links(self, content_id, episode_id=None, get_m3u=False):
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
            get_m3u (bool):
                Se si desidera direttamente il file m3u
                If you want the m3u file

        Returns:
            tuple:
                Una tupla contenente il contenuto dell'iframe da incorporare e l'URL scaricabile.
                A tuple containing the iframe content for embedding and the downloadable URL.

        Example:
        ```
        iframe, m3u_playlist_url = get_links(50636)
        iframe, m3u_playlist_url, m3u_playlist_file = get_links(50636, get_m3u=True)
        ```

        """
        headers = {
            "user-agent": self.user_agent,
        }
        
        episode_id_qs = f"?episode_id={episode_id}" if episode_id else ""
        sc_iframe_url = f"{self._url.geturl()}/it/iframe/{content_id}{episode_id_qs}"
        

        # Extract the video page url
        video_page_url = self._wbpage_as_text(sc_iframe_url)

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
        streams = json.loads(
            self._html_regex(
                r"window\.streams[^=]+=[^[](\[.*\])",
                iframe_page,
                "playlist streams",
            )
        )

        # playlist_url = next((sub for sub in streams if sub["active"] is True), None)[
        #     "url"
        # ]
        playlist_url = self._html_regex(
            r"window\.masterPlaylist[^<]+url:[^<]+\'([^<]+?)\'",
            iframe_page,
            "playlist url",
        )

        can_play_fhd = (
            self._html_regex(
                r"window\.canPlayFHD\s+?=\s+?(\w+)",
                iframe_page,
                "playlist fhd option",
            )
            == "true"
        )
        # video_info = json.loads(self._html_regex(r'window\.video[^{]+({[^<]+});',vixcloud_iframe, "video info")

        # Generate the polaylist url
        dl_url = (
            playlist_url
            + ("&" if bool(re.search(r"\?[^#]+", playlist_url)) else "?")
            + "expires="
            + playlist_params.get("expires")
            + "&token="
            + playlist_params.get("token")
            + ("&h=1" if can_play_fhd else "")
        )

        if get_m3u:
            m3u = None
            try:
                m3u_response = self.session.get(
                    dl_url,
                    headers=headers,
                    timeout=REQ_TIMEOUT,
                )
            except requests.exceptions.Timeout as e:
                raise WebPageTimeOutError("m3u URL") from e
            if m3u_response.status_code == 200:
                m3u = html.unescape(m3u_response.text)
            else:
                raise WebPageStatusCodeError("m3u URL", m3u_response.status_code)

            return sc_iframe_url, dl_url, m3u
        else:
            return sc_iframe_url, dl_url