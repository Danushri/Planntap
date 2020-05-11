from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import *

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)



    def test_register_url_is_resolved(self):
        url = reverse('register')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, register)



    def test_maps_url_is_resolved(self):
        url = reverse('maps')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, maps)



    def test_RandomButton_url_is_resolved(self):
        url = reverse('RandomButton')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, RandomButton)



    def test_getDiary_url_is_resolved(self):
        url = reverse('getDiary')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, get_diaryEntry)

    def test_addDiary_url_is_resolved(self):
        url = reverse('add diary')
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, AddDiaryView)

    def test_updateDiary_url_is_resolved(self):
        url = reverse('UpdateDiary')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, updateDiary)


    def test_deleteDiary_url_is_resolved(self):
        url = reverse('DeleteDiary')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, deleteDiary)



    def test_twitter_url_is_resolved(self):
        url = reverse('twitter')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, twitter)


    def test_EntrySuccess_url_is_resolved(self):
        url = reverse('EntrySuccess')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, EntrySuccess)


    def test_facebookEvents_url_is_resolved(self):
        url = reverse('facebook')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, facebookEvent)


    def test_Random_url_is_resolved(self):
        url = reverse('Random')
        # print(resolve(url))
        self.assertEquals(resolve(url).func, Random)

    # def test_logout_url_is_resolved(self):
    #     url = reverse('logout')
     # print(resolve(url))
    #     self.assertEquals(resolve(url).func.view_class, LogoutView)
