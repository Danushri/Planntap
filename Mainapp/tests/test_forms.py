from django.test import SimpleTestCase
from Mainapp.forms import Index_form

class TestForms(SimpleTestCase):

    def test_index_form_valid_data(self):
        form = Index_form(data={
            'Eventname' : 'Festival',
            'desc' : 'today I went to a Festival',
            'Location' : 'London',
            'Date' : '2020-02-02',
            'Rating' : '9',
            'Review' : 'The experiece was amazing'

        })

        self.assertTrue(form.is_valid())

    def test_index_form_no_data(self):
        form = Index_form(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 6)

    # def test_login_form_valid(self):
    #     form = Login_form(data={
    #
    #         'username' : 'Danushri',
    #         'password' : 'askdgbfDnfnA927'
    #     })
    #
    #     self.assertTrue(form.is_valid())
    #
    # def test_login_form_no_data(self):
    #     form = Login_form(data={})
    #
    #     self.assertFalse(form.is_valid())
    #     self.assertEquals(len(form.errors), 2)
