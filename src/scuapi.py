import requests
from bs4 import BeautifulSoup
import time
import hashlib
import base64
import json
import re


#streamingcommunity bet

class API:
    def __init__(self, DOMAIN, userAgent="Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"):
        self.userAgent = userAgent
        self.DOMAIN = DOMAIN
        self.URL = 'https://' + self.DOMAIN

    def search(self, query):
        headers = {'user-agent': self.userAgent}
        main_url = requests.get(self.URL, headers=headers).url
        query_formatted = query.replace(" ", "%20")
        url = f"{main_url}api/search?q={query_formatted}"
        #print(url)
        document = requests.get(url, headers=headers)
        search_results = document.json()['data']
        #print(search_results)
        output_dict = {}
        for result in search_results:
            result['url'] = f"{self.URL}/titles/{result['id']}-{result['slug']}"
            output_dict[result['name']] = result

        return output_dict #[result for result in search_results]


    def load(self, url):
        headers = {'user-agent': self.userAgent}
        document = requests.get(url, headers=headers)
        soup = BeautifulSoup(document.content, 'html.parser')
        poster = re.search("url\((.*)\)", soup.find("div", class_="title-container")['style']).group(1)
        #print(poster)
        id = ''.join(filter(str.isdigit, url.split('-')[0]))
        datajs = requests.post(f"{self.URL}/api/titles/preview/{id}", headers=headers).json()


        type = 'Movie' if datajs['type'] == 'movie' else 'TvSeries'

        year = datajs['release_date'].split('-')[0]

        pagedata = soup.find(id="app")["data-page"]
        #print(pagedata)
        props = json.loads(pagedata)['props']

        trailer_info = props['title']['trailers']
        trailer_url = f"https://www.youtube.com/watch?v={trailer_info[0]['youtube_id']}" if trailer_info else None
        #print(trailer_url)


        correlates = props['sliders'][0]['titles']
        size = min(len(correlates), 15)
        correlates_list = correlates[:size]

        plot = props['title']['plot']

        score = props['title']['score']

        tmdb_id = props['title']['tmdb_id']
        imdb_id = props['title']['imdb_id']
        netflix_id = props['title']['netflix_id']
        prime_id = props['title']['prime_id']
        disney_id = props['title']['disney_id']
        release_date = props['title']['release_date']
        sub_ita = props['title']['sub_ita']

        if type == 'TvSeries':

            name = props['title']['name']

            seasons = props['title']['seasons']

            seasons_count = int(props['title']['seasons_count'])

            episode_list = []
            for se in seasons:
                season = int(se['number'])
                document = requests.get(f'{url}/stagione-{season}', headers=headers)
                soup = BeautifulSoup(document.content, 'html.parser')
                pagedata = soup.find(id="app")["data-page"]
                #print(pagedata)
                episodes = json.loads(pagedata)['props']['loadedSeason']['episodes']
                sid = se['title_id']
                for ep in episodes:
                    scws_id = ep['scws_id']
                    href = f"{self.URL}/watch/{sid}?e={ep['id']}"
                    post_image = 'https://cdn.' + self.DOMAIN + '/images/' + ep['images'][0]['filename'] if ep['images'] else None
                    #print(post_image)

                    episode = {
                        'name': ep['name'],
                        'season': season,
                        'episode': int(ep['number']),
                        'description': ep['plot'],
                        'duration': int(ep['duration']),
                        'posterUrl': post_image,
                        'url': href,
                        'scws_id': scws_id
                    }
                    episode_list.append(episode)

            if not episode_list:
                raise Exception("No Seasons Found")

            return {
                'name': name,
                'url': url,
                'type': type,
                'episodeList': episode_list,
                'posterUrl': poster,
                'year': int(''.join(filter(str.isdigit, year))),
                'plot': plot,
                'tmdb_id': tmdb_id,
                'imdb_id': imdb_id,
                'netflix_id': netflix_id,
                'prime_id': prime_id,
                'disney_id': disney_id,
                'release_date': release_date,
                'sub_ita': bool(sub_ita),
                'rating': int(float(score) * 1000),
                'seasons_count': seasons_count,
                'tags': [genre['name'] for genre in datajs['genres']],
                'trailerUrl': trailer_url,
                'recommendations': correlates_list
            }
        else:
            return {
                'name': soup.select_one("div > div > h1").text,
                'url': f"{self.URL}/watch/{props['title']['id']}",
                'scws_id': props['title']['scws_id'],
                'type': type,
                'posterUrl': poster,
                'year': int(''.join(filter(str.isdigit, year))),
                'plot': plot,
                'tmdb_id': tmdb_id,
                'imdb_id': imdb_id,
                'netflix_id': netflix_id,
                'prime_id': prime_id,
                'disney_id': disney_id,
                'release_date': release_date,
                'sub_ita': bool(sub_ita),
                'rating': int(float(score) * 1000),
                'tags': [genre['name'] for genre in datajs['genres']],
                'duration': int(props['title']['runtime']),
                'trailerUrl': trailer_url,
                'recommendations': correlates_list
            }


    def load_links(self, data):
        ip = requests.get("https://api.ipify.org/").text

        type = 'Movie' if data['type'] == 'Movie' else 'TvSeries'

        #print(type)
        return 'Still working on it!'

        if type == 'TvSeries':
            links = []
            for ep in data['episodeList']:
                scwsid = ep['scws_id']

                expire = str(int(time.time()) + 172800)
                token0 = (expire + ip + " Yc8U6r8KjAKAepEA").encode()
                token1 = hashlib.md5(token0).digest()
                token2 = base64.b64encode(token1).decode()
                token = token2.replace("=", "").replace("+", "-").replace("/", "_")

                link = f'https://vixcloud.co/v2/playlist/{scwsid}?token={token}&token480p={token}&expires={expire}&n=1'

                links.append(link)

            return links

        else:
            scwsid = data['scws_id']


            expire = str(int(time.time()) + 172800)

            token0 = (expire + ip + " Yc8U6r8KjAKAepEA").encode()
            token1 = hashlib.md5(token0).digest()
            token2 = base64.b64encode(token1).decode()
            token = token2.replace("=", "").replace("+", "-").replace("/", "_")

            #link = f'https://scws.work/master/{scwsid}?token={token}&expires={expire}&n=1'
            link = f'https://vixcloud.co/v2/playlist/{scwsid}?token={token}&token480p={token}&expires={expire}&n=1'
                    #https://vixcloud.co/v2/playlist/159536?token=t5OmJHPGf9Ti3DXdd0l_AQ&token360p=&token480p=cEjEiuArJcYsrbPzksSQTQ&token720p=n-00eKBvOxqRh0ISQjbu3Q&token1080p=&expires=1695317130&canCast=1&n=1&b=1

            #https://vixcloud.co/v2/playlist/159536?type=video&rendition=1080p&token=&expires=1695316859&canCast=1&b=1&n=1
            #https://vixcloud.co/v2/playlist/159536?type=video&rendition=1080p&token=HjLZ1Qbx0oNt7u7DbDHM3w&expires=1690305563&n=1

            return link
