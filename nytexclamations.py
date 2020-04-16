import requests
import nltk

nltk.download('punkt')


def get_exclamations(NYT_API_KEY):
    included_fields = ['title', 'abstract', 'kicker', 'subheadline', 'caption']

    response = requests.get(
        'https://api.nytimes.com/svc/news/v3/content/all/all.json?api-key='
        + NYT_API_KEY
    )

    exclamations = []

    for result in response.json()['results']:
        for field in included_fields:
            try:
                sentences = nltk.sent_tokenize(result[field])
                for sentence in sentences:
                    if sentence[-1] == '!':
                        exclamations.append(sentence)
            except KeyError:
                pass

    return exclamations
