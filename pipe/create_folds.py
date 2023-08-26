import constants as const
import pandas as pd
from blazingai.params import load_cfg
from sklearn import model_selection


def create_folds(cfg):
    df = pd.read_csv(const.train_fpath)

    # assign records to folds
    df["kfold"] = -1
    skf = model_selection.KFold(
        n_splits=cfg.n_folds,
        shuffle=True,
        random_state=cfg.seed,
    )
    for fold_number, (_, val_idx) in enumerate(skf.split(X=df)):
        df.loc[val_idx, "kfold"] = fold_number

    print(df.groupby("kfold").mean())
    df.to_csv(const.train_folds_fpath, index=False)


if __name__ == "__main__":
    cfg = load_cfg(fpath=const.cfg_fpath, cfg_name="create_folds")
    create_folds(cfg=cfg)
