from dataclasses import replace
from genericpath import exists
import pandas as pd
import numpy as np
import pm4py as pm
from sqlalchemy import create_engine
import resources__
import datetime
from resources__ import variants
import plotly.express as plx

#db_connection
db_provider = "postgresql://"
user = "ubuntu1"
password ="3004222950a"
address  = "20.226.14.116:5432/postgres"
engine = create_engine(db_provider + user + ":" + password  + '@'+ address)


# Read eventlog
event_log = pm.read_xes('Hospital Billing - Event Log.xes.gz')
event_log_df = pm.convert_to_dataframe(event_log)
event_log_df.to_sql('event_log',con = engine,schema='billing',if_exists = 'replace' )
print("Done")


df_variants = variants.get_variants_df(event_log)
df_variants['info'] = df_variants['info'].astype(str)
#  df_variants.to_sql(name="variants_total_df",con=engine,if_exists='replace',index =False,schema="billing")

# Datframe with Traces
def get_df_traces_total():
    df_traces = resources__.variants.get_variants_df(eventlog=event_log)
    df_traces['info'] = df_traces['info'].astype(str)
    df_traces.to_sql(name="variants_total_df",con=engine,if_exists='replace',index =False,schema="billing")

# Overview Information   --------------- { Cses, Events, Activities, Variants, States, Period }
def get_overview_info() :
    years = event_log_df['time:timestamp'].dt.year.unique().tolist()
    dataframes = []
    __dataframes = []
    for year in years:
        traces_contained = pm.filter_time_range(event_log,dt1=datetime.datetime(year-1,12,31),dt2=datetime.datetime(year,12,31),mode='traces_contained')
        df_traces_contained = pm.convert_to_dataframe(traces_contained)
        variants_trace = pm.get_variants_as_tuples(traces_contained)
        var_ = []
        data_ = []
        for var,dat in variants_trace.items():
            var_.append(var)
            data_.append(dat)
        df_g = pd.DataFrame({'var':var_,'dat':data_})
        xc = ['variant_' + str(h) for h in np.arange(len(df_g))]
        df_g['v_name'] = xc
        __dataframes.append(df_g)
        events_ = [len(df_traces_contained)]
        total_variants = [len(df_g)]
        activities = [len(df_traces_contained['concept:name'].unique())]
        cases = [len(df_traces_contained['case:concept:name'].unique())]
        states = [len(df_traces_contained['state'].unique())] # ----------------------------------------------------------------This particular event log has states
        df_final = pd.DataFrame({
            'Cases':cases,
            'Events':events_,
            'Activities':activities,
            'Variants': total_variants,
            'States': states, # ----------------------------------------------------------------This particular event log has states
            'year': [year]
        })
        dataframes.append(df_final)
    events_ = [len(event_log_df)]
    total_variants = [len(get_df_traces_total())]
    activities = [len(event_log_df['concept:name'].unique())]
    cases = [len(event_log_df['case:concept:name'].unique())]
    states = [len(event_log_df['state'].unique())] # ----------------------------------------------------------------This particular event log has states
    df_final_ = pd.DataFrame({
        'Cases':cases,
        'Events':events_,
        'Activities':activities,
        'Variants': total_variants,
        'States': states, # ----------------------------------------------------------------This particular event log has states
        'year': ['total']
    })
    years_details_df = pd.concat(dataframes)
    total_df_details = pd.concat([years_details_df,df_final_])
    total_df_details.to_sql(name='overview_details',con=engine,schema='billing',if_exists="replace",index=False)

