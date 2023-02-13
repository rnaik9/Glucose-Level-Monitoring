#Copyrights:Rahul Naik(ASU id:12256122721)


import pandas as pd
import numpy as np

contiglumon_sys=pd.read_csv('CGMData.csv',low_memory=False,usecols=['Date','Time','Sensor Glucose (mg/dL)'])
ins_datasys=pd.read_csv('InsulinData.csv',low_memory=False)

contiglumon_sys['date_time_stamp']=pd.to_datetime(contiglumon_sys['Date'] + ' ' + contiglumon_sys['Time'])
date_to_be_removed=contiglumon_sys[contiglumon_sys['Sensor Glucose (mg/dL)'].isna()]['Date'].unique()
contiglumon_sys=contiglumon_sys.set_index('Date').drop(index=date_to_be_removed).reset_index()
contiglumon_sys_test=contiglumon_sys.copy()
contiglumon_sys_test=contiglumon_sys_test.set_index(pd.DatetimeIndex(contiglumon_sys['date_time_stamp']))
ins_datasys['date_time_stamp']=pd.to_datetime(ins_datasys['Date'] + ' ' + ins_datasys['Time'])
automatic_mode_start=ins_datasys.sort_values(by='date_time_stamp',ascending=True).loc[ins_datasys['Alarm']=='AUTO MODE ACTIVE PLGM OFF'].iloc[0]['date_time_stamp']
automatic_mode_dataframe=contiglumon_sys.sort_values(by='date_time_stamp',ascending=True).loc[contiglumon_sys['date_time_stamp']>=automatic_mode_start]
man_mode_dataframe=contiglumon_sys.sort_values(by='date_time_stamp',ascending=True).loc[contiglumon_sys['date_time_stamp']<automatic_mode_start]
automatic_mode_dataframe_date_indices=automatic_mode_dataframe.copy()
automatic_mode_dataframe_date_indices=automatic_mode_dataframe_date_indices.set_index('date_time_stamp')
listno1=automatic_mode_dataframe_date_indices.groupby('Date')['Sensor Glucose (mg/dL)'].count().where(lambda x:x>0.8*288).dropna().index.tolist()
automatic_mode_dataframe_date_indices=automatic_mode_dataframe_date_indices.loc[automatic_mode_dataframe_date_indices['Date'].isin(listno1)]





