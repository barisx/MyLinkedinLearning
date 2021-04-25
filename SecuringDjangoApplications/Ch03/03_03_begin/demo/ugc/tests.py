import base64
import re
from cryptography.fernet import Fernet

from unittest.mock import patch

from celery.exceptions import Retry
from celery.contrib.testing.worker import start_worker
import django.test
from django.core.cache import cache
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APISimpleTestCase

from demo.celery import app

from api.utils import create_access_token, auth_header
from api.models import ActivityLog
from ugc.models import Comment, Journal
from ugc.tasks import create_comment

class CreateCommentTaskTestCase(TestCase):
    def setUp(self):
        super().setUp()
        cache.clear()

    def test_creates_object(self):
        self.assertEqual(Comment.objects.count(), 0)
        user_id = User.objects.first().id
        cache_key = '{}/comment_created'.format(user_id)

        self.assertFalse(cache.has_key(cache_key))
        create_comment(user_id, 'example')
        comment = Comment.objects.first()
        self.assertEqual(comment.text, 'example')
        self.assertEqual(cache.get(cache_key), comment.id)

    @patch('ugc.tasks.create_comment.retry')
    def test_retry(self, create_comment_retry):
        user_id = User.objects.first().id
        create_comment(user_id, 'example')
        create_comment_retry.side_effect = Retry()
        with self.assertRaises(Retry):
            create_comment(user_id, 'example')

    def test_create(self):
        client_side_key = 'incredible2amazing'
        client_side_key += ('_' * (32 - len(client_side_key)))
        client_side_key = base64.urlsafe_b64encode(client_side_key.encode())
        plain_text = 'helloworld'.encode()
        encrypted_text = Fernet(client_side_key).encrypt(plain_text)
        encrypted_text = ''.join([chr(c) for c in ecnrypted_text])
        data = {
            'created_by': self.user.id,
            'encrypted_text': encrypted_text,
        }
        response = self.client.post(
            '/api/v1/journal/',
            data=data, **self.auth_user
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ActivityLog.objects.count(), 0)
        journal = Journal.objects.last()
        self.assertEqual(journal.created_by, self.user)
        self.assertEqual(journal.encrypted_text, encrypted_text)
        
        encrypted_bytes = bytes([ord(n) for n in journal.encrypted_text])
        decrypted = Fernet(client_side_key).decrypt(encrypted_bytes)
        self.assertEqual(decrypted, b'hello world')
        
        print(plain_text)
        print(journal.encrypted_text)
        print(decrypted)
        