# Crate Datframe with events per month ---------------------------- { Month and number of activities }
def dataframes_graphs_overview():
    #Count per Month
    month = event_log_df[['time:timestamp','case:concept:name']]
    month['month_year'] = month['time:timestamp'].dt.to_period('M')
    month_ = month.groupby('month_year')['case:concept:name'].count().to_frame().reset_index()
    month_['month_year'] =  month_['month_year'].astype(str)
    month_['month_year'] = pd.to_datetime(month_['month_year'])
    month_.to_sql(name='count_month',con=engine, schema='billing',if_exists='replace',index =False)

    # Events_per Case
    events_per_case_df = event_log_df.groupby(['case:concept:name'])['time:timestamp'].count().to_frame().reset_index()
    events_per_case_df['t'] = 'a'
    events_per_case_df = events_per_case_df.groupby('time:timestamp')['t'].count().to_frame().reset_index()
    events_per_case_df.columns = ['Events per case','Count']
    events_per_case_df = events_per_case_df.sort_values('Count',ascending=False)
    events_per_case_df.to_sql(name='events_per_case_df', con=engine,schema='billing',index=False,if_exists='replace')


    #Activities per case
    activities = event_log_df['concept:name'].unique().tolist()
    numbers = []
    for activity in activities:
        _ = event_log_df[event_log_df['concept:name'] == activity]
        numbers.append(len(_['case:concept:name'].unique()))
    g_df = pd.DataFrame({'activities':activities,'count':numbers})
    g_df['percentage'] = g_df['count'] / len(event_log_df['case:concept:name'].unique()) * 100
    g_df.to_sql(name='activities_per_case', con=engine,schema='billing',index=False,if_exists='replace')

    #Df Canceled
    df_cancelled = event_log_df.groupby(['case:concept:name','isCancelled'])['time:timestamp'].count().to_frame().reset_index()
    df_cancelled = df_cancelled.drop_duplicates(subset=['case:concept:name'],keep ='last')
    df_cancelled =  df_cancelled.groupby('isCancelled')['time:timestamp'].count().to_frame().reset_index()
    df_cancelled.to_sql(name = 'df_canceled', con=engine,schema ="billing",index=False,if_exists='replace')

    #Df_ Closed
    df_closed = event_log_df.groupby(['case:concept:name','isClosed'])['time:timestamp'].count().to_frame().reset_index()
    df_closed = df_closed.drop_duplicates(subset=['case:concept:name'],keep ='last')
    df_closed =  df_closed.groupby('isClosed')['time:timestamp'].count().to_frame().reset_index()
    df_closed.to_sql(name = 'df_closed', con=engine,schema ="billing",index=False,if_exists='replace')


