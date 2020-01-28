from pa_messenger.forms import SendMessageForm
from tests.base import BaseTestCase


class FormTests(BaseTestCase):
    # Ensures populate SenMessageForm with missing message filed give an error
    def test_populate_SendMessageForm_with_missing_message_should_produce_error(self):
        # arrange
        form = SendMessageForm(message='', imageUrl='')

        # assert
        assert form.validate() is False
        assert 'Message is required' in form.message.errors

    # Ensures populate SenMessageForm with message over 160 should produce error 
    def test_populate_SendMessageForm_with_message_over_160_should_produce_error(self):
        # arrange
        form = SendMessageForm(message='This is longThis is longThis is longThis is longThis is longThis is longThis is longThis is longThis is longThis is longThis is longThis is longThis is longThis is longThis is longThis is longThis is longThis is longThis is longThis is long', imageUrl='')

        # assert
        assert form.validate() is False
        assert 'Message must be between 1 and 160 characters' in form.message.errors
