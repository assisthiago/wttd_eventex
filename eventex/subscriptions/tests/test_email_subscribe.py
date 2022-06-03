from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self) -> None:
        data = dict(
            name='Thiago Assis',
            cpf='12345678901',
            email='thiago.medassis@gmail.com',
            phone='21-99664-3040')

        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'thiago.medassis@gmail.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['thiago.medassis@gmail.com', 'thiago.medassis@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Thiago Assis',
            '12345678901',
            'thiago.medassis@gmail.com',
            '21-99664-3040',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
