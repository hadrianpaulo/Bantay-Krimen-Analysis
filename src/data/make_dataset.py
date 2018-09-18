# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
import os
import pandas as pd

@click.command()
def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    files = os.listdir('data/raw/060718')
#    files.remove('.gitkeep')
    df = pd.DataFrame()
    for f in files:
        df = df.append(pd.read_json(f'data/raw/060718/{f}'))
    df['region'] = [x[-1] for x in df.location.str.split(', ').tolist()]
    df['province'] = [x[-2] for x in df.location.str.split(', ').tolist()]
    df.date = pd.to_datetime(df.date)
    df['hour'] = pd.to_datetime(df['time'], format='%H:%M:%S').dt.hour
    df.to_csv('data/processed/crime_incidences.csv', index=False)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
