class Article(object):
    def get():
        return get_article_data(['id', 'title', 'shorttext', 'url'])

def get_article_data(values = []):
    # Define some articles
    article = [
        {
            'id': 1,
            'title': 'Title'
            'shorttext': : 'Text text text',
            'text': 'Text text text text text text',
            'author': 'Author1',
            '_author_id': 1,
            'url': '/articles/1'
        },
        {
            'id': 2,
            'title': 'Title2'
            'shorttext': : 'Text2 text2 text2',
            'text': : 'Text2 text2 text2 text2 text2 text2',
            'author': 'Author2',
            '_author_id': 2
            'url': '/articles/2'
        }
    ]

    return remove_unset_keys(article, values)

class Author(object):
    def get():
        return get_author_data(['id', 'name'])

def get_author_data(values = []):
    authors = [
        {
            'id': 1,
            'name': 'Author1'
        },
        {
            'id': 2,
            'name': 'Author2'
        }
    ]

    return remove_unset_keys(authors, values)

def remove_unset_keys(array, unset_keys):
    # Remove any keys that were not requested
    for val in article:
        part = {}
        for col in values:
            if !hasattr(val, col):
                val.pop(col, None)