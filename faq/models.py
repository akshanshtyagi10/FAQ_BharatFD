from django.db import models
from django.core.cache import cache
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)

    def translate_questions(self):
        translator = Translator()

        # Translate to Hindi if not already translated
        if not self.question_hi:
            self.question_hi = cache.get(self.question + "_hi")
            if not self.question_hi:
                self.question_hi = translator.translate(self.question, src='en', dest='hi').text
                cache.set(self.question + "_hi", self.question_hi)

        # Translate to Bengali if not already translated
        if not self.question_bn:
            self.question_bn = cache.get(self.question + "_bn")
            if not self.question_bn:
                self.question_bn = translator.translate(self.question, src='en', dest='bn').text
                cache.set(self.question + "_bn", self.question_bn)

    def save(self, *args, **kwargs):
        # Automatically trigger translation before saving the object
        if not self.question_hi or not self.question_bn:
            self.translate_questions()

        # Call the original save method to save the object
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
