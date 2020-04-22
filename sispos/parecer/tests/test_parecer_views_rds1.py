from django.test import TestCase
from django.shortcuts import resolve_url as r
from sispos.parecer.tests import mock
from sispos.parecer.models import Rds1


class ParecerViewsGetTest(TestCase):
    def setUp(self):
        mock_relatorio = mock.MockRelatorio()
        data = mock_relatorio.make_relatorio()
        self.relatorio = mock_relatorio.save_relatorio(data)
        self.resp = self.client.get(r('parecer:parecer_rds1_new',
                                      slug=str(self.relatorio.uuid)))

    def test_status_code(self):
        """Sttatus code should be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """It should render parecer_new.html template"""
        self.assertTemplateUsed(self.resp, 'parecer_new.html')

    def test_extends_template(self):
        """It should extends base.html"""
        self.assertTemplateUsed(self.resp, 'base.html')

    def test_context_has_form(self):
        """Context should have Rds1Form"""
        self.assertIn('form', self.resp.context)

    def test_context_has_slug(self):
        """Context field should have slug"""
        self.assertIn('slug', self.resp.context)

    def test_form_action(self):
        expected = 'action="{}"'.format(r('parecer:parecer_rds1_new',
                                        slug=str(self.relatorio.uuid)))
        self.assertContains(self.resp, expected)

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

    def test_form_novalidate(self):
        """Form should have novalidate attr"""
        self.assertContains(self.resp, 'novalidate')

    def test_side_bar(self):
        """It must render sidebar.html"""
        self.assertTemplateUsed(self.resp, 'sidebar.html')


class ParecerViewPostTest(TestCase):
    def setUp(self):
        mock_user = mock.MockUser()
        relator = mock_user.make_relator()
        mock_relatorio = mock.MockRelatorio()
        data = mock_relatorio.make_relatorio()
        relatorio = mock_relatorio.save_relatorio(data)
        mock_parecer = mock.MockParecer()
        parecer_data = mock_parecer.make_parecer()
        self.client.force_login(relator)
        self.resp = self.client.post(r('parecer:parecer_rds1_new',
                                       slug=str(relatorio.uuid)), parecer_data)

    def test_status_code(self):
        """Status code should be 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_parecer_created(self):
        """It should create a parecer"""
        self.assertTrue(Rds1.objects.exists())

    def test_status_message(self):
        """It should show status messages"""
        expected = 'Parecer enviado com sucesso.'
        self.assertContains(self.resp, expected)

    def test_has_status_field(self):
        """It should render status field"""
        self.assertContains(self.resp, 'Status')


class ParecerViewInvalidPostTest(TestCase):
    def setUp(self):
        mock_user = mock.MockUser()
        relator = mock_user.make_relator()
        mock_relatorio = mock.MockRelatorio()
        data = mock_relatorio.make_relatorio()
        relatorio = mock_relatorio.save_relatorio(data)
        self.client.force_login(relator)
        self.resp = self.client.post(r('parecer:parecer_rds1_new',
                                       slug=str(relatorio.uuid)), {})

    def test_message(self):
        expected = 'Não foi possível enviar o parecer.'
        self.assertContains(self.resp, expected)
