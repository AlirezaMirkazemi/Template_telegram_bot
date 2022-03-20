from types import SimpleNamespace
from src.utils.keyboard import create_keyboard


keys = SimpleNamespace(
    random_connect='random_connect',
    settings=':gear: Settings',
    exit=':cross_mark: Exit',
)

keyboards = SimpleNamespace(
    main=create_keyboard([keys.random_connect, keys.settings, keys.exit]),
)