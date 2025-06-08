A simple unofficial api for the italian StreamingCommunity website.

![Static Badge](https://img.shields.io/badge/version-3.1b-orange?style=for-the-badge) ![Static Badge](https://img.shields.io/badge/03%2F06%2F2025-To%20Be%20Tested-orange?style=for-the-badge
)

[![PyPI](https://img.shields.io/pypi/v/streamingcommunity-unofficialapi?style=flat)](https://pypi.org/project/streamingcommunity-unofficialapi/)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/w/Blu-Tiger/streamingcommunity-unofficialapi?style=flat)
![PyPI - Downloads](https://img.shields.io/pypi/dd/streamingcommunity-unofficialapi?style=flat)
![PyPI - Downloads](https://img.shields.io/pypi/dw/streamingcommunity-unofficialapi?style=flat)
![PyPI - Downloads](https://img.shields.io/pypi/dm/streamingcommunity-unofficialapi?style=flat)

> [!IMPORTANT]
> After updating please check the changes in the output examples.

# StreamingCommunity-API

### Table of Contents

- [Installazione](#installazione)
- [Utilizzo](#utilizzo)
  - [Ricerca](#ricerca)
    - [Esempio Film](#ricerca-esempio-film)
    - [Esempio Serie](#ricerca-esempio-serie)
  - [Info Film/Serie](#info-filmserie)
    - [Esempio Film](#info-esempio-film)
    - [Esempio Serie](#info-esempio-serie)
  - [Link Iframe (embed) e Playlist m3u8](#getlinks)
- [Download Video](#download-video)

## Installazione <a name="installazione" />

Questa libreria richiede [Python 3.10](https://www.python.org/) o superiore.

È Possibile installarare la libreria tramite pip:

```
pip install streamingcommunity-unofficialapi
```

## Utilizzo <a name="utilizzo" />

Per iniziare bisona impostare il dominio di StreamingCommunity che si desidera utilizzare.

```python
from scuapi import API

sc = API('StreamingCommunity.esempio')
```

- ### Ricerca <a name="ricerca" />

  Per ricercare un Film o una Serie per nome nel sito di StreamingCommunity è possibile usare la funzione search().

  ```python
  from scuapi import API

  sc = API('StreamingCommunity.esempio')
  sc.search('John Wick')
  ```

  La funzione restituirà un dizionario contentente per chiave il nome del Film o Serie e per valore un dizionario contenente tutte le informazioni correllate.

  <details>
  <summary>Esempio Film: <a name="ricerca-esempio-film" /></summary>

  ```
  {
      "John Wick": {
          "id": 6,
          "slug": "john-wick",
          "name": "John Wick",
          "type": "movie",
          "score": "8.1",
          "sub_ita": 0,
          "last_air_date": "2014-10-22",
          "seasons_count": 0,
          "images": [
              {
                  "imageable_id": 6,
                  "imageable_type": "title",
                  "filename": "f7887fba-d2d3-4252-b2e9-45129e1ecfd9.webp",
                  "type": "poster",
                  "original_url_field": None,
              },
              {
                  "imageable_id": 6,
                  "imageable_type": "title",
                  "filename": "3ca16987-4229-4369-ba0b-670e0ec2b4df.webp",
                  "type": "background",
                  "original_url_field": None,
              }
          ],
          "url": "https://StreamingCommunity.esempio/titles/6-john-wick",
      },
      "John Wick 4": {
          "id": 6203,
          "slug": "john-wick-4",
          "name": "John Wick 4",
          "type": "movie",
          "score": "8.6",
          "sub_ita": 0,
          "last_air_date": "2023-03-22",
          "seasons_count": 0,
          "images": [
              {
                  "imageable_id": 6203,
                  "imageable_type": "title",
                  "filename": "8babb029-90b3-4237-aff2-2395b2dfb5ce.webp",
                  "type": "cover_mobile",
                  "original_url_field": None,
              },
              {
                  "imageable_id": 6203,
                  "imageable_type": "title",
                  "filename": "64934c02-794f-4307-a860-758eed06b717.webp",
                  "type": "logo",
                  "original_url_field": None,
              }
          ],
          "url": "https://StreamingCommunity.esempio/titles/6203-john-wick-4",
      },
  }
  ```

   </details>

  <details>
  <summary>Esempio Serie: <a name="ricerca-esempio-serie" /></summary>

  ```
  {
    "Hazbin Hotel": {
      "id": 7540,
      "slug": "hazbin-hotel",
      "name": "Hazbin Hotel",
      "type": "tv",
      "score": "9.2",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 1,
      "images": [
        {
          "imageable_id": 7540,
          "imageable_type": "title",
          "filename": "cf42bff9-41dc-4710-be80-cbc91ac6686c.webp",
          "type": "logo",
          "original_url_field": null
        },
        {
          "imageable_id": 7540,
          "imageable_type": "title",
          "filename": "d79bac25-35d5-4cae-9543-3f7380260ff8.webp",
          "type": "cover_mobile",
          "original_url_field": null
        },
        {
          "imageable_id": 7540,
          "imageable_type": "title",
          "filename": "4ba17e65-c47b-41cb-833c-2fc5e640bad0.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 7540,
          "imageable_type": "title",
          "filename": "ca6cbc7b-4d05-4d23-bc35-cef0aafd33b4.webp",
          "type": "background",
          "original_url_field": null
        },
        {
          "imageable_id": 7540,
          "imageable_type": "title",
          "filename": "d06f117f-d3c6-43ef-9d9a-9d99543387ad.webp",
          "type": "poster",
          "original_url_field": null
        }
      ],
      "url": "https://StreamingCommunity.esempio/titles/7540-hazbin-hotel"
    }
  }
  ```

  </details>

- ### Info Film/Serie <a name="info-filmserie" />

  Per ottenere informazioni su un Film o una Serie è possibile usare la funzione load() o preview per informazioni minimali.

  ```python
  from scuapi import API

  sc = API('StreamingCommunity.esempio')
  sc.load('6203-john-wick-4')
  ```

  La funzione restituirà un dizionario contentente tutte le informazioni su Film o Serie.

  <details>
  <summary>Esempio Film: <a name="info-esempio-film" /></summary>

  ```
    {
        "name": "John Wick",
        "url": "https://streamingcommunity.esempio/titles/6-john-wick",
        "id": 6,
        "type": "Movie",
        "images": [
            {
                "id": 216,
                "filename": "f7887fba-d2d3-4252-b2e9-45129e1ecfd9.webp",
                "type": "poster",
                "imageable_type": "title",
                "imageable_id": 6,
                "created_at": "2023-05-18T11:48:50.000000Z",
                "updated_at": "2023-05-18T14:16:51.000000Z",
                "original_url_field": None,
            },
            {
                "id": 217,
                "filename": "3ca16987-4229-4369-ba0b-670e0ec2b4df.webp",
                "type": "background",
                "imageable_type": "title",
                "imageable_id": 6,
                "created_at": "2023-05-18T11:48:50.000000Z",
                "updated_at": "2023-05-18T14:16:51.000000Z",
                "original_url_field": None,
            },
        ],
        "year": 2014,
        "plot": "Dopo la morte dell'amata moglie, il leggendario ex assassino John Wick (Keanu Reeves) trascorre le giornate a rimettere in sesto la sua Ford Mustang del 1969 e con la sola compagnia del cane Daisy. La sua esistenza scivola via senza intoppi fino a quando un sadico delinquente di nome Yosef Tarasof nota la sua auto. Non accettando il rifiuto di venderla di Wick, Yosef manda due suoi complici a rubare la macchina e a uccidere brutalmente Daisy. Da quel momento, John si mette sulle tracce del criminale a New York, scoprendo di avere a che fare con l'unico figlio del boss della mala Viggo Tarasof. Quando in breve tempo per la città si diffonde la voce che John è in cerca di Yosef per vendicarsi, Viggo mette sulla sua testa una grande ricompensa, che attira tutti gli assassini in circolazione.",
        "tmdb_id": 245891,
        "imdb_id": "tt2911666",
        "netflix_id": 80013762,
        "prime_id": "0G58W0Q34J67V60W5XWF6BAVXM",
        "disney_id": None,
        "release_date": "2014-10-22",
        "sub_ita": None,
        "rating": 8000,
        "tags": ["Azione", "Thriller"],
        "duration": 136,
        "trailerUrl": "https://www.youtube.com/watch?v=N_ZPL3hmFEo",
        "recommendations": [
            {
                "id": 5981,
                "slug": "invito-a-cena-con-delitto",
                "name": "Invito a cena con delitto",
                "type": "movie",
                "score": "7.8",
                "sub_ita": 0,
                "last_air_date": "1976-06-23",
                "age": None,
                "seasons_count": 0,
                "images": [
                    {
                        "imageable_id": 5981,
                        "imageable_type": "title",
                        "filename": "19aabbad-784e-480c-b5d1-97bd3266eea4.webp",
                        "type": "poster",
                        "original_url_field": None,
                    },
                    {
                        "imageable_id": 5981,
                        "imageable_type": "title",
                        "filename": "85cd7753-4b33-4c73-ad42-f20689a67d69.webp",
                        "type": "background",
                        "original_url_field": None,
                    },
                ],
            },
            {
                "id": 10916,
                "slug": "absolution-storia-criminale",
                "name": "ABSOLUTION - STORIA CRIMINALE",
                "type": "movie",
                "score": "6.2",
                "sub_ita": 0,
                "last_air_date": "2024-10-31",
                "age": 18,
                "seasons_count": 0,
                "images": [
                    {
                        "imageable_id": 10916,
                        "imageable_type": "title",
                        "filename": "dde0111a-f0d9-4510-a85e-288e55059023.webp",
                        "type": "cover",
                        "original_url_field": None,
                    },
                    {
                        "imageable_id": 10916,
                        "imageable_type": "title",
                        "filename": "f2c04f2f-a940-43d1-9f60-7b754ad82c79.webp",
                        "type": "cover_mobile",
                        "original_url_field": None,
                    },
                ],
            },
        ],
    }
  ```

  </details>

  <details>
  <summary>Esempio Serie: <a name="info-esempio-serie" /></summary>

  ```
    {
        "name": "Scissione",
        "url": "https://streamingcommunity.esempio/titles/4937-scissione",
        "id": 4937,
        "type": "TvSeries",
        "episodeList": [
            {
                "name": "Buone notizie sull'inferno",
                "season": 1,
                "episode": 1,
                "description": "Mark viene promosso a capo del team di impiegati la cui memoria è stata chirurgicamente scissa per dividere i ricordi della vita lavorativa da quelli della vita privata.",
                "duration": 52,
                "images": [
                    {
                        "id": 144908,
                        "filename": "333170a8-9dfd-49d9-b5b2-565b97cb78c0.webp",
                        "type": "cover",
                        "imageable_type": "episode",
                        "imageable_id": 30088,
                        "created_at": "2024-12-12T16:44:40.000000Z",
                        "updated_at": "2024-12-12T16:44:40.000000Z",
                        "original_url_field": None,
                    }
                ],
                "url": "ParseResult(scheme='https', netloc='streamingcommunity.esempio', path='', params='', query='', fragment='')/watch/4937?e=30088",
                "id": 30088,
            },
            {
                "name": "Half Loop",
                "season": 1,
                "episode": 2,
                "description": "Il team forma la nuova assunta, Helly, sul lavoro di Macrodata Refinment. Mark si prende un giorno di pausa per incontrare un misterioso ex collega.",
                "duration": 47,
                "images": [
                    {
                        "id": 144909,
                        "filename": "51a84c9f-8691-4069-b74e-8e04245291b8.webp",
                        "type": "cover",
                        "imageable_type": "episode",
                        "imageable_id": 30089,
                        "created_at": "2024-12-12T16:44:48.000000Z",
                        "updated_at": "2024-12-12T16:44:48.000000Z",
                        "original_url_field": None,
                    }
                ],
                "url": "ParseResult(scheme='https', netloc='streamingcommunity.esempio', path='', params='', query='', fragment='')/watch/4937?e=30089",
                "id": 30089,
            },
            {
                "name": "Chi è vivo?",
                "season": 2,
                "episode": 3,
                "description": "Mark, Helly, Irving e Dylan cercano risposte.",
                "duration": 53,
                "images": [
                    {
                        "id": 149514,
                        "filename": "dd954958-6633-4221-97e9-3ec448758725.webp",
                        "type": "cover",
                        "imageable_type": "episode",
                        "imageable_id": 84347,
                        "created_at": "2025-01-31T02:10:31.000000Z",
                        "updated_at": "2025-01-31T02:10:31.000000Z",
                        "original_url_field": None,
                    }
                ],
                "url": "ParseResult(scheme='https', netloc='streamingcommunity.esempio', path='', params='', query='', fragment='')/watch/4937?e=84347",
                "id": 84347,
            },
            {
                "name": "La Valle del Dolore",
                "season": 2,
                "episode": 4,
                "description": "Il team partecipa a un'attività di gruppo.",
                "duration": 50,
                "images": [
                    {
                        "id": 150044,
                        "filename": "01f322e9-2534-46bc-a55c-b29152298d82.webp",
                        "type": "cover",
                        "imageable_type": "episode",
                        "imageable_id": 84509,
                        "created_at": "2025-02-07T02:08:31.000000Z",
                        "updated_at": "2025-02-07T02:08:31.000000Z",
                        "original_url_field": None,
                    }
                ],
                "url": "ParseResult(scheme='https', netloc='streamingcommunity.esempio', path='', params='', query='', fragment='')/watch/4937?e=84509",
                "id": 84509,
            },
        ],
        "images": [
            {
                "id": 155419,
                "filename": "c0e66fa5-9d20-47cf-aee4-7a1a7eb3d9ce.webp",
                "type": "cover",
                "imageable_type": "title",
                "imageable_id": 4937,
                "created_at": "2025-03-13T18:37:16.000000Z",
                "updated_at": "2025-03-13T18:37:16.000000Z",
                "original_url_field": None,
            },
            {
                "id": 155420,
                "filename": "dd1fdc3e-bd17-4791-a8b0-57e16b30aadb.webp",
                "type": "cover_mobile",
                "imageable_type": "title",
                "imageable_id": 4937,
                "created_at": "2025-03-13T18:37:16.000000Z",
                "updated_at": "2025-03-13T18:37:16.000000Z",
                "original_url_field": None,
            },
        ],
        "year": 2022,
        "plot": "In questa serie vincitrice del premio Emmy diretta da Ben Stiller, Mark guida un team di impiegati la cui memoria è stata chirurgicamente scissa per dividere i ricordi della vita lavorativa da quelli della vita privata. Gli impiegati iniziano un viaggio alla scoperta della verità riguardo al loro lavoro e se stessi.",
        "tmdb_id": 95396,
        "imdb_id": "tt11280740",
        "netflix_id": None,
        "prime_id": None,
        "disney_id": None,
        "release_date": "2022-02-18",
        "sub_ita": None,
        "rating": 8700,
        "seasons_count": 2,
        "tags": ["Dramma", "Sci-Fi & Fantasy", "Mistero"],
        "trailerUrl": "https://www.youtube.com/watch?v=gHUPGia32y4",
        "recommendations": [
            {
                "id": 10623,
                "slug": "the-madness",
                "name": "The Madness",
                "type": "tv",
                "score": "6.9",
                "sub_ita": 0,
                "last_air_date": "2024-11-28",
                "age": 16,
                "seasons_count": 1,
                "images": [
                    {
                        "imageable_id": 10623,
                        "imageable_type": "title",
                        "filename": "a002ecd7-4218-472c-b909-0f80c057b933.webp",
                        "type": "logo",
                        "original_url_field": None,
                    },
                    {
                        "imageable_id": 10623,
                        "imageable_type": "title",
                        "filename": "d77b621a-6cc9-4c7c-9380-682cfb027b46.webp",
                        "type": "background",
                        "original_url_field": None,
                    },
                ],
            },
            {
                "id": 5010,
                "slug": "shining-girls",
                "name": "Shining Girls",
                "type": "tv",
                "score": "7.6",
                "sub_ita": 0,
                "last_air_date": "2022-04-29",
                "age": 12,
                "seasons_count": 1,
                "images": [
                    {
                        "imageable_id": 5010,
                        "imageable_type": "title",
                        "filename": "ee0b09c6-3fcc-4ae8-9aac-c1abe8b7b9b4.webp",
                        "type": "poster",
                        "original_url_field": None,
                    },
                    {
                        "imageable_id": 5010,
                        "imageable_type": "title",
                        "filename": "ec20c1ca-8450-4c45-80ec-38e379d66a29.webp",
                        "type": "background",
                        "original_url_field": None,
                    },
                ],
            },
        ],
    }

  ```

   </details>

- ### Link Iframe (embed) e Playlist m3u8 <a name="getlinks" />

  ```python
  from scuapi import API

  sc = API('StreamingCommunity.esempio')

  # Film
  iframe, m3u_playlist_url = sc.get_links('7540')
  iframe, m3u_playlist_url = sc.get_links(7540)
  iframe, m3u_playlist_url, m3u_playlist_file = sc.get_links('7540', get_m3u=True)
  # Serie
  iframe, m3u_playlist_url = sc.get_links('7540', '50636')
  iframe, m3u_playlist_url = sc.get_links(7540, 50636)
  iframe, m3u_playlist_url, m3u_playlist_file = sc.get_links('7540', '50636', get_m3u=True)
  iframe, m3u_playlist_url, m3u_playlist_file = sc.get_links('7540', episode_id='50636', get_m3u=True)
  ```

  #### Esempio Risultati Link

  ```
  ('https://esempio.com/embed/187503?token=c250fa66452196905729239d0630fc28&title=Hazbin+Hotel&referer=1&expires=1712698824&description=S1%3AE1+Ouverture&nextEpisode=1&b=1',
  'https://esempio.com/playlist/187503?token=_SZhU9hVpDBU1Eld1p8PGQ&token=_SZhU9hVpDBU1Eld1p8PGQ&token480p=fkHMJTm4hOTW1yxBenQ8Vw&token720p=D9AarDND8u2sypbB11ApCA&expires=1712698824')
  ```

## Download Video <a name="download-video" />

I video possono essere scricati con il [plugin per yt-dlp](https://github.com/Blu-Tiger/StreamingCommunity-yt-dlp-plugin) usando il link dell'episodio.
