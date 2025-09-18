from fastapi_zero.settings import Settings


def test_settings_load_default():
    settings = Settings()
    assert isinstance(settings.DATABASE_URL, str)
    assert settings.DATABASE_URL.startswith(
        'sqlite://'
    ) or settings.DATABASE_URL.startswith('postgresql://')


def test_settings_env_override(monkeypatch):
    monkeypatch.setenv('DATABASE_URL', 'sqlite:///test.db')
    settings = Settings()
    assert settings.DATABASE_URL == 'sqlite:///test.db'
