A simple unofficial api for the italian StreamingCommunity website.


![PyPI](https://img.shields.io/pypi/v/streamingcommunity-unofficialapi)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/w/Blu-Tiger/streamingcommunity-unofficialapi)

![PyPI - Downloads](https://img.shields.io/pypi/dd/streamingcommunity-unofficialapi)
![PyPI - Downloads](https://img.shields.io/pypi/dw/streamingcommunity-unofficialapi)
![PyPI - Downloads](https://img.shields.io/pypi/dd/streamingcommunity-unofficialapi)


# StreamingCommunity-API

## Installazione

Questa libreria richiede [Python 3.10](https://www.python.org/) o superiore.

È Possibile installarare la libreria tramite pip:


```
pip install streamingcommunity-unofficialapi
```


## Utilizzo

Per iniziare bisona impostare il dominio di StreamingCommunity che si desidera utilizzare.
```
from scuapi import API

sc = API('StreamingCommunity.esempio')

```

### Ricerca
Per ricercare un Film o una Serie per nome nel sito di StreamingCommunity è possibile usare la funzione search().

```
from scuapi import API

sc = API('StreamingCommunity.esempio')
sc.search('John Wick')

```

La funzione restituirà un dizionario contentente per chiave il nome del Film o Serie e per valore un dizionario contenente tutte le informazioni correllate.

#### Esempio:
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

### Info Film/Serie

Per ottenere informazioni su un Film o una Serie è possibile usare la funzione load().

```
from scuapi import API

sc = API('StreamingCommunity.esempio')
sc.load('https://StreamingCommunity.esempio/titles/6203-john-wick-4')
```

La funzione restituirà un dizionario contentente tutte le informazioni su Film o Serie.

#### Esempio:
```
{
    "name": "John Wick 4",
    "url": "https://StreamingCommunity.esempio/watch/6203",
    "scws_id": 157670,
    "type": "Movie",
    "posterUrl": "https://cdn.StreamingCommunity.esempio/images/8babb029-90b3-4237-aff2-2395b2dfb5ce.webp",
    "year": 2023,
    "plot": "John Wick trova una via per sconfiggere la Gran Tavola. Ma prima di guadagnare la libertà, Wick deve affrontare un nuovo nemico che ha potenti alleanze in tutto il mondo e ha mezzi tali da tramutare vecchi amici in nuovi nemici.",
    "tmdb_id": 603692,
    "imdb_id": "tt10366206",
    "netflix_id": None,
    "prime_id": None,
    "disney_id": None,
    "release_date": "2023-03-22",
    "sub_ita": False,
    "rating": 8600,
    "tags": ["Crime", "Azione", "Thriller"],
    "duration": 169,
    "trailerUrl": "https://www.youtube.com/watch?v=049RtZzgAtA",
    "recommendations": [
        {
            "id": 5077,
            "slug": "luomo-ombra",
            "name": "L'uomo ombra",
            "type": "movie",
            "score": "6.0",
            "sub_ita": 0,
            "last_air_date": "1994-07-01",
            "seasons_count": 0,
            "images": [
                {
                    "imageable_id": 5077,
                    "imageable_type": "title",
                    "filename": "125664cb-82c6-403b-a262-916080307f77.webp",
                    "type": "poster",
                    "original_url_field": None,
                },
                {
                    "imageable_id": 5077,
                    "imageable_type": "title",
                    "filename": "1666007b-f7df-4308-910b-4e4ae414f35a.webp",
                    "type": "background",
                    "original_url_field": None,
                }
            ],
        },
        {
            "id": 1636,
            "slug": "il-padrino",
            "name": "Il padrino",
            "type": "movie",
            "score": "9.2",
            "sub_ita": 0,
            "last_air_date": "1972-03-14",
            "seasons_count": 0,
            "images": [
                {
                    "imageable_id": 1636,
                    "imageable_type": "title",
                    "filename": "37beda03-f1c5-4958-9456-b696b9d8918f.webp",
                    "type": "cover",
                    "original_url_field": None,
                },
                {
                    "imageable_id": 1636,
                    "imageable_type": "title",
                    "filename": "d6bf67db-6644-4381-a3a1-7d5a75b393c6.webp",
                    "type": "cover_mobile",
                    "original_url_field": None,
                }
            ],
        }
    ],
}

```

### Download link

In progresso.