A simple unofficial api for the italian StreamingCommunity website.

![Static Badge](https://img.shields.io/badge/version-2.0.1-green?style=for-the-badge) ![Static Badge](https://img.shields.io/badge/23%2F12%2F2024-Working-green?style=for-the-badge)

[![PyPI](https://img.shields.io/pypi/v/streamingcommunity-unofficialapi?style=flat)](https://pypi.org/project/streamingcommunity-unofficialapi/)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/w/Blu-Tiger/streamingcommunity-unofficialapi?style=flat)
![PyPI - Downloads](https://img.shields.io/pypi/dd/streamingcommunity-unofficialapi?style=flat)
![PyPI - Downloads](https://img.shields.io/pypi/dw/streamingcommunity-unofficialapi?style=flat)
![PyPI - Downloads](https://img.shields.io/pypi/dm/streamingcommunity-unofficialapi?style=flat)

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
      "name": "John Wick 4",
      "url": "StreamingCommunity.esempio/titles/6203-john-wick-4",
      "scws_id": 157670,
      "type": "Movie",
      "images": [
          {
              "id": 62111,
              "filename": "8babb029-90b3-4237-aff2-2395b2dfb5ce.webp",
              "type": "cover_mobile",
              "imageable_type": "title",
              "imageable_id": 6203,
              "created_at": "2023-05-18T13:35:15.000000Z",
              "updated_at": "2023-05-18T13:35:15.000000Z",
              "original_url_field": None,
          },
          {
              "id": 66322,
              "filename": "64934c02-794f-4307-a860-758eed06b717.webp",
              "type": "logo",
              "imageable_type": "title",
              "imageable_id": 6203,
              "created_at": "2023-05-18T13:54:10.000000Z",
              "updated_at": "2023-05-18T18:24:23.000000Z",
              "original_url_field": None,
          },
          {
              "id": 66600,
              "filename": "6e08fcb2-59c4-4024-99f6-8b11843c7d86.webp",
              "type": "background",
              "imageable_type": "title",
              "imageable_id": 6203,
              "created_at": "2023-05-24T04:33:08.000000Z",
              "updated_at": "2023-05-24T04:33:08.000000Z",
              "original_url_field": None,
          },
          {
              "id": 66601,
              "filename": "91c3b096-4636-4cea-bdcf-80dc2740fe96.webp",
              "type": "poster",
              "imageable_type": "title",
              "imageable_id": 6203,
              "created_at": "2023-05-24T04:33:08.000000Z",
              "updated_at": "2023-05-24T04:33:08.000000Z",
              "original_url_field": None,
          },
          {
              "id": 66602,
              "filename": "3a9b0a6b-92f7-4c2d-94b8-8ecd5e5e48be.webp",
              "type": "cover",
              "imageable_type": "title",
              "imageable_id": 6203,
              "created_at": "2023-05-24T04:33:08.000000Z",
              "updated_at": "2023-05-24T04:33:08.000000Z",
              "original_url_field": None,
          },
          {
              "id": 66603,
              "filename": "3a3bae1a-b7a3-4bc2-afd1-eabe2d0f31ef.webp",
              "type": "cover_mobile",
              "imageable_type": "title",
              "imageable_id": 6203,
              "created_at": "2023-05-24T04:33:08.000000Z",
              "updated_at": "2023-05-24T04:33:08.000000Z",
              "original_url_field": None,
          },
      ],
      "year": 2023,
      "plot": "John Wick trova una via per sconfiggere la Gran Tavola. Ma prima di guadagnare la libertà, Wick deve affrontare un nuovo nemico che ha potenti alleanze in tutto il mondo e ha mezzi tali da tramutare vecchi amici in nuovi nemici.",
      "tmdb_id": 603692,
      "imdb_id": "tt10366206",
      "netflix_id": None,
      "prime_id": None,
      "disney_id": None,
      "release_date": "2023-03-22",
      "sub_ita": False,
      "rating": 8100,
      "tags": ["Crime", "Azione", "Thriller"],
      "duration": 169,
      "trailerUrl": "https://www.youtube.com/watch?v=049RtZzgAtA",
      "recommendations": [
          {
              "id": 10677,
              "slug": "salt",
              "name": "Salt",
              "type": "movie",
              "score": "6.9",
              "sub_ita": 0,
              "last_air_date": "2010-07-21",
              "age": 12,
              "seasons_count": 0,
              "images": [
                  {
                      "imageable_id": 10677,
                      "imageable_type": "title",
                      "filename": "ba9fef9d-fa7e-4d86-876d-a2e9fdebe9eb.webp",
                      "type": "poster",
                      "original_url_field": None,
                  },
                  {
                      "imageable_id": 10677,
                      "imageable_type": "title",
                      "filename": "b635c8c4-aa08-45a0-978e-4367894b87c5.webp",
                      "type": "cover",
                      "original_url_field": None,
                  },
                  {
                      "imageable_id": 10677,
                      "imageable_type": "title",
                      "filename": "8abaf974-3d11-401b-9811-6a4b19403cf9.webp",
                      "type": "cover_mobile",
                      "original_url_field": None,
                  },
                  {
                      "imageable_id": 10677,
                      "imageable_type": "title",
                      "filename": "88f700a3-c9c0-430d-8633-63fe5e0196c5.webp",
                      "type": "background",
                      "original_url_field": None,
                  },
                  {
                      "imageable_id": 10677,
                      "imageable_type": "title",
                      "filename": "3db9bd79-5a6f-4459-ad79-0d884b7a177b.webp",
                      "type": "logo",
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
      "name": "Hazbin Hotel",
      "url": "https://StreamingCommunity.esempio/titles/7540-hazbin-hotel",
      "type": "TvSeries",
      "episodeList": [
          {
              "name": "Ouverture",
              "season": 1,
              "episode": 1,
              "description": "Charlie presenta al Paradiso il suo piano per salvare i peccatori redimendoli nel suo hotel. Vaggie coinvolge lo staff nella realizzazione di uno spot per promuovere l'hotel.",
              "duration": 25,
              "images": [
                  {
                      "id": 88291,
                      "filename": "6daa820e-0c15-48ad-a93d-1896e229e37a.webp",
                      "type": "cover",
                      "imageable_type": "episode",
                      "imageable_id": 50635,
                      "created_at": "2024-01-19T02:54:02.000000Z",
                      "updated_at": "2024-01-19T02:54:02.000000Z",
                      "original_url_field": None,
                  }
              ],
              "url": "ParseResult(scheme='https', netloc='StreamingCommunity.esempio', path='', params='', query='', fragment='')/watch/7540?e=50635",
              "scws_id": 187503,
          },
          {
              "name": "La radio ha ucciso la televisione",
              "season": 1,
              "episode": 2,
              "description": "I Vee: Vox, Velvette e Valentino governano il loro angolo dell'Inferno incontrastati, ma il ritorno di Alastor nell'etere potrebbe smuovere le cose. Nel frattempo, un nuovo ospite dell'hotel mette alla prova la pazienza di Angel.",
              "duration": 25,
              "images": [
                  {
                      "id": 88292,
                      "filename": "4e714841-c4fc-447a-aac5-c5d70ed3cf0c.webp",
                      "type": "cover",
                      "imageable_type": "episode",
                      "imageable_id": 50636,
                      "created_at": "2024-01-19T02:54:03.000000Z",
                      "updated_at": "2024-01-19T02:54:03.000000Z",
                      "original_url_field": None,
                  }
              ],
              "url": "ParseResult(scheme='https', netloc='StreamingCommunity.esempio', path='', params='', query='', fragment='')/watch/7540?e=50636",
              "scws_id": 187504,
          },
          {
              "name": "Uova strapazzate",
              "season": 1,
              "episode": 3,
              "description": "Mentre gli ospiti ed il personale dell'Hotel trascorrono la giornata ad apprendere la fiducia, informazioni rivelate ad una riunione fra i signori supremi portano ad una lite irrispettosa.",
              "duration": 24,
              "images": [
                  {
                      "id": 88293,
                      "filename": "96e2811d-9bb9-4d8c-bf4f-7d886283585d.webp",
                      "type": "cover",
                      "imageable_type": "episode",
                      "imageable_id": 50637,
                      "created_at": "2024-01-19T02:54:05.000000Z",
                      "updated_at": "2024-01-19T02:54:05.000000Z",
                      "original_url_field": None,
                  }
              ],
              "url": "ParseResult(scheme='https', netloc='StreamingCommunity.esempio', path='', params='', query='', fragment='')/watch/7540?e=50637",
              "scws_id": 187505,
          },
          {
              "name": "Messinscena",
              "season": 1,
              "episode": 4,
              "description": "Angel fatica a destreggiarsi tra il suo lavoro e il suo tempo all'hotel. Charlie decide che è ora di usare il suo status di Principessa con il capo di Angel.",
              "duration": 24,
              "images": [
                  {
                      "id": 88294,
                      "filename": "d33f5488-b77e-4c8d-a59e-2319c811bbf3.webp",
                      "type": "cover",
                      "imageable_type": "episode",
                      "imageable_id": 50638,
                      "created_at": "2024-01-19T02:54:07.000000Z",
                      "updated_at": "2024-01-19T02:54:07.000000Z",
                      "original_url_field": None,
                  }
              ],
              "url": "ParseResult(scheme='https', netloc='StreamingCommunity.esempio', path='', params='', query='', fragment='')/watch/7540?e=50638",
              "scws_id": 187506,
          },
          {
              "name": "Papà batte papà",
              "season": 1,
              "episode": 5,
              "description": "Charlie è combattuta nel chiedere aiuto a suo padre, Lucifero. Nel frattempo, un nuovo arrivo inatteso movimenta le cose all'Hotel.",
              "duration": 25,
              "images": [
                  {
                      "id": 91383,
                      "filename": "a360fcd5-b40a-4aef-be3d-7c2fa7da9bbd.webp",
                      "type": "cover",
                      "imageable_type": "episode",
                      "imageable_id": 51656,
                      "created_at": "2024-01-26T06:35:02.000000Z",
                      "updated_at": "2024-01-26T06:35:02.000000Z",
                      "original_url_field": None,
                  }
              ],
              "url": "ParseResult(scheme='https', netloc='StreamingCommunity.esempio', path='', params='', query='', fragment='')/watch/7540?e=51656",
              "scws_id": 192160,
          },
          {
              "name": "Benvenute in Paradiso",
              "season": 1,
              "episode": 6,
              "description": "Charlie e Vaggie riescono a raggiungere il Paradiso per parlare con il capo di Adamo. Nel frattempo, una rimpatriata esplosiva dà ad Angel l'opportunità di mostrare quanta strada ha fatto.",
              "duration": 25,
              "images": [
                  {
                      "id": 91384,
                      "filename": "cfb5d01a-3e27-47c7-92e4-a335496d3957.webp",
                      "type": "cover",
                      "imageable_type": "episode",
                      "imageable_id": 51657,
                      "created_at": "2024-01-26T06:35:04.000000Z",
                      "updated_at": "2024-01-26T06:35:04.000000Z",
                      "original_url_field": None,
                  }
              ],
              "url": "ParseResult(scheme='https', netloc='StreamingCommunity.esempio', path='', params='', query='', fragment='')/watch/7540?e=51657",
              "scws_id": 192161,
          },
          {
              "name": "Ciao Rosie!",
              "season": 1,
              "episode": 7,
              "description": "Con i segreti rivelati e l'Hotel nel mirino, Charlie e Vaggie devono fare il possibile per proteggere la loro casa dalla distruzione con ogni mezzo necessario.",
              "duration": 25,
              "images": [
                  {
                      "id": 91924,
                      "filename": "848da78a-954a-458c-8dcd-5f5fdb9a88cd.webp",
                      "type": "cover",
                      "imageable_type": "episode",
                      "imageable_id": 51885,
                      "created_at": "2024-02-02T12:21:05.000000Z",
                      "updated_at": "2024-02-02T12:21:05.000000Z",
                      "original_url_field": None,
                  }
              ],
              "url": "ParseResult(scheme='https', netloc='StreamingCommunity.esempio', path='', params='', query='', fragment='')/watch/7540?e=51885",
              "scws_id": 199946,
          },
          {
              "name": "Lo spettacolo deve continuare",
              "season": 1,
              "episode": 8,
              "description": "Nel finale di stagione, succede di tutto, mentre lo scontro tra le legioni del Paradiso e dell'Inferno ha inizio.",
              "duration": 25,
              "images": [
                  {
                      "id": 91923,
                      "filename": "da8ea904-10ba-4312-b09b-32e78cf361c6.webp",
                      "type": "cover",
                      "imageable_type": "episode",
                      "imageable_id": 51884,
                      "created_at": "2024-02-02T12:21:02.000000Z",
                      "updated_at": "2024-02-02T12:21:02.000000Z",
                      "original_url_field": None,
                  }
              ],
              "url": "ParseResult(scheme='https', netloc='StreamingCommunity.esempio', path='', params='', query='', fragment='')/watch/7540?e=51884",
              "scws_id": 199947,
          },
      ],
      "images": [
          {
              "id": 88287,
              "filename": "cf42bff9-41dc-4710-be80-cbc91ac6686c.webp",
              "type": "logo",
              "imageable_type": "title",
              "imageable_id": 7540,
              "created_at": "2024-01-19T02:52:11.000000Z",
              "updated_at": "2024-01-19T02:52:11.000000Z",
              "original_url_field": None,
          },
          {
              "id": 88288,
              "filename": "d79bac25-35d5-4cae-9543-3f7380260ff8.webp",
              "type": "cover_mobile",
              "imageable_type": "title",
              "imageable_id": 7540,
              "created_at": "2024-01-19T02:53:52.000000Z",
              "updated_at": "2024-01-19T02:53:52.000000Z",
              "original_url_field": None,
          },
          {
              "id": 88289,
              "filename": "4ba17e65-c47b-41cb-833c-2fc5e640bad0.webp",
              "type": "cover",
              "imageable_type": "title",
              "imageable_id": 7540,
              "created_at": "2024-01-19T02:53:52.000000Z",
              "updated_at": "2024-01-19T02:53:52.000000Z",
              "original_url_field": None,
          },
          {
              "id": 88290,
              "filename": "ca6cbc7b-4d05-4d23-bc35-cef0aafd33b4.webp",
              "type": "background",
              "imageable_type": "title",
              "imageable_id": 7540,
              "created_at": "2024-01-19T02:53:52.000000Z",
              "updated_at": "2024-01-19T02:53:52.000000Z",
              "original_url_field": None,
          },
          {
              "id": 89554,
              "filename": "d06f117f-d3c6-43ef-9d9a-9d99543387ad.webp",
              "type": "poster",
              "imageable_type": "title",
              "imageable_id": 7540,
              "created_at": "2024-01-19T11:44:35.000000Z",
              "updated_at": "2024-01-19T11:44:35.000000Z",
              "original_url_field": None,
          },
      ],
      "year": 2024,
      "plot": "Charlie. Stella del Mattino, la Principessa dell'Inferno, fatica a convincere sia i demoni che gli angeli che ogni anima possa essere redenta. Cantate e imprecate con noi in questa commedia musicale animata per adulti sul tema delle seconde chance.",
      "tmdb_id": 94954,
      "imdb_id": "tt7216636",
      "netflix_id": None,
      "prime_id": "0HZWTBZYQQXYW48YBANMDM2MZE",
      "disney_id": None,
      "release_date": "2024-01-18",
      "sub_ita": False,
      "rating": 8700,
      "seasons_count": 1,
      "tags": ["Commedia", "Animazione"],
      "trailerUrl": "https://www.youtube.com/watch?v=u-zpwEA7ceY",
      "recommendations": [
          {
              "id": 8166,
              "slug": "angel",
              "name": "Angel",
              "type": "tv",
              "score": "8.3",
              "sub_ita": 0,
              "last_air_date": "1999-10-05",
              "age": 13,
              "seasons_count": 5,
              "images": [
                  {
                      "imageable_id": 8166,
                      "imageable_type": "title",
                      "filename": "c836c83c-33ca-4ee7-83a0-3e0d5d1e6ead.webp",
                      "type": "background",
                      "original_url_field": None,
                  },
                  {
                      "imageable_id": 8166,
                      "imageable_type": "title",
                      "filename": "13475346-adb4-4032-875a-954f3ff0498c.webp",
                      "type": "logo",
                      "original_url_field": None,
                  },
                  {
                      "imageable_id": 8166,
                      "imageable_type": "title",
                      "filename": "333b626d-6e0c-42f2-b136-62108181d449.webp",
                      "type": "poster",
                      "original_url_field": None,
                  },
                  {
                      "imageable_id": 8166,
                      "imageable_type": "title",
                      "filename": "eab1cf97-3d43-4fc3-b896-10bd0c275510.webp",
                      "type": "cover",
                      "original_url_field": None,
                  },
                  {
                      "imageable_id": 8166,
                      "imageable_type": "title",
                      "filename": "33bda01b-ffdd-46bf-b623-f29501b5b307.webp",
                      "type": "cover_mobile",
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

  iframe, m3u8_playlist = sc.get_links('https://StreamingCommunity.esempio/watch/7540?e=50636')
  ```

  #### Esempio Risultati Link

  ```
  ('https://esempio.com/embed/187503?token=c250fa66452196905729239d0630fc28&title=Hazbin+Hotel&referer=1&expires=1712698824&description=S1%3AE1+Ouverture&nextEpisode=1&b=1',
  'https://esempio.com/playlist/187503?token=_SZhU9hVpDBU1Eld1p8PGQ&token=_SZhU9hVpDBU1Eld1p8PGQ&token480p=fkHMJTm4hOTW1yxBenQ8Vw&token720p=D9AarDND8u2sypbB11ApCA&expires=1712698824')
  ```

## Download Video <a name="download-video" />

I video possono essere scricati con il [plugin per yt-dlp](https://github.com/Blu-Tiger/StreamingCommunity-yt-dlp-plugin) usando il link dell'episodio.
