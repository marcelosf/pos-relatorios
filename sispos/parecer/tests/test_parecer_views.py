from django.test import TestCase
from django.shortcuts import resolve_url as r
from sispos.parecer.tests import mock


class ParecerViewsGetTest(TestCase):
    def setUp(self):
        mock_relatorio = mock.MockRelatorio()
        data = mock_relatorio.make_relatorio()
        relatorio = mock_relatorio.save_relatorio(data)
        self.resp = self.client.get(r('parecer:parecer_new',
                                      slug=str(relatorio.uuid)))

    def test_status_code(self):
        """Sttatus code should be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It should render parecer_ds1_new.html template"""
        self.assertTemplateUsed(self.resp, 'parecer_ds1_new.html')

    def test_extends_template(self):
        """It should extends base.html"""
        self.assertTemplateUsed(self.resp, 'base.html')

    def test_context_has_form(self):
        """Context should have Rds1Form"""
        self.assertIn('form', self.resp.context)

    def test_form_rendered(self):
        """It should render the form"""
        tags = ((1, '<form'), (6, '<textarea'), (1, '<input'),
                (1, 'type="submit"'))
        for count, expected in tags:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_has_csrf(self):
        """It should render the csrf middleware"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')


class ParecerViewPostTest(TestCase):
    def setUp(self):
        mock_relatorio = mock.MockRelatorio()
        data = mock_relatorio.make_relatorio()
        relatorio = mock_relatorio.save_relatorio(data)
        self.resp = self.client.post(r('parecer:parecer_new',
                                       slug=str(relatorio.uuid)))

    def test_status_code(self):
        """Status code should be 200"""
        self.assertEqual(200, self.resp.status_code)
