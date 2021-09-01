"""Post views"""

# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime

posts = [ {
        'name': 'Mont Blac',
        'user': 'David',
        'timestamp': datetime.now().strftime('%b %dth %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/200',
    },
    {
        'name': 'Mont Blac2',
        'user': 'David2',
        'timestamp': datetime.now().strftime('%b %dth %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/200/200/200',
    },
    {
        'name': 'Mont Blac2',
        'user': 'David3',
        'timestamp': datetime.now().strftime('%b %dth %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/219/200/200',
    }
]

# Create your views here.
def list_posts(request):
    """List existign posts"""
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{name} - <i>{timestamp}</i></small></p>
            <figure>
                <img src={picture}/>
            </figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))

