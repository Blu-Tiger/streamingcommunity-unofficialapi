A simple unofficial api for the italian StreamingCommunity website.

![Static Badge](https://img.shields.io/badge/3%2F2%2F2023-Working-green?style=for-the-badge)


![PyPI](https://img.shields.io/pypi/v/streamingcommunity-unofficialapi?style=flat)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/w/Blu-Tiger/streamingcommunity-unofficialapi?style=flat)

![PyPI - Downloads](https://img.shields.io/pypi/dd/streamingcommunity-unofficialapi?style=flat)
![PyPI - Downloads](https://img.shields.io/pypi/dw/streamingcommunity-unofficialapi?style=flat)
![PyPI - Downloads](https://img.shields.io/pypi/dm/streamingcommunity-unofficialapi?style=flat)


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

#### Esempio Film:
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

#### Esempio Serie:
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

### Info Film/Serie

Per ottenere informazioni su un Film o una Serie è possibile usare la funzione load().

```
from scuapi import API

sc = API('StreamingCommunity.esempio')
sc.load('https://StreamingCommunity.esempio/titles/6203-john-wick-4')
```

La funzione restituirà un dizionario contentente tutte le informazioni su Film o Serie.

#### Esempio Film:
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

#### Esempio Serie:
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
      "posterUrl": "https://cdn.StreamingCommunity.esempio/images/6daa820e-0c15-48ad-a93d-1896e229e37a.webp",
      "url": "https://StreamingCommunity.esempio/watch/7540?e=50635",
      "scws_id": 187503
    },
    {
      "name": "La radio ha ucciso la televisione",
      "season": 1,
      "episode": 2,
      "description": "I Vee: Vox, Velvette e Valentino governano il loro angolo dell'Inferno incontrastati, ma il ritorno di Alastor nell'etere potrebbe smuovere le cose. Nel frattempo, un nuovo ospite dell'hotel mette alla prova la pazienza di Angel.",
      "duration": 25,
      "posterUrl": "https://cdn.StreamingCommunity.esempio/images/4e714841-c4fc-447a-aac5-c5d70ed3cf0c.webp",
      "url": "https://StreamingCommunity.esempio/watch/7540?e=50636",
      "scws_id": 187504
    },
    {
      "name": "Uova strapazzate",
      "season": 1,
      "episode": 3,
      "description": "Mentre gli ospiti ed il personale dell'Hotel trascorrono la giornata ad apprendere la fiducia, informazioni rivelate ad una riunione fra i signori supremi portano ad una lite irrispettosa.",
      "duration": 24,
      "posterUrl": "https://cdn.StreamingCommunity.esempio/images/96e2811d-9bb9-4d8c-bf4f-7d886283585d.webp",
      "url": "https://StreamingCommunity.esempio/watch/7540?e=50637",
      "scws_id": 187505
    },
    {
      "name": "Messinscena",
      "season": 1,
      "episode": 4,
      "description": "Angel fatica a destreggiarsi tra il suo lavoro e il suo tempo all'hotel. Charlie decide che \\u00e8 ora di usare il suo status di Principessa con il capo di Angel.",
      "duration": 24,
      "posterUrl": "https://cdn.StreamingCommunity.esempio/images/d33f5488-b77e-4c8d-a59e-2319c811bbf3.webp",
      "url": "https://StreamingCommunity.esempio/watch/7540?e=50638",
      "scws_id": 187506
    },
    {
      "name": "Pap\\u00e0 batte pap\\u00e0",
      "season": 1,
      "episode": 5,
      "description": "Charlie \\u00e8 combattuta nel chiedere aiuto a suo padre, Lucifero. Nel frattempo, un nuovo arrivo inatteso movimenta le cose all'Hotel.",
      "duration": 25,
      "posterUrl": "https://cdn.StreamingCommunity.esempio/images/a360fcd5-b40a-4aef-be3d-7c2fa7da9bbd.webp",
      "url": "https://StreamingCommunity.esempio/watch/7540?e=51656",
      "scws_id": 192160
    },
    {
      "name": "Benvenute in Paradiso",
      "season": 1,
      "episode": 6,
      "description": "Charlie e Vaggie riescono a raggiungere il Paradiso per parlare con il capo di Adamo. Nel frattempo, una rimpatriata esplosiva d\\u00e0 ad Angel l'opportunit\\u00e0 di mostrare quanta strada ha fatto.",
      "duration": 25,
      "posterUrl": "https://cdn.StreamingCommunity.esempio/images/cfb5d01a-3e27-47c7-92e4-a335496d3957.webp",
      "url": "https://StreamingCommunity.esempio/watch/7540?e=51657",
      "scws_id": 192161
    }
  ],
  "posterUrl": "https://cdn.StreamingCommunity.esempio/images/d79bac25-35d5-4cae-9543-3f7380260ff8.webp",
  "year": 2024,
  "plot": "Charlie. Stella del Mattino, la Principessa dell'Inferno, fatica a convincere sia i demoni che gli angeli che ogni anima possa essere redenta. Cantate e imprecate con noi in questa commedia musicale animata per adulti sul tema delle seconde chance.",
  "tmdb_id": 94954,
  "imdb_id": null,
  "netflix_id": null,
  "prime_id": "0HZWTBZYQQXYW48YBANMDM2MZE",
  "disney_id": null,
  "release_date": "2024-01-18",
  "sub_ita": false,
  "rating": 9200,
  "seasons_count": 1,
  "tags": ["Commedia", "Animazione"],
  "trailerUrl": "https://www.youtube.com/watch?v=u-zpwEA7ceY",
  "recommendations": [
    {
      "id": 1348,
      "slug": "brickleberry",
      "name": "Brickleberry",
      "type": "tv",
      "score": "7.9",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 3,
      "images": [
        {
          "imageable_id": 1348,
          "imageable_type": "title",
          "filename": "b81a5ff7-9054-4964-99fb-8f1024d2fbd1.webp",
          "type": "poster",
          "original_url_field": null
        },
        {
          "imageable_id": 1348,
          "imageable_type": "title",
          "filename": "76aed4ab-7361-4872-b85a-b2d92cb5514c.webp",
          "type": "background",
          "original_url_field": null
        },
        {
          "imageable_id": 1348,
          "imageable_type": "title",
          "filename": "3c5663dd-2c5c-42e1-9792-31e394837c51.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 1348,
          "imageable_type": "title",
          "filename": "212c4158-834f-4ae9-a074-f08941027184.webp",
          "type": "cover_mobile",
          "original_url_field": null
        }
      ]
    },
    {
      "id": 4760,
      "slug": "erase-una-vez-pero-ya-no",
      "name": "Erase una vez... Pero ya no",
      "type": "tv",
      "score": "7.3",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 1,
      "images": [
        {
          "imageable_id": 4760,
          "imageable_type": "title",
          "filename": "eb004804-c092-4414-bd8d-a076180742c1.webp",
          "type": "poster",
          "original_url_field": null
        },
        {
          "imageable_id": 4760,
          "imageable_type": "title",
          "filename": "67b84954-1cce-458a-876f-210658bf115d.webp",
          "type": "background",
          "original_url_field": null
        },
        {
          "imageable_id": 4760,
          "imageable_type": "title",
          "filename": "4683ff2f-4fd3-4280-aad5-a839a3c25965.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 4760,
          "imageable_type": "title",
          "filename": "16b4b1d4-c63d-4b19-aebf-b59652cc9cad.webp",
          "type": "cover_mobile",
          "original_url_field": null
        },
        {
          "imageable_id": 4760,
          "imageable_type": "title",
          "filename": "38d6c989-5a77-4f3f-bcd1-729be0da5e6a.webp",
          "type": "logo",
          "original_url_field": null
        }
      ]
    },
    {
      "id": 4734,
      "slug": "mezzanotte-a-istanbul",
      "name": "Mezzanotte a Istanbul",
      "type": "tv",
      "score": "7.5",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 1,
      "images": [
        {
          "imageable_id": 4734,
          "imageable_type": "title",
          "filename": "6f6cacba-10e1-4d19-b84c-480bb251fa97.webp",
          "type": "poster",
          "original_url_field": null
        },
        {
          "imageable_id": 4734,
          "imageable_type": "title",
          "filename": "c6a89ba9-cf48-4607-bdd8-c6598f65088f.webp",
          "type": "background",
          "original_url_field": null
        },
        {
          "imageable_id": 4734,
          "imageable_type": "title",
          "filename": "1637828b-5712-47f7-9c7f-9a0da7f4a642.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 4734,
          "imageable_type": "title",
          "filename": "6cc429e5-362d-4577-8110-4034a84d95b9.webp",
          "type": "cover_mobile",
          "original_url_field": null
        },
        {
          "imageable_id": 4734,
          "imageable_type": "title",
          "filename": "b79da36c-5f49-407d-8232-8ae7e44c4457.webp",
          "type": "logo",
          "original_url_field": null
        }
      ]
    },
    {
      "id": 3156,
      "slug": "violetta",
      "name": "Violetta",
      "type": "tv",
      "score": "7.6",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 3,
      "images": [
        {
          "imageable_id": 3156,
          "imageable_type": "title",
          "filename": "fb0d8a03-cd05-4bc5-a2e7-fc936d4a9b1d.webp",
          "type": "poster",
          "original_url_field": null
        },
        {
          "imageable_id": 3156,
          "imageable_type": "title",
          "filename": "e8369aca-3812-4aee-8118-d6295f9ce864.webp",
          "type": "background",
          "original_url_field": null
        },
        {
          "imageable_id": 3156,
          "imageable_type": "title",
          "filename": "07226748-7f8d-46d7-8126-d12f3cb23928.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 3156,
          "imageable_type": "title",
          "filename": "831d6590-0f75-4fdf-a506-cf634d0cc8a1.webp",
          "type": "cover_mobile",
          "original_url_field": null
        }
      ]
    },
    {
      "id": 5267,
      "slug": "farzar",
      "name": "Farzar",
      "type": "tv",
      "score": "6.0",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 1,
      "images": [
        {
          "imageable_id": 5267,
          "imageable_type": "title",
          "filename": "9fa2fb7f-a1df-45b9-8869-3ef577403c9f.webp",
          "type": "poster",
          "original_url_field": null
        },
        {
          "imageable_id": 5267,
          "imageable_type": "title",
          "filename": "dfe97601-f2a0-4873-aeeb-f16c811cda26.webp",
          "type": "background",
          "original_url_field": null
        },
        {
          "imageable_id": 5267,
          "imageable_type": "title",
          "filename": "f8a1457c-441f-4cb4-b18b-a5709824eca5.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 5267,
          "imageable_type": "title",
          "filename": "3d468ead-946b-44bb-aef2-81fe53e61526.webp",
          "type": "cover_mobile",
          "original_url_field": null
        },
        {
          "imageable_id": 5267,
          "imageable_type": "title",
          "filename": "f4c960e9-f12d-4a41-816a-1b536acf7fcd.webp",
          "type": "logo",
          "original_url_field": null
        }
      ]
    },
    {
      "id": 1478,
      "slug": "american-dad",
      "name": "American Dad!",
      "type": "tv",
      "score": "7.8",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 17,
      "images": [
        {
          "imageable_id": 1478,
          "imageable_type": "title",
          "filename": "6da01035-cc9e-476c-84a6-cdf8ade08d61.webp",
          "type": "background",
          "original_url_field": null
        },
        {
          "imageable_id": 1478,
          "imageable_type": "title",
          "filename": "c20483d6-d40a-4b9a-8c0e-bef6341db24f.webp",
          "type": "cover_mobile",
          "original_url_field": null
        },
        {
          "imageable_id": 1478,
          "imageable_type": "title",
          "filename": "feffae39-63da-4970-b2ee-39d8937b9a07.webp",
          "type": "logo",
          "original_url_field": null
        },
        {
          "imageable_id": 1478,
          "imageable_type": "title",
          "filename": "a93db0ae-875a-427d-8b1d-d219d7095e6e.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 1478,
          "imageable_type": "title",
          "filename": "726c99c7-8d67-4ccf-89e1-ce63a8e47de1.webp",
          "type": "poster",
          "original_url_field": null
        }
      ]
    },
    {
      "id": 1817,
      "slug": "sleepy-hollow",
      "name": "Sleepy Hollow",
      "type": "tv",
      "score": "7.9",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 4,
      "images": [
        {
          "imageable_id": 1817,
          "imageable_type": "title",
          "filename": "d228fbea-de1d-4366-9d9b-c71413b1f343.webp",
          "type": "poster",
          "original_url_field": null
        },
        {
          "imageable_id": 1817,
          "imageable_type": "title",
          "filename": "07d7ffd0-08ff-49f1-ae7f-5823fca7bc21.webp",
          "type": "background",
          "original_url_field": null
        },
        {
          "imageable_id": 1817,
          "imageable_type": "title",
          "filename": "4265fa86-bcf5-4d04-818f-2ad9de1beb3d.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 1817,
          "imageable_type": "title",
          "filename": "31e21efa-c10c-440a-ad4c-7a0029ec50d8.webp",
          "type": "cover_mobile",
          "original_url_field": null
        },
        {
          "imageable_id": 1817,
          "imageable_type": "title",
          "filename": "5c3519e9-3c47-4a7c-8421-07e2c854b467.webp",
          "type": "logo",
          "original_url_field": null
        }
      ]
    },
    {
      "id": 2325,
      "slug": "undone",
      "name": "Undone",
      "type": "tv",
      "score": "8.0",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 1,
      "images": [
        {
          "imageable_id": 2325,
          "imageable_type": "title",
          "filename": "f8cef0cd-99ee-4cd1-8a6f-01f6aa1e1991.webp",
          "type": "poster",
          "original_url_field": null
        },
        {
          "imageable_id": 2325,
          "imageable_type": "title",
          "filename": "c4650313-5274-41e5-ae1f-b82f0c03e936.webp",
          "type": "background",
          "original_url_field": null
        },
        {
          "imageable_id": 2325,
          "imageable_type": "title",
          "filename": "5e22b9f2-b132-48e4-b856-2bb0f5be8739.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 2325,
          "imageable_type": "title",
          "filename": "9bbd4f4a-7f92-42c8-9b2c-22ec1df52766.webp",
          "type": "cover_mobile",
          "original_url_field": null
        },
        {
          "imageable_id": 2325,
          "imageable_type": "title",
          "filename": "c2341fb6-8459-4dba-a4d2-bea6eb4f066e.webp",
          "type": "logo",
          "original_url_field": null
        }
      ]
    },
    {
      "id": 3273,
      "slug": "solar-opposites",
      "name": "Solar Opposites",
      "type": "tv",
      "score": "8.3",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 2,
      "images": [
        {
          "imageable_id": 3273,
          "imageable_type": "title",
          "filename": "a5871f11-cec1-4e7d-bf36-e988ff7c6a98.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 3273,
          "imageable_type": "title",
          "filename": "5ce6d11b-7f21-48a0-adbf-78fd04a7bc62.webp",
          "type": "cover_mobile",
          "original_url_field": null
        },
        {
          "imageable_id": 3273,
          "imageable_type": "title",
          "filename": "9f146577-8616-4da9-beab-30a9347dc61a.webp",
          "type": "logo",
          "original_url_field": null
        },
        {
          "imageable_id": 3273,
          "imageable_type": "title",
          "filename": "c2326ada-cd2c-4158-9100-a610a4d0f03c.webp",
          "type": "poster",
          "original_url_field": null
        },
        {
          "imageable_id": 3273,
          "imageable_type": "title",
          "filename": "ce1eb47b-bbf4-4b5c-bfab-8c11041991d1.webp",
          "type": "background",
          "original_url_field": null
        }
      ]
    },
    {
      "id": 5537,
      "slug": "grand-hotel-intrighi-e-passioni",
      "name": "Grand Hotel - Intrighi e Passioni",
      "type": "tv",
      "score": "8.0",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 3,
      "images": [
        {
          "imageable_id": 5537,
          "imageable_type": "title",
          "filename": "3ce9129f-73af-46d7-a846-996039dcd7a9.webp",
          "type": "poster",
          "original_url_field": null
        },
        {
          "imageable_id": 5537,
          "imageable_type": "title",
          "filename": "4abcfbd2-b206-4f2a-9b18-3bb12001b30d.webp",
          "type": "background",
          "original_url_field": null
        },
        {
          "imageable_id": 5537,
          "imageable_type": "title",
          "filename": "2d493b1c-12fe-4c94-9793-f0f6734da656.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 5537,
          "imageable_type": "title",
          "filename": "8e6a43da-f869-4fba-b696-fd5a8cafac27.webp",
          "type": "cover_mobile",
          "original_url_field": null
        }
      ]
    },
    {
      "id": 4403,
      "slug": "hellbound",
      "name": "Hellbound",
      "type": "tv",
      "score": "7.7",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 1,
      "images": [
        {
          "imageable_id": 4403,
          "imageable_type": "title",
          "filename": "6a918fd3-7e03-45af-a40d-b4dd675a965a.webp",
          "type": "poster",
          "original_url_field": null
        },
        {
          "imageable_id": 4403,
          "imageable_type": "title",
          "filename": "d90b191d-1f7d-4d7b-a267-f8ff4823ef8f.webp",
          "type": "background",
          "original_url_field": null
        },
        {
          "imageable_id": 4403,
          "imageable_type": "title",
          "filename": "d7e7138d-0366-4226-98da-538c170e83cf.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 4403,
          "imageable_type": "title",
          "filename": "245d7813-8ad6-41fc-be24-241dd12ee8d2.webp",
          "type": "cover_mobile",
          "original_url_field": null
        },
        {
          "imageable_id": 4403,
          "imageable_type": "title",
          "filename": "ec9802c5-0a6e-49d4-92f5-f0fb884831c6.webp",
          "type": "logo",
          "original_url_field": null
        }
      ]
    },
    {
      "id": 7077,
      "slug": "carol-e-la-fine-del-mondo",
      "name": "Carol e la fine del mondo",
      "type": "tv",
      "score": "8.1",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 1,
      "images": [
        {
          "imageable_id": 7077,
          "imageable_type": "title",
          "filename": "f9902ccc-cd60-43d6-a000-c095c1036172.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 7077,
          "imageable_type": "title",
          "filename": "77b7e3e4-9d70-4e9e-9cfc-9e67ed6c6aa4.webp",
          "type": "cover_mobile",
          "original_url_field": null
        },
        {
          "imageable_id": 7077,
          "imageable_type": "title",
          "filename": "ab0400b3-3132-4fc3-a0b9-a6b4791c2530.webp",
          "type": "logo",
          "original_url_field": null
        },
        {
          "imageable_id": 7077,
          "imageable_type": "title",
          "filename": "f5c66330-ce69-4bfc-a6c6-76eecd56ed7a.webp",
          "type": "background",
          "original_url_field": null
        },
        {
          "imageable_id": 7077,
          "imageable_type": "title",
          "filename": "6602eb29-4172-48cc-b401-eeefd6465a9d.webp",
          "type": "poster",
          "original_url_field": null
        }
      ]
    },
    {
      "id": 5756,
      "slug": "marvels-modok",
      "name": "Marvel's M.O.D.O.K.",
      "type": "tv",
      "score": "6.5",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 1,
      "images": [
        {
          "imageable_id": 5756,
          "imageable_type": "title",
          "filename": "25d37085-a667-485a-8075-3b44a6e98a49.webp",
          "type": "poster",
          "original_url_field": null
        },
        {
          "imageable_id": 5756,
          "imageable_type": "title",
          "filename": "a39f2ff6-095d-4350-9b3e-cfdf8b655634.webp",
          "type": "background",
          "original_url_field": null
        },
        {
          "imageable_id": 5756,
          "imageable_type": "title",
          "filename": "ac15bf0f-7f29-4af6-ae25-077b0a84e6d6.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 5756,
          "imageable_type": "title",
          "filename": "8802cde9-aceb-417a-9473-e1c8e0442d28.webp",
          "type": "cover_mobile",
          "original_url_field": null
        },
        {
          "imageable_id": 5756,
          "imageable_type": "title",
          "filename": "2197fce5-ea2b-4c1e-adc1-108f4a6db628.webp",
          "type": "logo",
          "original_url_field": null
        }
      ]
    },
    {
      "id": 6300,
      "slug": "mulligan",
      "name": "Mulligan",
      "type": "tv",
      "score": "5.3",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 1,
      "images": [
        {
          "imageable_id": 6300,
          "imageable_type": "title",
          "filename": "f4fc2b09-af04-432b-98fc-347511933b3a.webp",
          "type": "poster",
          "original_url_field": null
        },
        {
          "imageable_id": 6300,
          "imageable_type": "title",
          "filename": "5b623f25-1f31-496e-bec2-6e2767ab40ef.webp",
          "type": "background",
          "original_url_field": null
        },
        {
          "imageable_id": 6300,
          "imageable_type": "title",
          "filename": "3f3c5901-31fa-4111-a397-00183880b53f.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 6300,
          "imageable_type": "title",
          "filename": "26f47dea-6b6d-4d95-bf4c-36eef0fe9604.webp",
          "type": "cover_mobile",
          "original_url_field": null
        },
        {
          "imageable_id": 6300,
          "imageable_type": "title",
          "filename": "8549139c-f147-4db2-8336-a3fb821e0042.webp",
          "type": "logo",
          "original_url_field": null
        }
      ]
    },
    {
      "id": 6944,
      "slug": "invincibile",
      "name": "Invincibile",
      "type": "tv",
      "score": "8.7",
      "sub_ita": 0,
      "last_air_date": null,
      "seasons_count": 3,
      "images": [
        {
          "imageable_id": 6944,
          "imageable_type": "title",
          "filename": "52424ba0-8d57-49c9-b1f9-b28b7d46d895.webp",
          "type": "poster",
          "original_url_field": null
        },
        {
          "imageable_id": 6944,
          "imageable_type": "title",
          "filename": "79091c84-4b20-479c-8ee0-8f03f90faa45.webp",
          "type": "logo",
          "original_url_field": null
        },
        {
          "imageable_id": 6944,
          "imageable_type": "title",
          "filename": "674a000a-2508-4dd7-b7c0-2006fb0d38a2.webp",
          "type": "background",
          "original_url_field": null
        },
        {
          "imageable_id": 6944,
          "imageable_type": "title",
          "filename": "d46b52e8-690b-4d21-a1bf-17285ae4bef4.webp",
          "type": "cover",
          "original_url_field": null
        },
        {
          "imageable_id": 6944,
          "imageable_type": "title",
          "filename": "5c62ca60-2787-4439-bbfa-a7708049fca0.webp",
          "type": "cover_mobile",
          "original_url_field": null
        }
      ]
    }
  ]
}

```

### Download link

I video possono essere scricati con il [plugin per yt-dlp](https://github.com/Blu-Tiger/StreamingCommunity-yt-dlp-plugin) usando il link dell'episodio.
