from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class MediaStorage(S3Boto3Storage):
    """Storage of media files (S3)"""

    location = "media"
    default_acl = "public-read"
    file_overwrite = False
    custom_domain = settings.AWS_S3_CUSTOM_DOMAIN


class StaticStorage(S3Boto3Storage):
    """Storage of static files (S3)"""

    location = "static"
    default_acl = "public-read"
    file_overwrite = False
    custom_domain = settings.AWS_S3_CUSTOM_DOMAIN
