from datetime import datetime, timedelta
from django.utils import timezone
from django.test import SimpleTestCase , TestCase, Client
from django.urls import resolve, reverse
from .models import Post
from .views import post_list , post_new
from .forms import  PostForm


#urls test
class TestUrls(SimpleTestCase):

    def test_post_list_url_is_resolved(self):
        url = reverse('blogs:post_list')
        self.assertEquals(resolve(url).func, post_list)


    def test_post_new_url_is_resolved(self):
        url = reverse('blogs:post_new')
        self.assertEquals(resolve(url).func, post_new)

#forms test
class TestForms(SimpleTestCase):

    def test_postform_form_valid_data(self):
        form = PostForm(data = {
            'title' : 'abc',
            'text'  : 'xyz'
        })

        self.assertTrue(form.is_valid())

#views test
class TestViews(TestCase):

    def test_post_list_GET(self):
        client = Client()

        response = client.get(reverse('blogs:post_list'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blogs/post_list.html')

#models test
class TestModels(TestCase):

    def test_was_published_recently_with_future_post(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Post(published_date=time)
        self.assertIs(future_post.was_published_recently(), False)