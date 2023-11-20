""" _scratch.py

Scratch pad...
"""
import os

import pandas as pd
import yfinance as yf

import toolkit_config as tk_cfg


# ---------------------------------------------------
# Constants
# ---------------------------------------------------
TIC = 'tsla'
PRC_CSV = os.path.join(tk_cfg.DATADIR , 'tsla_prc.csv')
START = '1900-01-01'
END = '2020-12-31'

# ---------------------------------------------------
# get_data0
# ---------------------------------------------------
def get_data0(tic):
    """ Draft of the get_data function. Will download and save stock prices.

    Parameters
    ----------
    tic : str
        Ticker

    """
    df = yf.download(tic,
                     start=START,
                     end=END,
                     ignore_tz=True
                     )
    df.to_csv(PRC_CSV)

if __name__ == "__main__":
    get_data0(tic=TIC)