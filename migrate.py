from models import Author, Quote, Tag
from mongoengine import connect
from your_mongo_models import Author as MongoAuthor, Quote as MongoQuote

connect("quotes_db")

for a in MongoAuthor.objects():
    Author.objects.create(
        fullname=a.fullname,
        born_date=a.born_date,
        born_location=a.born_location,
        description=a.description
    )

for q in MongoQuote.objects():
    author = Author.objects.get(fullname=q.author.fullname)

    quote = Quote.objects.create(
        text=q.quote,
        author=author,
        user_id=1
    )

    for tag in q.tags:
        t, _ = Tag.objects.get_or_create(name=tag)
        quote.tags.add(t)
