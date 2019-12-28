from elasticsearch_dsl import  connections,Document,Text,Keyword,Date,Search
from elasticsearch import  Elasticsearch
connections.create_connection(hosts=['127.0.0.1'], timeout=20)
es=Elasticsearch()

class Blogpost(Document):
    Title=Text()
    published_date=Date()
    published_by=Text()
    tags=Keyword()
    body=Text()

    class Index:
        name='blog_index' #index will be created automatically

bg=Blogpost()
bg.title="A better way to use elasticsearch python"
bg.published_date="12-01-2019"
bg.published_by="Kartik"
bg.tags=['tech','elasticsearch','python']
bg.body="Who does not love object-oriented programming paradigms"
bg.save()


s = Search(using=es, index="blog_index").filter("term", tags="tech").query("match", title="python")\
    .exclude("match", body="Hello world")