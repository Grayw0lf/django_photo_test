from django.test import TestCase
from .models import UPhoto
from .forms import UPhotoForm
from django.core.files.uploadedfile import SimpleUploadedFile


NEW_PHOTO = SimpleUploadedFile('tum.png', content=open('tum.png', 'rb+').read(), content_type='image/jpeg')
ERROR_FILE = SimpleUploadedFile('rtest.txt', content=open('rtest.txt', 'rb').read(), content_type='application/octet-stream')


class UPhotoTest(TestCase):

    """ Тестирование модели. """

    @classmethod
    def setUpTestData(cls) -> None:
        UPhoto.objects.create(photo=NEW_PHOTO, comment='hello, world')

    def test_photo(self) -> None:
        get_photo = UPhoto.objects.get(id=1)
        field: str = get_photo._meta.get_field('photo').verbose_name

        self.assertEqual(field, 'photo')

    def test_comment(self) -> None:
        get_comment = UPhoto.objects.get(id=1)
        field: str = get_comment._meta.get_field('comment').verbose_name

        self.assertEqual(field, 'comment')

    def test_len(self) -> None:
        get_len = UPhoto.objects.get(id=1)
        field: int = get_len._meta.get_field('comment').max_length

        self.assertEqual(field, 200)


class ViewsTest(TestCase):

    """ Тестирование представления. """

    @classmethod
    def setUpTestData(cls) -> None:
        UPhoto.objects.create(comment='first comment', photo=NEW_PHOTO)

    def test_home_view(self) -> None:
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='home.html')
        self.assertTrue(len(response.context['object_list']) == 1)

    def test_upload_view(self) -> None:
        response = self.client.get('/upload/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='upload.html')


class UPhotoFormTest(TestCase):

    """ Тестирование формы и отправка файла заведомо неправильного формата. """

    def test_comment_and_photo_labels(self) -> None:
        form: UPhotoForm = UPhotoForm()

        self.assertTrue(form.fields['comment'].label is False and form.fields['photo'].label is False)

    def test_error_form(self) -> None:
        response = self.client.post('/upload/', data={'comment': 'goodbye, world', 'photo': ERROR_FILE})

        self.assertContains(
            response, 'Upload a valid image. The file you uploaded was either not an image or a corrupted image.', html=True)
