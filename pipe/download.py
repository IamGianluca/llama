from pathlib import Path

from blazingai.kaggle import download_comp_data, extract_comp_data

from constants import comp_name, data_path
from kaggle import api


def main():
    zip_fpath: Path = download_comp_data(
        comp_name=comp_name, path=Path("/tmp"), api=api
    )
    extract_comp_data(fname=zip_fpath, path=data_path)


if __name__ == "__main__":
    main()
