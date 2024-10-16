from __future__ import division
import math 
import pandas as pd
import numpy as np
from scipy import stats


def get_subject_info(DF, subjects, var_name):
    df_subjects = DF['Subjects'].to_list()

    subj_idx = []
    df_idx = []
    for isubj, subj in enumerate(subjects):
        if subj in df_subjects:
            idx = df_subjects.index(subj)
            subj_idx.append(isubj)
            df_idx.append(idx)
    care_DF = DF.iloc[df_idx].reset_index(drop=True)
    info_data = np.nan*np.zeros((len(subjects), len(var_name)))
    info_data[subj_idx] = care_DF[var_name].to_numpy()
    info_data = np.squeeze(info_data)
    return info_data



