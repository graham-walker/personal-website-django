from django import template

from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def file_to_icon(value):
    url = value.file.url
    if (url.endswith('.zip')):
        return mark_safe('<span class="icon is-large media-icon"><span class="icon"><i class="fas fa-file-archive fa-lg"></i></span></span>')
    elif (url.endswith('.mp3')):
        return mark_safe('<span class="icon is-large media-icon"><span class="icon"><i class="fas fa-volume-up fa-lg"></i></span></span>')
    elif (url.endswith('.mp4')):
        return mark_safe('<span class="icon is-large media-icon"><span class="icon"><i class="fas fa-film fa-lg"></i></span></span>')
    elif (url.endswith('.exe')):
        return mark_safe('<span class="icon is-large media-icon"><span class="icon"><i class="far fa-window-maximize"></i></span></span>')
    elif (url.endswith('.png')
          or url.endswith('.jpg')
          or url.endswith('.jpeg')
          or url.endswith('.svg')
          or url.endswith('.gif')
          or url.endswith('.bmp')
          or url.endswith('.ico')
          or url.endswith('.webp')
          ):
        return mark_safe('<img style="height: 3rem;" src="' + value.file.url + '">')
    else:
        return mark_safe('<span class="icon is-large media-icon"><span class="icon"><i class="fas fa-file fa-lg"></i></span></span>')


@register.filter
def underscore_to_space(value):
    return value.replace('_', ' ')


@register.filter
def to_class_name(value):
    return value.__class__.__name__
