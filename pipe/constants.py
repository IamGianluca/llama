import os
from pathlib import Path

comp_name = os.environ["COMPETITION_LONG_NAME"]
comp_shortname = os.environ["COMPETITION_SHORT_NAME"]

# general paths and full paths
_path = Path("/workspace")
cfg_fpath = _path / "params.yaml"

# data paths and full paths
data_path = _path / "data"
ckpt_path = _path / "ckpt"
mtrc_path = _path / "mtrc"

train_fpath = data_path / "train.csv"
test_fpath = data_path / "test.csv"

train_folds_fpath = data_path / "train_folds.csv"
sample_sub_fpath = data_path / "sample_submission.csv"
