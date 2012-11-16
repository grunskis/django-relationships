from django.conf import settings

VERSION = (0, 3, 2)

RELATIONSHIPS_SITE_ID = getattr(settings, 'RELATIONSHIPS_SITE_ID',
                                settings.SITE_ID)
