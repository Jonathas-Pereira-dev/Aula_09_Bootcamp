import sentry_sdk

sentry_sdk.init(
    dsn="__________________________________________",#testado e funcionando retirado codigo
    # Add data like request headers and IP for users,
    # see _________________________ for more info
    send_default_pii=True,
)

division_by_zero = 1 / 0