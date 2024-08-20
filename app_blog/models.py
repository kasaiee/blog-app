from django.db import models

STATUS_CHOICES = (
    ('dr', 'draft'),
    ('pb', 'published'),
)

class Author(models.Model):
    name = models.CharField(null=True, max_length=250)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=True)
    description = models.TextField(null=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, null=True)

    def __str__(self):
        return self.title

# # get all authors
# Author.objects.all()

# # get all Posts
# Post.objects.all()

# get a user with name == ali
# Author.objects.get(name="ali")

# # get count of Authors
# Author.objects.all().count()

# # get all posts contains 'A' in title
# Post.objects.filter(title__contains="A")

# # all published posts
# Post.objects.filter(status="pb")

# all posts related to mahmoud
# mahmoud = Author.objects.get(name="mahmoud")
# mahmoud.post_set.all()

# Author.objects.get(name="mahmoud").post_set.all()

# Post.objects.filter(author__name='mahmoud')