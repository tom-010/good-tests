from django import template

register = template.Library()

@register.filter()
def embedded_youtube_url(url):
    try:
        path, param_str = url.split('?')
        for param in param_str.split('&'):
            key, value = param.split('=')
            if key == 'v':
                return f'https://www.youtube.com/embed/{value}'
    except Exception as e:
        pass
    return url