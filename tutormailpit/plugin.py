from tutor import hooks

hooks.Filters.ENV_PATCHES.add_items(
    [
        (
            "openedx-development-settings",
            """
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
  """,
        ),
        (
            "local-docker-compose-dev-services",
            """
mailpit:
  image: axllent/mailpit:v1.18
  restart: unless-stopped
  volumes:
    - ../../data/mailpit:/data
  ports:
    - 8025:8025
    - 1025:1025
  environment:
    MP_MAX_MESSAGES: 5000
    MP_DATABASE: /data/mailpit.db
    MP_SMTP_AUTH_ACCEPT_ANY: 1
    MP_SMTP_AUTH_ALLOW_INSECURE: 1
  """,
        ),
    ]
)

# Modify configuration
hooks.Filters.CONFIG_DEFAULTS.add_items([("SMTP_HOST", "mailpit"), ("SMTP_PORT", 1025)])
