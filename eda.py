import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def eda(path):
    df = pd.read_csv(path, index_col=0)
    fig, ax = plt.subplots(figsize=(20,20))
    ax = sns.heatmap((df.drop(['target', 'user', 'id', 'activityrecognition#0'], axis=1)).corr(), annot=True)
    print(ax)

    df1_drop_by_corr = df.drop(['android.sensor.accelerometer#min','android.sensor.accelerometer#max',
'android.sensor.game_rotation_vector#min',
'android.sensor.game_rotation_vector#max', 'android.sensor.gravity#min',
 'android.sensor.gravity#max',  'android.sensor.gyroscope#min',
 'android.sensor.gyroscope#max', 'android.sensor.gyroscope_uncalibrated#min',
 'android.sensor.gyroscope_uncalibrated#max', 'speed#min',
 'speed#max', 'android.sensor.light#min',
 'android.sensor.light#max', 'android.sensor.linear_acceleration#min',
 'android.sensor.linear_acceleration#max','android.sensor.magnetic_field#min',
 'android.sensor.magnetic_field#max', 'android.sensor.magnetic_field_uncalibrated#min',
 'android.sensor.magnetic_field_uncalibrated#max', 'android.sensor.orientation#min',
 'android.sensor.orientation#max', 'android.sensor.pressure#min',
 'android.sensor.pressure#max', 'android.sensor.proximity#min',
 'android.sensor.proximity#max', 'android.sensor.rotation_vector#min',
 'android.sensor.rotation_vector#max','android.sensor.step_counter#min',
 'android.sensor.step_counter#max', 'sound#min',
 'sound#max','id', 'activityrecognition#0'], axis=1)

 
    df1_drop_by_corr1 = df1_drop_by_corr.drop(['android.sensor.accelerometer#mean','android.sensor.linear_acceleration#mean',
    'android.sensor.gyroscope#mean', 
    'android.sensor.pressure#mean','android.sensor.gyroscope_uncalibrated#mean',
    'android.sensor.accelerometer#std','android.sensor.linear_acceleration#std',
    'android.sensor.gyroscope_uncalibrated#std','android.sensor.gyroscope#std','android.sensor.light#mean','accelerometer#std_tion#std',
    'gyrscope_uncalibrated#std', 'android.sensor.light#std', 'android.sensor.pressure#std',
    'android.sensor.proximity#mean','android.sensor.proximity#std', 'android.sensor.step_counter#mean', 'speed#mean','sound#std',
    'android.sensor.game_rotation_vector#mean', 'android.sensor.gravity#mean', 'android.sensor.step_counter#std' ,'speed#std'
    ], axis=1)

    df1_drop_by_corr2 = df1_drop_by_corr1.dropna()

    df1_drop_by_corr2['game_rot_vec_std'] = df1_drop_by_corr2.apply(lambda a: 
        (a['android.sensor.rotation_vector#std']+a['android.sensor.game_rotation_vector#std'])/2, axis=1)

    df1_drop_by_corr2['mag_field_mean'] = df1_drop_by_corr2.apply(lambda b: 
        (b['android.sensor.magnetic_field_uncalibrated#mean'] + b['android.sensor.magnetic_field#mean'])/2, axis=1)

    df1_drop_by_corr2 = df1_drop_by_corr2.drop([
        'android.sensor.magnetic_field_uncalibrated#mean','android.sensor.magnetic_field#mean', 
        ], axis=1)

    
    df1_drop_by_corr['accelerometer#std_tion#std'] = df1_drop_by_corr.apply(lambda a: 
        (a['android.sensor.accelerometer#std']+a['android.sensor.linear_acceleration#std'])/2, axis=1)

    df1_drop_by_corr['gyrscope_uncalibrated#std'] = df1_drop_by_corr.apply(lambda a:
        (a['android.sensor.gyroscope#std']+a['android.sensor.gyroscope_uncalibrated#std'])/2, axis=1)

    df1_drop_by_corr['new4_std'] = df1_drop_by_corr.apply(lambda a:
        (a['gyrscope_uncalibrated#std'] + a['accelerometer#std_tion#std'])/2, axis=1)

    df1_drop_by_corr[['android.sensor.accelerometer#std','android.sensor.linear_acceleration#std']]
    df1_drop_by_corr['accelerometer#std_tion#std'] = df1_drop_by_corr.apply(lambda a: 
        (a['android.sensor.accelerometer#std']+a['android.sensor.linear_acceleration#std'])/2, axis=1)


    fig, ax = plt.subplots(figsize=(20,20))
    ax = sns.heatmap(df1_drop_by_corr2.corr(), vmax=1, vmin=-1, annot=True)

    fig, ax = plt.subplots(figsize=(20,20))
    ax = sns.heatmap(df1_drop_by_corr1.corr(),vmin=-1, vmax=1, annot=True)

    a = pd.pivot_table(df1_drop_by_corr1, index=['user', 'target'])

    last_data = df1_drop_by_corr2.copy()
    last_data.to_csv('last.csv', index=False)

    test_side = last_data.loc[(last_data['user'] == 'U11') | (last_data['user'] == 'U12')]
    train_side = last_data.loc[(last_data['user'] != 'U11') &(last_data['user'] != 'U12')]
    test_side.to_csv('test_side.csv')
    train_side.to_csv('train_side.csv')

    last_ = pd.pivot_table(last_data ,index=['target'])
    # print(last_)


eda('./dataset_5secondWindow.csv')