def process_tab(): # ---------------------------- { Month and number of activities }

    def process_level_1():
        #Level 1 
        level_1 = pm.filter_variants(event_log,[df_variants['trace'].to_list()[0]])
        level_1_df = pm.convert_to_dataframe(level_1)
        level_1_heunet = pm.discover_heuristics_net(level_1)
        pm.view_heuristics_net(level_1_heunet)

        # Starting activities & Ending Activities
        start_act_1 = pm.get_start_activities(level_1)
        key_1 = []
        value_1 = []
        for k,v in start_act_1.items():
            key_1.append(k)
            value_1.append(v)
        df_start_act_1 = pd.DataFrame({'Activity':key_1,'number_cases':value_1})
        df_start_act_1.to_sql(name= 'df_start_act_1', schema = 'billing',con= engine,index =False,if_exists='replace')

        end_act_1 = pm.get_end_activities(level_1)
        key_1_e = []
        value_1_e = []
        for k,v in end_act_1.items():
            key_1_e.append(k)
            value_1_e.append(v)
        df_end_act_1 = pd.DataFrame({'Activity':key_1_e,'number_cases':value_1_e})
        df_end_act_1['Percentage'] = df_end_act_1['number_cases'] / len(level_1_df['case:concept:name'].unique()) * 100 
        df_end_act_1.to_sql(name= 'df_end_act_1', schema = 'billing',con= engine,index =False,if_exists='replace')

        #% Ending Activities
        plot_ends_1 = plx.bar(data_frame=df_end_act_1,y = 'Activity',x = 'Percentage')
        #plot_ends_1

        #Business Process Model
        bpmn_1 = pm.discover_bpmn_inductive(level_1)
        pm.view_bpmn(bpmn_1)

        df_variants_level_1 = variants.get_variants_df(level_1)
        df_variants_level_1 =  df_variants_level_1[['trace','len','percentage','Variant_Name']]
        df_variants_level_1['len_trace'] = [len(x) for x in df_variants_level_1['trace'].to_list() ]
        df_variants_level_1.to_sql(name = 'df_variants_level_1', schema = 'billing',con = engine, if_exists='replace',index = False)

        #lenght_variant
        len_variance_1 = plx.bar(df_variants_level_1,x = 'Variant_Name', y = 'len_trace' )
        len_variance_1
        ocurrance_1 = plx.bar(df_variants_level_1,x = 'Variant_Name', y = 'percentage')
        ocurrance_1


        #Petri Net Inductive
        net_inductive_1, im_inductive_1, fm_inductive_1 = pm.discover_petri_net_inductive(level_1)
        pm.view_petri_net(net_inductive_1, im_inductive_1, fm_inductive_1)
        # Petri Net alpha
        net_alpha_1, im_alpha_1, fm_alpha_1 = pm.discover_petri_net_alpha(level_1)
        pm.view_petri_net(net_alpha_1, im_alpha_1, fm_alpha_1)
        #Petrinet alpha plus
        net_alphaplus_1, im_alphaplus_1, fm_alphaplus_1 = pm.discover_petri_net_alpha_plus(level_1)
        pm.view_petri_net(net_alphaplus_1, im_alphaplus_1, fm_alphaplus_1 )

    def process_level_16():
        #Level 1 
        level_16 = pm.filter_variants(event_log,df_variants['trace'].to_list()[0:4])
        level_16_df = pm.convert_to_dataframe(level_16)
        level_16_heunet = pm.discover_heuristics_net(level_16)
        pm.view_heuristics_net(level_16_heunet)

        start_act_16 = pm.get_start_activities(level_16)
        key_16 = []
        value_16 = []
        for k,v in start_act_16.items():
            key_16.append(k)
            value_16.append(v)
        df_start_act_16 = pd.DataFrame({'Activity':key_16,'number_cases':value_16})
        df_start_act_16.to_sql(name= 'df_start_act_16', schema = 'billing',con= engine,index =False,if_exists='replace')


        end_act_16 = pm.get_end_activities(level_16)
        key_16_e = []
        value_16_e = []
        for k,v in end_act_16.items():
            key_16_e.append(k)
            value_16_e.append(v)
        df_end_act_16 = pd.DataFrame({'Activity':key_16_e,'number_cases':value_16_e})
        df_end_act_16['Percentage'] = df_end_act_16['number_cases'] / len(level_16_df['case:concept:name'].unique()) * 100 
        df_end_act_16.to_sql(name= 'df_end_act_16', schema = 'billing',con= engine,index =False,if_exists='replace')

        #% Ending Activities
        plot_ends_16 = plx.bar(data_frame=df_end_act_16,y = 'Activity',x = 'Percentage')
        plot_ends_16

        #Business Process Model
        bpmn_16 = pm.discover_bpmn_inductive(level_16)
        pm.view_bpmn(bpmn_16)


        df_variants_level_16 = variants.get_variants_df(level_16)
        df_variants_level_16 =  df_variants_level_16[['trace','len','percentage','Variant_Name']]
        df_variants_level_16['len_trace'] = [len(x) for x in df_variants_level_16['trace'].to_list() ]
        df_variants_level_16.to_sql(name = 'df_variants_level_16', schema = 'billing',con = engine, if_exists='replace',index = False)

        len_variance_16 = plx.bar(df_variants_level_16,x = 'Variant_Name', y = 'len_trace' )
        #len_variance_16
        ocurrance_16 = plx.bar(df_variants_level_16,x = 'Variant_Name', y = 'percentage')
        ocurrance_16


        #Petri Net Inductive
        net_inductive_16, im_inductive_16, fm_inductive_16 = pm.discover_petri_net_inductive(level_16)
        pm.view_petri_net(net_inductive_16, im_inductive_16, fm_inductive_16)
        # Petri Net alpha
        net_alpha_16, im_alpha_16, fm_alpha_16 = pm.discover_petri_net_alpha(level_16)
        pm.view_petri_net(net_alpha_16, im_alpha_16, fm_alpha_16)
        #Petrinet alpha plus
        net_alphaplus_16, im_alphaplus_16, fm_alphaplus_16 = pm.discover_petri_net_alpha_plus(level_16)
        pm.view_petri_net(net_alphaplus_16, im_alphaplus_16, fm_alphaplus_16 )

    def process_level_46():
        #Level 46 
        level_46 = pm.filter_variants(event_log,df_variants['trace'].to_list()[0:12])
        level_46_df = pm.convert_to_dataframe(level_46)
        level_46_heunet = pm.discover_heuristics_net(level_46)
        pm.view_heuristics_net(level_46_heunet)

        start_act_46 = pm.get_start_activities(level_46)
        key_46 = []
        value_46 = []
        for k,v in start_act_46.items():
            key_46.append(k)
            value_46.append(v)
        df_start_act_46 = pd.DataFrame({'Activity':key_46,'number_cases':value_46})
        df_start_act_46.to_sql(name= 'df_start_act_46', schema = 'billing',con= engine,index =False,if_exists='replace')


        end_act_46 = pm.get_end_activities(level_46)
        key_46_e = []
        value_46_e = []
        for k,v in end_act_46.items():
            key_46_e.append(k)
            value_46_e.append(v)
        df_end_act_46 = pd.DataFrame({'Activity':key_46_e,'number_cases':value_46_e})
        df_end_act_46['Percentage'] = df_end_act_46['number_cases'] / len(level_46_df['case:concept:name'].unique()) * 100 
        df_end_act_46.to_sql(name= 'df_end_act_46', schema = 'billing',con= engine,index =False,if_exists='replace')


        #% Ending Activities
        plot_ends_46 = plx.bar(data_frame=df_end_act_46,y = 'Activity',x = 'Percentage')
        plot_ends_46

        #Business Process Model
        bpmn_46 = pm.discover_bpmn_inductive(level_46)
        pm.view_bpmn(bpmn_46)


        df_variants_level_46 = variants.get_variants_df(level_46)
        df_variants_level_46 =  df_variants_level_46[['trace','len','percentage','Variant_Name']]
        df_variants_level_46['len_trace'] = [len(x) for x in df_variants_level_46['trace'].to_list() ]
        df_variants_level_46.to_sql(name = 'df_variants_level_46', schema = 'billing',con = engine, if_exists='replace',index = False)



        len_variance_46 = plx.bar(df_variants_level_46,x = 'Variant_Name', y = 'len_trace' )
        len_variance_46
        ocurrance_46 = plx.bar(df_variants_level_46,x = 'Variant_Name', y = 'percentage')
        ocurrance_46


        #Petri Net Inductive
        net_inductive_46, im_inductive_46, fm_inductive_46 = pm.discover_petri_net_inductive(level_46)
        pm.view_petri_net(net_inductive_46, im_inductive_46, fm_inductive_46)
        # Petri Net alpha
        net_alpha_46, im_alpha_46, fm_alpha_46 = pm.discover_petri_net_alpha(level_46)
        pm.view_petri_net(net_alpha_46, im_alpha_46, fm_alpha_46)
        #Petrinet alpha plus
        net_alphaplus_46, im_alphaplus_46, fm_alphaplus_46 = pm.discover_petri_net_alpha_plus(level_46)
        pm.view_petri_net(net_alphaplus_46, im_alphaplus_46, fm_alphaplus_46 )

    def process_level_61():
        #Level 61 
        level_61 = pm.filter_variants(event_log,df_variants['trace'].to_list()[0:60])
        level_61_df = pm.convert_to_dataframe(level_61)
        level_61_heunet = pm.discover_heuristics_net(level_61)
        pm.view_heuristics_net(level_61_heunet)

        start_act_61 = pm.get_start_activities(level_61)
        key_61 = []
        value_61 = []
        for k,v in start_act_61.items():
            key_61.append(k)
            value_61.append(v)
        df_start_act_61 = pd.DataFrame({'Activity':key_61,'number_cases':value_61})
        df_start_act_61.to_sql(name= 'df_start_act_61', schema = 'billing',con= engine,index =False,if_exists='replace')


        end_act_61 = pm.get_end_activities(level_61)
        key_61_e = []
        value_61_e = []
        for k,v in end_act_61.items():
            key_61_e.append(k)
            value_61_e.append(v)
        df_end_act_61 = pd.DataFrame({'Activity':key_61_e,'number_cases':value_61_e})
        df_end_act_61['Percentage'] = df_end_act_61['number_cases'] / len(level_61_df['case:concept:name'].unique()) * 100 
        df_end_act_61.to_sql(name= 'df_end_act_61', schema = 'billing',con= engine,index =False,if_exists='replace')


        #% Ending Activities
        plot_ends_61 = plx.bar(data_frame=df_end_act_61,y = 'Activity',x = 'Percentage')
        plot_ends_61

        #Business Process Model
        bpmn_61 = pm.discover_bpmn_inductive(level_61)
        pm.view_bpmn(bpmn_61)


        df_variants_level_61 = variants.get_variants_df(level_61)
        df_variants_level_61 =  df_variants_level_61[['trace','len','percentage','Variant_Name']]
        df_variants_level_61['len_trace'] = [len(x) for x in df_variants_level_61['trace'].to_list() ]
        df_variants_level_61.to_sql(name = 'df_variants_level_61', schema = 'billing',con = engine, if_exists='replace',index = False)



        len_variance_61 = plx.bar(df_variants_level_61,x = 'Variant_Name', y = 'len_trace' )
        len_variance_61
        ocurrance_61 = plx.bar(df_variants_level_61,x = 'Variant_Name', y = 'percentage')
        ocurrance_61


        #Petri Net Inductive
        net_inductive_61, im_inductive_61, fm_inductive_61 = pm.discover_petri_net_inductive(level_61)
        pm.view_petri_net(net_inductive_61, im_inductive_61, fm_inductive_61)
        # Petri Net alpha
        net_alpha_61, im_alpha_61, fm_alpha_61 = pm.discover_petri_net_alpha(level_61)
        pm.view_petri_net(net_alpha_61, im_alpha_61, fm_alpha_61)
        #Petrinet alpha plus
        net_alphaplus_61, im_alphaplus_61, fm_alphaplus_61 = pm.discover_petri_net_alpha_plus(level_61)
        pm.view_petri_net(net_alphaplus_61, im_alphaplus_61, fm_alphaplus_61 )

    def process_level_76():
        #Level 76 
        level_76 = pm.filter_variants(event_log,df_variants['trace'].to_list()[0:120])
        level_76_df = pm.convert_to_dataframe(level_76)
        level_76_heunet = pm.discover_heuristics_net(level_76)
        pm.view_heuristics_net(level_76_heunet)

        start_act_76 = pm.get_start_activities(level_76)
        key_76 = []
        value_76 = []
        for k,v in start_act_76.items():
            key_76.append(k)
            value_76.append(v)
        df_start_act_76 = pd.DataFrame({'Activity':key_76,'number_cases':value_76})
        df_start_act_76.to_sql(name= 'df_start_act_76', schema = 'billing',con= engine,index =False,if_exists='replace')


        end_act_76 = pm.get_end_activities(level_76)
        key_76_e = []
        value_76_e = []
        for k,v in end_act_76.items():
            key_76_e.append(k)
            value_76_e.append(v)
        df_end_act_76 = pd.DataFrame({'Activity':key_76_e,'number_cases':value_76_e})
        df_end_act_76['Percentage'] = df_end_act_76['number_cases'] / len(level_76_df['case:concept:name'].unique()) * 100 
        df_end_act_76.to_sql(name= 'df_end_act_76', schema = 'billing',con= engine,index =False,if_exists='replace')


        #% Ending Activities
        plot_ends_76 = plx.bar(data_frame=df_end_act_76,y = 'Activity',x = 'Percentage')
        plot_ends_76

        #Business Process Model
        bpmn_76 = pm.discover_bpmn_inductive(level_76)
        pm.view_bpmn(bpmn_76)


        df_variants_level_76 = variants.get_variants_df(level_76)
        df_variants_level_76 =  df_variants_level_76[['trace','len','percentage','Variant_Name']]
        df_variants_level_76['len_trace'] = [len(x) for x in df_variants_level_76['trace'].to_list() ]
        df_variants_level_76.to_sql(name = 'df_variants_level_76', schema = 'billing',con = engine, if_exists='replace',index = False)



        len_variance_76 = plx.bar(df_variants_level_76,x = 'Variant_Name', y = 'len_trace' )
        len_variance_76
        ocurrance_76 = plx.bar(df_variants_level_76,x = 'Variant_Name', y = 'percentage')
        ocurrance_76


        #Petri Net Inductive
        net_inductive_76, im_inductive_76, fm_inductive_76 = pm.discover_petri_net_inductive(level_76)
        pm.view_petri_net(net_inductive_76, im_inductive_76, fm_inductive_76)
        # Petri Net alpha
        net_alpha_76, im_alpha_76, fm_alpha_76 = pm.discover_petri_net_alpha(level_76)
        pm.view_petri_net(net_alpha_76, im_alpha_76, fm_alpha_76)
        #Petrinet alpha plus
        net_alphaplus_76, im_alphaplus_76, fm_alphaplus_76 = pm.discover_petri_net_alpha_plus(level_76)
        pm.view_petri_net(net_alphaplus_76, im_alphaplus_76, fm_alphaplus_76 )

    def process_level_91():

        level_91 = pm.filter_variants(event_log,df_variants['trace'].to_list()[0:650])
        level_91_df = pm.convert_to_dataframe(level_91)
        level_91_heunet = pm.discover_heuristics_net(level_91)
        pm.view_heuristics_net(level_91_heunet)

        start_act_91 = pm.get_start_activities(level_91)
        key_91 = []
        value_91 = []
        for k,v in start_act_91.items():
            key_91.append(k)
            value_91.append(v)
        df_start_act_91 = pd.DataFrame({'Activity':key_91,'number_cases':value_91})
        df_start_act_91.to_sql(name= 'df_start_act_91', schema = 'billing',con= engine,index =False,if_exists='replace')


        end_act_91 = pm.get_end_activities(level_91)
        key_91_e = []
        value_91_e = []
        for k,v in end_act_91.items():
            key_91_e.append(k)
            value_91_e.append(v)
        df_end_act_91 = pd.DataFrame({'Activity':key_91_e,'number_cases':value_91_e})
        df_end_act_91['Percentage'] = df_end_act_91['number_cases'] / len(level_91_df['case:concept:name'].unique()) * 100 
        df_end_act_91.to_sql(name= 'df_end_act_91', schema = 'billing',con= engine,index =False,if_exists='replace')

        #% Ending Activities
        plot_ends_91 = plx.bar(data_frame=df_end_act_91,y = 'Activity',x = 'Percentage')
        plot_ends_91

        #Business Process Model
        bpmn_91 = pm.discover_bpmn_inductive(level_91)
        pm.view_bpmn(bpmn_91)


        df_variants_level_91 = variants.get_variants_df(level_91)
        df_variants_level_91 =  df_variants_level_91[['trace','len','percentage','Variant_Name']]
        df_variants_level_91['len_trace'] = [len(x) for x in df_variants_level_91['trace'].to_list() ]
        df_variants_level_91.to_sql(name = 'df_variants_level_91', schema = 'billing',con = engine, if_exists='replace',index = False)

        len_variance_91 = plx.bar(df_variants_level_91,x = 'Variant_Name', y = 'len_trace' )
        len_variance_91
        ocurrance_91 = plx.bar(df_variants_level_91,x = 'Variant_Name', y = 'percentage')
        ocurrance_91

        #Petri Net Inductive
        net_inductive_91, im_inductive_91, fm_inductive_91 = pm.discover_petri_net_inductive(level_91)
        pm.view_petri_net(net_inductive_91, im_inductive_91, fm_inductive_91)
        # Petri Net alpha
        net_alpha_91, im_alpha_91, fm_alpha_91 = pm.discover_petri_net_alpha(level_91)
        pm.view_petri_net(net_alpha_91, im_alpha_91, fm_alpha_91)
        #Petrinet alpha plus
        net_alphaplus_91, im_alphaplus_91, fm_alphaplus_91 = pm.discover_petri_net_alpha_plus(level_91)
        pm.view_petri_net(net_alphaplus_91, im_alphaplus_91, fm_alphaplus_91 )


if __name__ == "__main__":
    get_df_traces_total()
    get_overview_info()
    dataframes_graphs_overview()
    process_tab()