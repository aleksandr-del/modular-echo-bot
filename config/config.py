from dataclasses import dataclass
from environs import Env


@dataclass
class TelegramBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    bot: TelegramBot


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        bot=TelegramBot(
            token=env("BOT_TOKEN"),
            admin_ids=(
                [int(id) for id in env.list("ADMIN_IDS")] if env("ADMIN_IDS") else []
            ),
        )
    )
