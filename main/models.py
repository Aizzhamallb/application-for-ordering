from django.db import models
# from ckeditor.fields import RichTextField
from django.urls import reverse


# class Category(models.Model):
#     slug = models.SlugField(primary_key=True, max_length=50)
#     title = models.CharField(max_length=50,)
#     parent = models.ForeignKey('self', related_name='children', null=True, blank=True, on_delete=models.CASCADE)

#     def __str__(self):
#         if self.parent:
#             return f'{self.parent} -> {self.title}'
#         return self.title

#     @property
#     def get_children(self):
#         if self.children:
#             return self.children.all()
#         return False






