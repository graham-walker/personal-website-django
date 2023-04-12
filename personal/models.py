from django.db import models
from taggit.managers import TaggableManager
from taggit.models import Tag
from django.utils.timezone import datetime
from ckeditor.fields import RichTextField


class Bio(models.Model):
    name = models.CharField(max_length=2000, default="Your Name")
    initials = models.CharField(max_length=2000, blank=True, null=True)
    title = models.CharField(max_length=2000, blank=True, null=True)
    greeting = models.CharField(max_length=2000, blank=True, null=True)
    screenshot_url = models.CharField(max_length=2000, blank=True, null=True)
    favicon_url = models.CharField(max_length=2000, blank=True, null=True)
    siteicon_url = models.CharField(max_length=2000, blank=True, null=True)
    email = models.CharField(max_length=2000, blank=True, null=True)
    phone_number = models.CharField(max_length=2000, blank=True, null=True)
    employment = models.CharField(max_length=2000, blank=True, null=True)
    location = models.CharField(max_length=2000, blank=True, null=True)
    github_url = models.CharField(max_length=2000, blank=True, null=True)
    linkedin_url = models.CharField(max_length=2000, blank=True, null=True)
    youtube_url = models.CharField(max_length=2000, blank=True, null=True)
    facebook_url = models.CharField(max_length=2000, blank=True, null=True)
    twitter_url = models.CharField(max_length=2000, blank=True, null=True)
    resume_url = models.CharField(max_length=2000, blank=True, null=True)
    about_me = RichTextField(blank=True, null=True)
    show_about_buttons = models.BooleanField(default=True)
    announcement = RichTextField(blank=True, null=True)
    website_repo_url = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.name


class File(models.Model):
    name = models.CharField(max_length=2000, null=True, blank=True)
    file = models.FileField()
    date_uploaded = models.DateTimeField(default=datetime.now)

    def __str__(self):
        if (not self.name):
            return str(self.file)
        else:
            return self.name


class Post(models.Model):
    title = models.CharField(max_length=2000)
    subtitle = models.CharField(max_length=2000, blank=True)
    visible = models.BooleanField(default=True)
    show_on_homepage = models.BooleanField(default=False)
    screenshot = models.CharField(max_length=2000, blank=True)
    screenshot_credit = models.CharField(max_length=2000, blank=True)
    short_description = RichTextField()
    primary_button_text = models.CharField(max_length=50, default="View Post")
    tags = TaggableManager(blank=True)
    body = RichTextField()
    date_posted = models.DateTimeField(default=datetime.now)
    date_edited = models.DateTimeField(blank=True, null=True)
    display_posted = models.BooleanField(default=False)
    display_edited = models.BooleanField(default=False)
    files = models.ManyToManyField(File, blank=True)

    def __str__(self):
        if (self.visible == False):
            return '(Invisible) ' + self.title
        return self.title

    def save(self, *args, **kwargs):
        self.date_edited = datetime.now()
        super(Post, self).save(*args, **kwargs)


class LinkPost(models.Model):
    title = models.CharField(max_length=2000)
    subtitle = models.CharField(max_length=2000, blank=True)
    visible = models.BooleanField(default=True)
    show_on_homepage = models.BooleanField(default=False)
    screenshot = models.CharField(max_length=2000, blank=True)
    short_description = RichTextField()
    primary_button_text = models.CharField(max_length=50, default="Visit Link")
    primary_button_link = models.CharField(max_length=2000, blank=True)
    secondary_button_text = models.CharField(max_length=50, blank=True)
    secondary_button_link = models.CharField(max_length=2000, blank=True)
    tags = TaggableManager(blank=True)
    date_posted = models.DateTimeField(default=datetime.now)
    date_edited = models.DateTimeField(blank=True, null=True)
    display_posted = models.BooleanField(default=True)
    display_edited = models.BooleanField(default=False)

    def __str__(self):
        if (self.visible == False):
            return '(Invisible) ' + self.title
        return self.title

    def save(self, *args, **kwargs):
        self.date_edited = datetime.now()
        super(LinkPost, self).save(*args, **kwargs)