Percentageandtime_in_hyperglycemia_wholeday_automaticmode=(automatic_mode_dataframe_date_indices.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']>180].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_hyperglycemia_daytime_automaticmode=(automatic_mode_dataframe_date_indices.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']>180].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_hyperglycemia_overnight_automaticmode=(automatic_mode_dataframe_date_indices.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']>180].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_hyperglycemia_critical_wholeday_automaticmode=(automatic_mode_dataframe_date_indices.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']>250].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_hyperglycemia_critical_daytime_automaticmode=(automatic_mode_dataframe_date_indices.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']>250].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_hyperglycemia_critical_overnight_automaticmode=(automatic_mode_dataframe_date_indices.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']>250].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_range_wholeday_automaticmode=(automatic_mode_dataframe_date_indices.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']>=70) & (automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']<=180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_range_daytime_automaticmode=(automatic_mode_dataframe_date_indices.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']>=70) & (automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']<=180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_range_overnight_automaticmode=(automatic_mode_dataframe_date_indices.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']>=70) & (automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']<=180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_range_sec_wholeday_automaticmode=(automatic_mode_dataframe_date_indices.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']>=70) & (automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']<=150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_range_sec_daytime_automaticmode=(automatic_mode_dataframe_date_indices.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']>=70) & (automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']<=150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_range_sec_overnight_automaticmode=(automatic_mode_dataframe_date_indices.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']>=70) & (automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']<=150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_hypoglycemia_lv1_wholeday_automaticmode=(automatic_mode_dataframe_date_indices.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']<70].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_hypoglycemia_lv1_daytime_automaticmode=(automatic_mode_dataframe_date_indices.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']<70].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_hypoglycemia_lv1_overnight_automaticmode=(automatic_mode_dataframe_date_indices.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']<70].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_hypoglycemia_lv2_wholeday_automaticmode=(automatic_mode_dataframe_date_indices.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']<54].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_hypoglycemia_lv2_daytime_automaticmode=(automatic_mode_dataframe_date_indices.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']<54].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)
Percentageandtime_in_hypoglycemia_lv2_overnight_automaticmode=(automatic_mode_dataframe_date_indices.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[automatic_mode_dataframe_date_indices['Sensor Glucose (mg/dL)']<54].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)





man_mode_dataframe_index=man_mode_dataframe.copy()
man_mode_dataframe_index=man_mode_dataframe_index.set_index('date_time_stamp')
listno2=man_mode_dataframe_index.groupby('Date')['Sensor Glucose (mg/dL)'].count().where(lambda x:x>0.8*288).dropna().index.tolist()
man_mode_dataframe_index=man_mode_dataframe_index.loc[man_mode_dataframe_index['Date'].isin(listno2)]





Percentageandtime_in_hyperglycemia_wholeday_manualmode=(man_mode_dataframe_index.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[man_mode_dataframe_index['Sensor Glucose (mg/dL)']>180].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)





Percentageandtime_in_hyperglycemia_daytime_manualmode=(man_mode_dataframe_index.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[man_mode_dataframe_index['Sensor Glucose (mg/dL)']>180].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)





Percentageandtime_in_hyperglycemia_overnight_manualmode=(man_mode_dataframe_index.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[man_mode_dataframe_index['Sensor Glucose (mg/dL)']>180].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)



Percentageandtime_in_hyperglycemia_critical_wholeday_manualmode=(man_mode_dataframe_index.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[man_mode_dataframe_index['Sensor Glucose (mg/dL)']>250].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


# line44]:


Percentageandtime_in_hyperglycemia_critical_daytime_manualmode=(man_mode_dataframe_index.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[man_mode_dataframe_index['Sensor Glucose (mg/dL)']>250].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


# line45]:


Percentageandtime_in_hyperglycemia_critical_overnight_manualmode=(man_mode_dataframe_index.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[man_mode_dataframe_index['Sensor Glucose (mg/dL)']>250].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)





Percentageandtime_in_range_wholeday_manualmode=(man_mode_dataframe_index.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(man_mode_dataframe_index['Sensor Glucose (mg/dL)']>=70) & (man_mode_dataframe_index['Sensor Glucose (mg/dL)']<=180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)





Percentageandtime_in_range_daytime_manualmode=(man_mode_dataframe_index.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(man_mode_dataframe_index['Sensor Glucose (mg/dL)']>=70) & (man_mode_dataframe_index['Sensor Glucose (mg/dL)']<=180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


# line48]:


Percentageandtime_in_range_overnight_manualmode=(man_mode_dataframe_index.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(man_mode_dataframe_index['Sensor Glucose (mg/dL)']>=70) & (man_mode_dataframe_index['Sensor Glucose (mg/dL)']<=180)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)




Percentageandtime_in_range_sec_wholeday_manualmode=(man_mode_dataframe_index.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(man_mode_dataframe_index['Sensor Glucose (mg/dL)']>=70) & (man_mode_dataframe_index['Sensor Glucose (mg/dL)']<=150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


# line50]:


Percentageandtime_in_range_sec_daytime_manualmode=(man_mode_dataframe_index.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(man_mode_dataframe_index['Sensor Glucose (mg/dL)']>=70) & (man_mode_dataframe_index['Sensor Glucose (mg/dL)']<=150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


# line51]:


Percentageandtime_in_range_sec_overnight_manualmode=(man_mode_dataframe_index.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[(man_mode_dataframe_index['Sensor Glucose (mg/dL)']>=70) & (man_mode_dataframe_index['Sensor Glucose (mg/dL)']<=150)].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)





Percentageandtime_in_hypoglycemia_lv1_wholeday_manualmode=(man_mode_dataframe_index.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[man_mode_dataframe_index['Sensor Glucose (mg/dL)']<70].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


# line53]:


Percentageandtime_in_hypoglycemia_lv1_daytime_manualmode=(man_mode_dataframe_index.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[man_mode_dataframe_index['Sensor Glucose (mg/dL)']<70].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


# line54]:


Percentageandtime_in_hypoglycemia_lv1_overnight_manualmode=(man_mode_dataframe_index.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[man_mode_dataframe_index['Sensor Glucose (mg/dL)']<70].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)





Percentageandtime_in_hypoglycemia_lv2_wholeday_manualmode=(man_mode_dataframe_index.between_time('0:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[man_mode_dataframe_index['Sensor Glucose (mg/dL)']<54].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


# line56]:


Percentageandtime_in_hypoglycemia_lv2_daytime_manualmode=(man_mode_dataframe_index.between_time('6:00:00','23:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[man_mode_dataframe_index['Sensor Glucose (mg/dL)']<54].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)


# line57]:


Percentageandtime_in_hypoglycemia_lv2_overnight_manualmode=(man_mode_dataframe_index.between_time('0:00:00','05:59:59')[['Date','Time','Sensor Glucose (mg/dL)']].loc[man_mode_dataframe_index['Sensor Glucose (mg/dL)']<54].groupby('Date')['Sensor Glucose (mg/dL)'].count()/288*100)





finalresults_dataframe = pd.DataFrame({'Percentageandtime_in_hyperglycemia_overnight':[ Percentageandtime_in_hyperglycemia_overnight_manualmode.mean(axis=0),Percentageandtime_in_hyperglycemia_overnight_automaticmode.mean(axis=0)],


'Percentageandtime_in_hyperglycemia_critical_overnight':[ Percentageandtime_in_hyperglycemia_critical_overnight_manualmode.mean(axis=0),Percentageandtime_in_hyperglycemia_critical_overnight_automaticmode.mean(axis=0)],


'Percentageandtime_in_range_overnight':[ Percentageandtime_in_range_overnight_manualmode.mean(axis=0),Percentageandtime_in_range_overnight_automaticmode.mean(axis=0)],


'Percentageandtime_in_range_sec_overnight':[ Percentageandtime_in_range_sec_overnight_manualmode.mean(axis=0),Percentageandtime_in_range_sec_overnight_automaticmode.mean(axis=0)],


'Percentageandtime_in_hypoglycemia_lv1_overnight':[ Percentageandtime_in_hypoglycemia_lv1_overnight_manualmode.mean(axis=0),Percentageandtime_in_hypoglycemia_lv1_overnight_automaticmode.mean(axis=0)],


'Percentageandtime_in_hypoglycemia_lv2_overnight':[ np.nan_to_num(Percentageandtime_in_hypoglycemia_lv2_overnight_manualmode.mean(axis=0)),np.nan_to_num(Percentageandtime_in_hypoglycemia_lv2_overnight_automaticmode.mean(axis=0))],
                           'Percentageandtime_in_hyperglycemia_daytime':[ Percentageandtime_in_hyperglycemia_daytime_manualmode.mean(axis=0),Percentageandtime_in_hyperglycemia_daytime_automaticmode.mean(axis=0)],
                           'Percentageandtime_in_hyperglycemia_critical_daytime':[ Percentageandtime_in_hyperglycemia_critical_daytime_manualmode.mean(axis=0),Percentageandtime_in_hyperglycemia_critical_daytime_automaticmode.mean(axis=0)],
                           'Percentageandtime_in_range_daytime':[ Percentageandtime_in_range_daytime_manualmode.mean(axis=0),Percentageandtime_in_range_daytime_automaticmode.mean(axis=0)],
                           'Percentageandtime_in_range_sec_daytime':[ Percentageandtime_in_range_sec_daytime_manualmode.mean(axis=0),Percentageandtime_in_range_sec_daytime_automaticmode.mean(axis=0)],
                           'Percentageandtime_in_hypoglycemia_lv1_daytime':[ Percentageandtime_in_hypoglycemia_lv1_daytime_manualmode.mean(axis=0),Percentageandtime_in_hypoglycemia_lv1_daytime_automaticmode.mean(axis=0)],
                           'Percentageandtime_in_hypoglycemia_lv2_daytime':[ Percentageandtime_in_hypoglycemia_lv2_daytime_manualmode.mean(axis=0),Percentageandtime_in_hypoglycemia_lv2_daytime_automaticmode.mean(axis=0)],

                           
                           'Percentageandtime_in_hyperglycemia_wholeday':[ Percentageandtime_in_hyperglycemia_wholeday_manualmode.mean(axis=0),Percentageandtime_in_hyperglycemia_wholeday_automaticmode.mean(axis=0)],
                           'Percentageandtime_in_hyperglycemia_critical_wholeday':[ Percentageandtime_in_hyperglycemia_critical_wholeday_manualmode.mean(axis=0),Percentageandtime_in_hyperglycemia_critical_wholeday_automaticmode.mean(axis=0)],
                           'Percentageandtime_in_range_wholeday':[ Percentageandtime_in_range_wholeday_manualmode.mean(axis=0),Percentageandtime_in_range_wholeday_automaticmode.mean(axis=0)],
                           'Percentageandtime_in_range_sec_wholeday':[ Percentageandtime_in_range_sec_wholeday_manualmode.mean(axis=0),Percentageandtime_in_range_sec_wholeday_automaticmode.mean(axis=0)],
                           'Percentageandtime_in_hypoglycemia_lv1_wholeday':[ Percentageandtime_in_hypoglycemia_lv1_wholeday_manualmode.mean(axis=0),Percentageandtime_in_hypoglycemia_lv1_wholeday_automaticmode.mean(axis=0)],
                           'Percentageandtime_in_hypoglycemia_lv2_wholeday':[ Percentageandtime_in_hypoglycemia_lv2_wholeday_manualmode.mean(axis=0),Percentageandtime_in_hypoglycemia_lv2_wholeday_automaticmode.mean(axis=0)]
                    
                          
},
                          index=['manual_mode','auto_mode'])





finalresults_dataframe.to_csv('Results.csv',header=False,index=False)







