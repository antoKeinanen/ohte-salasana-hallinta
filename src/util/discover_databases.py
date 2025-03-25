from pathlib import Path
import platformdirs
from glob import glob


def discover_vaults(base_path: None | Path = None):
    base_path = Path(base_path or platformdirs.user_data_path("password-manager"))
    if not base_path.exists():
        base_path.mkdir(parents=True)

    db_pattern = Path(base_path).joinpath("*.sqlite")

    databases = [
        (db_path, Path(db_path).name.capitalize().removesuffix(".sqlite"))
        for db_path in glob(str(db_pattern))
    ]
    return databases
