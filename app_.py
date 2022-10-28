
import pandas as pd
import numpy as np
import plotly.express as plx
import streamlit as st
#import pm4py
import streamlit_nested_layout
st.set_page_config(layout="wide")
from PIL import Image
from io import BytesIO
from sqlalchemy import create_engine


#db_connection
db_provider = "postgresql://"
user = "ubuntu1"
password ="3004222950a"
address  = "20.226.14.116:5432/postgres"
engine = create_engine(db_provider + user + ":" + password  + '@'+ address)




def title_centered_h3(str_):
    title = st.markdown("""<h3 style='text-align: center'>""" + str(str_) +"""</h3>""",unsafe_allow_html =True)
    return title


def title_centered_h1(str_):
    title = st.markdown("""<h1 style='text-align: center'>""" + str(str_) +"""</h1>""",unsafe_allow_html =True)
    return title

def cent_text(str_):
    title = st.markdown("""<p style='text-align: center'>""" + str(str_) +"""</p>""",unsafe_allow_html =True)
    return title


#useful functions

def transp_corr(dataframe):
    xc = dataframe.T
    xc.columns = xc.iloc[0,:]
    xc = xc.drop(xc.index[0])
    return xc 


def download_image(path):
    im_ = Image.open(path)
    buf_ = BytesIO()
    im_.save(buf_,format='png')
    bytes_im = buf_.getvalue()
    return bytes_im



#total_df_details =pd.read_sql("""SELECT "Cases", "Events", "Activities", "Variants", "States", year FROM billing.overview_details;""",con=engine) ######## ----------------------Check if this can be moved to the begining of the Script
#df_variants = pd.read_sql(sql ="""SELECT * FROM billing.variants_total_df""",con=engine)
#month_ = pd.read_sql("""SELECT "month_year","case:concept:name" FROM billing.count_month;""",con=engine)
#month_['month_year'] = pd.to_datetime(month_['month_year'])
#variants_total_df = pd.read_sql("""select * from billing.variants_total_df""",con=engine)
#events_per_case_df = pd.read_sql("""SELECT * FROM  billing.events_per_case_df""",con=engine)
#activities_per_case = pd.read_sql("""SELECT activities, count, percentage FROM billing.activities_per_case;""",con=engine)
#df_canceled = pd.read_sql("""SELECT * FROM billing.df_canceled""", con= engine)
#df_closed = pd.read_sql("""SELECT * FROM billing.df_closed""", con= engine)


#df_start_act_1 = pd.read_sql(sql = """SELECT * FROM billing.df_start_act_1""",con = engine)
#df_end_act_1 = pd.read_sql(sql = """SELECT * FROM billing.df_end_act_1""",con = engine)
#df_variants_level_1 = pd.read_sql(sql = """SELECT * FROM billing.df_variants_level_1""",con = engine)

#df_start_act_16 = pd.read_sql("""SELECT * FROM billing.df_start_act_16""", con= engine)
#df_end_act_16 = pd.read_sql("""SELECT * FROM billing.df_end_act_16""", con= engine)
#df_variants_level_16 = pd.read_sql("""SELECT * FROM billing.df_variants_level_16""", con= engine)

#df_start_act_31 = pd.read_sql("""SELECT * FROM billing.df_start_act_31""", con= engine)
#df_end_act_31 = pd.read_sql("""SELECT * FROM billing.df_end_act_31""", con= engine)
#df_variants_level_31 = pd.read_sql("""SELECT * FROM billing.df_variants_level_31""", con= engine)

#df_start_act_46 = pd.read_sql("""SELECT * FROM billing.df_start_act_46""", con= engine)
#df_end_act_46 = pd.read_sql("""SELECT * FROM billing.df_end_act_46""", con= engine)
#df_variants_level_46 = pd.read_sql("""SELECT * FROM billing.df_variants_level_46""", con= engine)

#df_start_act_61 = pd.read_sql("""SELECT * FROM billing.df_start_act_61""", con= engine)
#df_end_act_61 = pd.read_sql("""SELECT * FROM billing.df_end_act_61""", con= engine)
#df_variants_level_61 = pd.read_sql("""SELECT * FROM billing.df_variants_level_61""", con= engine)

#df_start_act_76 = pd.read_sql("""SELECT * FROM billing.df_start_act_76""", con= engine)
#df_end_act_76 = pd.read_sql("""SELECT * FROM billing.df_end_act_76""", con= engine)
#df_variants_level_76 = pd.read_sql("""SELECT * FROM billing.df_variants_level_76""", con= engine)

#df_start_act_91 = pd.read_sql("""SELECT * FROM billing.df_start_act_91""", con= engine)
#df_end_act_91 = pd.read_sql("""SELECT * FROM billing.df_end_act_91""", con= engine)
#df_variants_level_91 = pd.read_sql("""SELECT * FROM billing.df_variants_level_91""", con= engine)

#df_start_act_100 = pd.read_sql("""SELECT * FROM billing.df_start_act_100""", con= engine)
#df_end_act_100 = pd.read_sql("""SELECT * FROM billing.df_end_act_100""", con= engine)
#df_variants_level_100 = pd.read_sql("""SELECT * FROM billing.df_variants_level_100""", con= engine)


total_df_details = pd.read_csv("dataframes/overview_details.csv")
df_variants = pd.read_csv('dataframes/variants_total_df.csv')
month_ = pd.read_csv("dataframes/count_month.csv")
month_['month_year'] = pd.to_datetime(month_['month_year'])
variants_total_df =  pd.read_csv('dataframes/variants_total_df.csv')
events_per_case_df= pd.read_csv('dataframes/events_per_case_df.csv')
activities_per_case =  pd.read_csv('dataframes/activities_per_case.csv')
df_canceled=  pd.read_csv('dataframes/df_canceled.csv')
df_closed=  pd.read_csv('dataframes/df_closed.csv')


df_start_act_1 = pd.read_csv('dataframes/df_start_act_1.csv')
df_end_act_1 = pd.read_csv('dataframes/df_end_act_1.csv')
df_variants_level_1 = pd.read_csv('dataframes/df_variants_level_1.csv')


df_start_act_16 = pd.read_csv('dataframes/df_start_act_16.csv')
df_end_act_16 = pd.read_csv('dataframes/df_end_act_16.csv')
df_variants_level_16 = pd.read_csv('dataframes/df_variants_level_16.csv')


df_start_act_31 = pd.read_csv('dataframes/df_start_act_31.csv')
df_end_act_31 = pd.read_csv('dataframes/df_end_act_31.csv')
df_variants_level_31 = pd.read_csv('dataframes/df_variants_level_31.csv')

df_start_act_46 = pd.read_csv('dataframes/df_start_act_46.csv')
df_end_act_46 = pd.read_csv('dataframes/df_end_act_46.csv')
df_variants_level_46 = pd.read_csv('dataframes/df_variants_level_46.csv')

df_start_act_61 = pd.read_csv('dataframes/df_start_act_61.csv')
df_end_act_61 = pd.read_csv('dataframes/df_end_act_61.csv')
df_variants_level_61 = pd.read_csv('dataframes/df_variants_level_61.csv')

df_start_act_76 = pd.read_csv('dataframes/df_start_act_76.csv')
df_end_act_76 = pd.read_csv('dataframes/df_end_act_76.csv')
df_variants_level_76 = pd.read_csv('dataframes/df_variants_level_76.csv')

df_start_act_91 = pd.read_csv('dataframes/df_start_act_91.csv')
df_end_act_91 = pd.read_csv('dataframes/df_end_act_91.csv')
df_variants_level_91 = pd.read_csv('dataframes/df_variants_level_91.csv')

df_start_act_100 = pd.read_csv('dataframes/df_start_act_100.csv')
df_end_act_100 = pd.read_csv('dataframes/df_end_act_100.csv')
df_variants_level_100 = pd.read_csv('dataframes/df_variants_level_100.csv')


time_head =pd.read_csv('dataframes/time_head.csv')
cases_df_list = pd.read_csv('dataframes\cases_df_list.csv')



# --------------                 #  Select Slider  -------------------------- Left --------------------------------------------------------------------------------------------------------------
# --------------                 #  Select Slider  -------------------------- Left --------------------------------------------------------------------------------------------------------------
# --------------                 #  Select Slider  -------------------------- Left --------------------------------------------------------------------------------------------------------------

selectbox = st.sidebar.selectbox("Available Options for you to explore",('Intro','Overview','Timing','Process','Data'))
with st.sidebar:
    st.markdown("<br>",unsafe_allow_html=True)
    st.info("If assistance is required, contact  Alejandro Velez")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.info("Updated : October 2022")
                             
# ---------------                #  Intro Page   -------------------------------------------------------------------------------------------------------------- 
# ---------------                #  Intro Page   -------------------------------------------------------------------------------------------------------------- 
# ---------------                #  Intro Page   -------------------------------------------------------------------------------------------------------------- 
# ---------------                #  Intro Page   -------------------------------------------------------------------------------------------------------------- 

if selectbox == 'Intro':
    st.markdown("""<h1 style='text-align: center'>Introduction  - Process Mining Project Net</h1>""",unsafe_allow_html=True) 
    y1,y2 = st.columns(2)
    with y2:
        ##st.image(r'Images\1-j3dTgXjyaYPo9XkM6UMZ3g-removebg-preview.png',use_column_width=True )
        st.image(r'images\logo1.png')
        #st.markdown("""<h1 style='text-align: center'> IMAGE GOES HERE !!! </h1>""",unsafe_allow_html=True)    
    with y1:
        st.markdown("<br>",unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html=True)
        st.markdown(
            """
            <p style="text-align:justify">
                Definition: Process mining is a family of techniques relating the fields of data
                science and process management to support the analysis of operational processes based on event logs. 
                The goal of process mining is to turn event  data into insights and actions. Process mining 
                is an integral part of data science, fueled by the availability of event data and 
                the desire to improve processes.[1] Process mining techniques use event data to show 
                what people, machines, and organizations are really doing. Process mining provides novel insights 
                that can be used to identify the executional path taken by operational processes and address their
                performance and compliance problems.
            </p>
            """,unsafe_allow_html=True)
    st.markdown("<hr>",unsafe_allow_html=True)
    with st.expander("Expand to see the basic layout of the project architecture"):
        v1,v2,v3,v4,v5,v6,v7 = st.columns([1,1,1,17,1,1,1]) 
        with v4: 
            st.image(r'images\logo2.png',use_column_width=True )
            #st.markdown("""<h1 style='text-align: center'> IMAGE GOES HERE !!! </h1>""",unsafe_allow_html=True)
    i1,i2 = st.columns([2,1])
    with i1:
        st.markdown("""
            <p style="text-align:justify">
                Designed to be used in both academia and industry, PM4Py is
                the leading open source process mining platform written in Python, implementing:
                Conformance Checking,Process Discovery, BPMN Support, Open XES/Importing & Exporting.
            </p> """,unsafe_allow_html=True) 
        st.markdown("""    
            <p style="text-align:justify">
                The term "Process mining" was first coined in a research proposal written by the Dutch
                computer scientist Wil van der Aalst ("Godfather of Process mining"). Thus began a new field of research that emerged 
                under the umbrella of techniques related to data science and process science at the Eindhoven University in 1999. 
                In the early days, process mining techniques were often convoluted with the techniques used for workflow management. 
                In the year 2000, the very first practically applicable algorithm for process discovery, "Alpha miner" 
                was developed. The very next year, in 2001, a much similar algorithm based on heuristics called "Heuristic miner"
                was introduced in the research papers. Further along the link more powerful algorithms such as inductive miner 
                were developed for process discovery. As the field of process mining began to evolve, 
                conformance checking became an integral part of it.
        """,unsafe_allow_html=True)

        with i2:
            st.markdown("""<h3 style="text-align:center"> Resources </h3>""",unsafe_allow_html=True)
            st.markdown("""<a href="https://www.python.org/" >Python - Official Site</a>""",unsafe_allow_html=True)
            st.markdown("""<a href="https://pm4py.fit.fraunhofer.de/" >PM4PY - Official Site</a>""",unsafe_allow_html=True)
            st.markdown("""<a href="https://streamlit.io/" >Streamlit - Official Site</a>""",unsafe_allow_html=True)
            st.markdown("""<a href="https://azure.microsoft.com/en-us/" >Azure - Official Site</a>""",unsafe_allow_html=True)
            st.markdown("""<a href="https://github.com/jhonalevc/Process-Mining-Hospital" >Github repo with the code </a>""",unsafe_allow_html=True)

# ---------------                #  Overview Page   -------------------------------------------------------------------------------------------------------------- 
# ---------------                #  Overview Page   -------------------------------------------------------------------------------------------------------------- 
# ---------------                #  Overview Page   -------------------------------------------------------------------------------------------------------------- 
# ---------------                #  Overview Page   --------------------------------------------------------------------------------------------------------------


if selectbox == 'Overview':
    st.markdown("""<h1 style='text-align: center'>Overview</h1>""", unsafe_allow_html= True)
    with st.container(): # ---------------- Container expander Years
        with st.expander("Basic Info on the Eventlog"):
            q1,q2,q3,q4,q5 = st.columns([1,1,3,1,1])
            with q3:
                global option_header_period
                option_header_period = st.radio("Select Year",total_df_details['year'],label_visibility ='hidden',index=5,horizontal=True)
    with st.container(): # ---------------- Container Overview Information
        total_df_details = total_df_details[total_df_details['year'] == option_header_period]
        col1,col2,col3,col4,col5,col6 = st.columns(6)
        with col1:
            st.subheader('Cases')
            st.markdown(total_df_details['Cases'].to_list()[0])
        with col2:
            st.subheader('Events')
            st.markdown(total_df_details['Events'].to_list()[0])
        with col3:
            st.subheader('Activities')
            st.markdown(total_df_details['Activities'].to_list()[0])
        with col4:
            st.subheader('Variants')
            st.markdown(total_df_details['Variants'].to_list()[0])
        with col5:
            st.subheader('States')
            st.markdown(total_df_details['States'].to_list()[0])
        with col6:
            st.subheader('Period')
            st.markdown(total_df_details['year'].to_list()[0])
    st.markdown("<hr>",unsafe_allow_html=True)
    with st.container(): # ---------------- Container With first plot and filter for month and year
        w1,w2 = st.columns(2)
        with w1:
            global monthly_yearly
            monthly_yearly = st.radio('Year-Month', ['Year','Month'],index=0)
        with w2:
            if monthly_yearly == 'Month':
                months = month_['month_year'].dt.month.unique()
                month_ = month_.copy()
                month_['month'] = month_['month_year'].dt.month
                month_ = month_.groupby('month')['case:concept:name'].sum().to_frame().reset_index()
                month_.columns = ['month_year','case:concept:name']
                st.error("Montlhy Data")
                month_d = month_.copy()
            else:
                year_select = st.selectbox('Select Year', options = month_['month_year'].dt.year.unique().tolist() + ['Total'] ,index = 5)
                if year_select == 'Total':
                    month_d = month_.copy()
                else:
                    month_d = month_[month_['month_year'].dt.year == year_select]
        try:
            if year_select == 2012:
                st.error("Only one Month to display")
            elif year_select == 2016:
                st.error("Only one Month to display")
        except:
            pass
        plot_month = plx.area(month_d,x ='month_year', y='case:concept:name')
        st.plotly_chart(plot_month,use_container_width=True)
    st.markdown("<hr>",unsafe_allow_html=True)
    with st.container(): # ---------------- Container with Three Plots
        e1,e2,e3 = st.columns(3)
        with e1:
            st.markdown("""<h3 style='text-align: center'>Variants</h3>""",unsafe_allow_html = True)
            variants_total_plot = plx.bar(variants_total_df.head(25),x = 'Variant_Name', y='percentage')
            st.plotly_chart(variants_total_plot,use_container_width=True)
        with e2:
            st.markdown("""<h3 style='text-align: center'>Events per Case</h3>""",unsafe_allow_html = True)
            events_per_case_df['%'] = events_per_case_df['Count'] / events_per_case_df['Count'].sum() * 100
            events_per_case_df['Events per case'] = events_per_case_df['Events per case'].astype(str) 
            events_per_Case_plot = plx.bar(events_per_case_df,x = '%', y='Events per case')
            st.plotly_chart(events_per_Case_plot,use_container_width=True)
        with e3:
            st.markdown("""<h3 style='text-align: center'>Activities</h3>""",unsafe_allow_html = True)
            activities_plot = plx.bar(activities_per_case, x = 'activities',y='percentage' )
            st.plotly_chart(activities_plot,use_container_width=True)
    st.markdown("<hr>",unsafe_allow_html=True)
    with st.container(): # ---------------- Container with df closed and df canceled
        r1,r2 =  st.columns(2)
        with r1:
            st.markdown("""<h3 style='text-align: center'>Is Cancelled</h3>""",unsafe_allow_html=True)
            plot_pie_canceled = plx.pie(data_frame=df_canceled,names ='isCancelled',values = 'time:timestamp')
            st.plotly_chart(plot_pie_canceled,use_container_width=True)
            with st.expander("Details"):
                r1_1 ,r1_2 = st.columns(2)
                with r1_1:
                    st.markdown("""<p align="justify">According to the Dataset documentation : isCancelled -  A flag that indicates whether the billing package  was eventually cancelled.</p>""", unsafe_allow_html=True)
                with r1_2:
                    df_canceled
        with r2:
            st.markdown("""<h3 style='text-align: center'>Is Closed</h3>""",unsafe_allow_html=True)
            with st.expander("Details"):
                r2_1 ,r2_2 = st.columns(2)
                with r2_1:
                    st.markdown("""<p align="justify">According to the Dataset documentation : isClosed -  A flag that indicates whether the billing package  was eventually cancelled.</p>""", unsafe_allow_html=True)
                with r2_2:
                    df_closed
            plot_pie_closed = plx.pie(data_frame=df_closed,names ='isClosed',values = 'time:timestamp')
            st.plotly_chart(plot_pie_closed,use_container_width=True)  


# ---------------                #  Timing Page   -------------------------------------------------------------------------------------------------------------- 
# ---------------                #  Timing Page   -------------------------------------------------------------------------------------------------------------- 
# ---------------                #  Timing Page   -------------------------------------------------------------------------------------------------------------- 
# ---------------                #  Timing Page   --------------------------------------------------------------------------------------------------------------

if selectbox == 'Timing':
    title_centered_h1('Timing')
    with st.container():
        v1,v2,v3,v4,v5,v6 = st.columns(6)
        with v1:
            title_centered_h3('Initial Time')
            st.markdown(time_head['min_time'].to_list()[0])
        with v2:
            st.markdown("<hr>",unsafe_allow_html=True)   
        with v3:
            st.markdown("<hr>",unsafe_allow_html=True)
        with v4:
            st.markdown("<hr>",unsafe_allow_html=True)
        with v5:
            st.markdown("<hr>",unsafe_allow_html=True)
        with v6:
            title_centered_h3('Ending Time')
            st.markdown(time_head['max_time'].to_list()[0])
        with st.expander("Time elapsed Details"):
            y1,y2,y3,y4,y5 = st.columns(5)
            with y2:
                title_centered_h3('Days')
                cent_text(time_head['days'].to_list()[0])
            with y3:
                title_centered_h3('Hours')
                cent_text(time_head['hours'].to_list()[0])
            with y4:
                title_centered_h3('Minutes')
                cent_text(time_head['minutes'].to_list()[0])
    st.markdown("<hr>",unsafe_allow_html=True)
    with st.container():
        f1,f2 = st.columns([2,1])
        with f1:
            global select_case, df_selected_variant, df_time_case_variant
            select_case = st.selectbox('Select case', cases_df_list['case:concept:name'])
            query = """SELECT "case:concept:name" , sum(interval) as interval FROM billing.cases_df WHERE "case:concept:name" = """ + """'""" +select_case + """'""" + """  OR "case:concept:name" IN ('A','G','HH','D','DF') group by "case:concept:name";"""
            query_1 = """SELECT "Variant" FROM billing.dfs_case_variant WHERE "case" = """ + """'""" + select_case +"""';"""
            query_2 = """SELECT * FROM billing.cases_df WHERE "case:concept:name" = """ +"""'"""+select_case+"""';"""
            df_plot_duration = pd.read_sql(sql = query, con= engine)
            df_selected_variant = pd.read_sql(sql = query_1, con=engine)
            df_time_case_variant = pd.read_sql(sql = query_2,con=engine)
            df_time_case_variant['interval'] = df_time_case_variant['interval'].round(decimals =2) 
            duration_bar_plot = plx.bar(df_plot_duration, x ='case:concept:name', y = 'interval')
            st.plotly_chart(duration_bar_plot,use_container_width =True)
        with f2:
            g1,g2,g3 = st.columns(3)
            with g1:
                title_centered_h3("Variant")
                cent_text(df_selected_variant['Variant'].to_list()[0])
            with g2:
                title_centered_h3("Case")
                cent_text(select_case)
            with g3:
                title_centered_h3("Time Elapsed In hours")
                cent_text(str(df_time_case_variant['interval'].sum()))
            st.markdown("<hr>",unsafe_allow_html = True)
            st.dataframe(df_time_case_variant[['time:timestamp','concept:name','interval']], use_container_width = True)
    st.markdown("<hr>",unsafe_allow_html =True)
    with st.container():
        o1,o2 = st.columns([1,2])
        with o1:
            global variant_activity_radio
            variant_activity_radio = st.radio('Select',['Variant','Activity'],horizontal =True)
        if variant_activity_radio == "Variant":
            with o2:
                global select_variant
                select_variant = st.selectbox('Select variant',label_visibility ='hidden',options = ['Variant_'+str(i) for i in np.arange(len(df_variants))])
        else:
            with o2:
                global select_activity
                select_activity = st.selectbox("Select Activity",label_visibility ='hidden',options = pd.read_sql("""SELECT DISTINCT("concept:name") FROM billing.full_case_variant_time""", con = engine)['concept:name'])
        p1,p2 = st.columns([1,2])
        if variant_activity_radio == 'Variant':
            with p1:
                query__1 = """SELECT * 	FROM billing.avegare_interval_variant where "Variant" =""" + """'""" + select_variant + """' OR "Variant" IN ('Variant_0','Variant_1000','Variant_340','Variant_76','Variant_89','Variant_897')"""
                df_query__1 = pd.read_sql(con = engine, sql = query__1)
                plot_avg_interval_varian = plx.bar(df_query__1, x = 'interval', y ='Variant')
                st.plotly_chart(plot_avg_interval_varian,use_container_width =True)
            with p2:
                query__2 = """
                SELECT 
                    "concept:name", 
                    count("interval") as count, 
                    MIN("interval") as min, 
                    MAX("interval") as max, 
                    AVG("interval") as mean, 
                    STDDEV("interval") as std, 
                    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY "interval") AS q1,
                    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY "interval") AS q3
                FROM 
                    billing.full_case_variant_time
                WHERE 
                    "Variant" = """ + """'""" + select_variant + """'""" + """ GROUP BY "concept:name" """
                df_query__2 = pd.read_sql(con = engine, sql = query__2).round(4)
                st.markdown("<br><br><br>",unsafe_allow_html =True)
                st.dataframe(df_query__2,use_container_width = True)
        if variant_activity_radio =='Activity':
            with p1:
                query___3 = """
                SELECT 
                    "concept:name", 
                    COUNT("interval") AS count ,
                    MIN("interval") AS min, 
                    MAX("interval") AS max, 
                    AVG("interval") as mean, 
                    STDDEV("interval") as std, 
                    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY "interval") AS q1, 
                    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY "interval") AS q3
                FROM billing.full_case_variant_time
                WHERE "concept:name" = """  + """'""" + select_activity + """'""" + """  GROUP BY "concept:name" """
                df_query__3 = pd.read_sql(sql = query___3,con=engine).drop('concept:name',axis=1).T
                df_query__3.columns = [str('interval ' + select_activity )]
                st.dataframe(df_query__3,use_container_width = True)
            with p2:
                st.markdown("<br><br>",unsafe_allow_html =True)
                with st.expander("Box plot"):
                    boxplot = plx.box(pd.read_sql(con = engine, sql = """ SELECT "interval" FROM billing.full_case_variant_time WHERE "concept:name" =  """ + """'"""+select_activity+"""';"""),x = 'interval')
                    st.plotly_chart(boxplot,use_container_width = True)
                st.markdown("<br>",unsafe_allow_html =True)
                with st.expander("Scatter plot"):
                    scatter = plx.scatter(pd.read_sql(con = engine, sql = """ SELECT "interval", "time:timestamp" FROM billing.full_case_variant_time WHERE "concept:name" =  """ + """'"""+select_activity+"""';"""),x = 'interval', y = 'time:timestamp')
                    st.plotly_chart(scatter,use_container_width = True)
                st.markdown("<br>",unsafe_allow_html =True)
                with st.expander("Line plot"):
                    query__4 = """ 
                    SELECT 
                        DATE("time:timestamp"), 
                        COUNT("interval") 
                    FROM 
                        billing.full_case_variant_time 
                    WHERE "concept:name" = '""" + select_activity + """'""" + """ GROUP BY DATE("time:timestamp") """
                    line = plx.area(pd.read_sql(con = engine, sql = query__4),x = 'date', y = 'count')
                    st.plotly_chart(line,use_container_width = True)
    st.markdown("<hr>",unsafe_allow_html =True)
    with st.container():
        with st.expander("Variant & Case Identifier"):
            r1,r2 = st.columns(2)
            with r1:
                title_centered_h3("Find Cases Per Variant")
                select_var = st.selectbox('Select Variant', df_variants['Variant_Name'],index = 196)
                q__5 = """ SELECT "Cases" FROM billing.variants_total_df WHERE "Variant_Name" = """ + """'""" + select_var + """'"""
                cent_text(str(pd.read_sql(con = engine, sql = q__5)['Cases'].to_list()[0]))
            with r2:
                title_centered_h3("Find Variant Per Case")
                select_cas = st.selectbox('Select case identify Variant', cases_df_list['case:concept:name'])
                q__7 = """ SELECT "Variant" FROM billing.full_case_variant_time WHERE "case:concept:name"  = '""" + select_cas + """'""" + """ LIMIT 1 """
                cent_text(str(pd.read_sql(con = engine, sql = q__7)['Variant'].to_list()[0]))                                                            
    st.markdown("<hr>",unsafe_allow_html =True)
    with st.container():
        title_centered_h1("Progress Analysis")
        global sel_slider
        sel_slider = st.slider(label="Slide Complexity", min_value=1, max_value=100, value=1,step = 15)


                                                            # # # ---------------- Timing - Level 1 ------------------------
                                                            # # # ---------------- Timing - Level 1 ------------------------ 

        if sel_slider == 1:
            with st.container():            
                l1,l2 = st.columns(2)
                with l1:
                    st.image('images/timing/DFG_1.png')
                with l2:
                    query_1_time = """                    
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Hour' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval"),
                            MAX("interval"),
                            AVG("interval")	
                        FROM billing.full_case_variant_time
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Days' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/24 AS min,
                            MAX("interval")/24 AS max,
                            AVG("interval")/24 AS avg	
                        FROM billing.full_case_variant_time
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Years' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/8760 AS min,
                            MAX("interval")/8760 AS max,
                            AVG("interval")/8760 AS avg	
                        FROM billing.full_case_variant_time
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant" """
                    df_header_time = pd.read_sql(con = engine, sql = query_1_time).round(3)
                    h1,h2,h3 = st.columns(3)
                    with h1:
                        title_centered_h3("Min")
                        selector_1 = st.selectbox("we",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_1]['min'].to_list()[0])
                    with h2:
                        title_centered_h3("Avg")
                        selector_2 = st.selectbox("we__",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_2]['avg'].to_list()[0])
                    with h3:
                        title_centered_h3("Max")
                        selector_3 = st.selectbox("w__e",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_3]['max'].to_list()[0])
                    st.markdown("<hr>",unsafe_allow_html = True)
                    
                    tuple_level_1 = tuple(df_variants_level_1['Variant_Name'].to_list())
                    if len(tuple_level_1) == 1:
                        tuple_level_1 = str(tuple(df_variants_level_1['Variant_Name'].to_list())).replace(",","")
                    else:
                        tuple_level_1 = str(tuple(df_variants_level_1['Variant_Name'].to_list()))
                    query_1_b = """
                    SELECT 
                        "concept:name",
                        MIN("interval") AS min,
                        MAX("interval") AS max,
                        AVG("interval") AS mean,
                        STDDEV("interval") AS std,
                        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY "interval") AS q1,
                        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY "interval") AS q3
                    FROM 
                        billing.full_case_variant_time 
                    WHERE "Variant" IN  """ + tuple_level_1 + """ GROUP BY "concept:name"  """
                    table_summary = pd.read_sql(con=engine , sql = query_1_b)
                    table_summary = table_summary.T
                    table_summary.columns = table_summary.loc["concept:name",:]
                    table_summary = table_summary.drop("concept:name",axis=0)
                    st.dataframe(table_summary)

                                                            # # # ---------------- Timing - Level 16 ------------------------
                                                            # # # ---------------- Timing - Level 16 ------------------------                     

                
        if sel_slider == 16:
            tuple_level_16 = tuple(df_variants_level_16['Variant_Name'].to_list())
            if len(tuple_level_16) == 1:
                tuple_level_16 = str(tuple(df_variants_level_16['Variant_Name'].to_list())).replace(",","")
            else:
                tuple_level_16 = str(tuple(df_variants_level_16['Variant_Name'].to_list()))
            with st.container():
                l1,l2 = st.columns(2)
                with l1:
                    st.image('images/timing/DFG_16.png')
                with l2:
                    query_1_time = """                    
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Hour' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval"),
                            MAX("interval"),
                            AVG("interval")	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ +  tuple_level_16 + """  
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Days' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/24 AS min,
                            MAX("interval")/24 AS max,
                            AVG("interval")/24 AS avg	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ + tuple_level_16 + """
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Years' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/8760 AS min,
                            MAX("interval")/8760 AS max,
                            AVG("interval")/8760 AS avg	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ + tuple_level_16 + """
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant" ; """
                    df_header_time = pd.read_sql(con = engine, sql = query_1_time).round(3)
                    h1,h2,h3 = st.columns(3)
                    with h1:
                        title_centered_h3("Min")
                        selector_1 = st.selectbox("weaa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_1]['min'].to_list()[0])
                    with h2:
                        title_centered_h3("Avg")
                        selector_2 = st.selectbox("we__aa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_2]['avg'].to_list()[0])
                    with h3:
                        title_centered_h3("Max")
                        selector_3 = st.selectbox("w__eaa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_3]['max'].to_list()[0])
                    st.markdown("<hr>",unsafe_allow_html = True)
                    query_16_b = """
                    SELECT 
                        "concept:name",
                        MIN("interval") AS min,
                        MAX("interval") AS max,
                        AVG("interval") AS mean,
                        STDDEV("interval") AS std,
                        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY "interval") AS q1,
                        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY "interval") AS q3
                    FROM 
                        billing.full_case_variant_time 
                    WHERE "Variant" IN  """ + tuple_level_16 + """ GROUP BY "concept:name"  """
                    table_summary = pd.read_sql(con=engine , sql = query_16_b)
                    table_summary = table_summary.T
                    table_summary.columns = table_summary.loc["concept:name",:]
                    table_summary = table_summary.drop("concept:name",axis=0)
                    st.dataframe(table_summary)         

                                                            # # # ---------------- Timing - Level 31 ------------------------
                                                            # # # ---------------- Timing - Level 31 ------------------------                     


        if sel_slider == 31:
            tuple_level_31 = tuple(df_variants_level_31['Variant_Name'].to_list())
            if len(tuple_level_31) == 1:
                tuple_level_31 = str(tuple(df_variants_level_31['Variant_Name'].to_list())).replace(",","")
            else:
                tuple_level_31 = str(tuple(df_variants_level_31['Variant_Name'].to_list()))
            with st.container():
                l1,l2 = st.columns(2)
                with l1:
                    st.image('images/timing/DFG_31.png')
                with l2:
                    query_1_time = """                    
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Hour' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval"),
                            MAX("interval"),
                            AVG("interval")	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ +  tuple_level_31 + """  
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Days' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/24 AS min,
                            MAX("interval")/24 AS max,
                            AVG("interval")/24 AS avg	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ + tuple_level_31 + """
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Years' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/8760 AS min,
                            MAX("interval")/8760 AS max,
                            AVG("interval")/8760 AS avg	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ + tuple_level_31 + """
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant" ; """
                    df_header_time = pd.read_sql(con = engine, sql = query_1_time).round(3)
                    h1,h2,h3 = st.columns(3)
                    with h1:
                        title_centered_h3("Min")
                        selector_1 = st.selectbox("weaa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_1]['min'].to_list()[0])
                    with h2:
                        title_centered_h3("Avg")
                        selector_2 = st.selectbox("we__aa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_2]['avg'].to_list()[0])
                    with h3:
                        title_centered_h3("Max")
                        selector_3 = st.selectbox("w__eaa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_3]['max'].to_list()[0])
                    st.markdown("<hr>",unsafe_allow_html = True)
                    query_31_b = """
                    SELECT 
                        "concept:name",
                        MIN("interval") AS min,
                        MAX("interval") AS max,
                        AVG("interval") AS mean,
                        STDDEV("interval") AS std,
                        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY "interval") AS q1,
                        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY "interval") AS q3
                    FROM 
                        billing.full_case_variant_time 
                    WHERE "Variant" IN  """ + tuple_level_31 + """ GROUP BY "concept:name"  """
                    table_summary = pd.read_sql(con=engine , sql = query_31_b)
                    table_summary = table_summary.T
                    table_summary.columns = table_summary.loc["concept:name",:]
                    table_summary = table_summary.drop("concept:name",axis=0)
                    st.dataframe(table_summary)

                                                            # # # ---------------- Timing - Level 46 ------------------------
                                                            # # # ---------------- Timing - Level 46 ------------------------                     

        if sel_slider == 46:
            tuple_level_46 = tuple(df_variants_level_46['Variant_Name'].to_list())
            if len(tuple_level_46) == 1:
                tuple_level_46 = str(tuple(df_variants_level_46['Variant_Name'].to_list())).replace(",","")
            else:
                tuple_level_46 = str(tuple(df_variants_level_46['Variant_Name'].to_list()))
            with st.container():
                l1,l2 = st.columns(2)
                with l1:
                    st.image('images/timing/DFG_46.png')
                with l2:
                    query_1_time = """                    
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Hour' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval"),
                            MAX("interval"),
                            AVG("interval")	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ +  tuple_level_46 + """  
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Days' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/24 AS min,
                            MAX("interval")/24 AS max,
                            AVG("interval")/24 AS avg	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ + tuple_level_46 + """
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Years' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/8760 AS min,
                            MAX("interval")/8760 AS max,
                            AVG("interval")/8760 AS avg	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ + tuple_level_46 + """
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant" ; """
                    df_header_time = pd.read_sql(con = engine, sql = query_1_time).round(3)
                    h1,h2,h3 = st.columns(3)
                    with h1:
                        title_centered_h3("Min")
                        selector_1 = st.selectbox("weaa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_1]['min'].to_list()[0])
                    with h2:
                        title_centered_h3("Avg")
                        selector_2 = st.selectbox("we__aa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_2]['avg'].to_list()[0])
                    with h3:
                        title_centered_h3("Max")
                        selector_3 = st.selectbox("w__eaa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_3]['max'].to_list()[0])
                    st.markdown("<hr>",unsafe_allow_html = True)
                    query_46_b = """
                    SELECT 
                        "concept:name",
                        MIN("interval") AS min,
                        MAX("interval") AS max,
                        AVG("interval") AS mean,
                        STDDEV("interval") AS std,
                        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY "interval") AS q1,
                        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY "interval") AS q3
                    FROM 
                        billing.full_case_variant_time 
                    WHERE "Variant" IN  """ + tuple_level_46 + """ GROUP BY "concept:name"  """
                    table_summary = pd.read_sql(con=engine , sql = query_46_b)
                    table_summary = table_summary.T
                    table_summary.columns = table_summary.loc["concept:name",:]
                    table_summary = table_summary.drop("concept:name",axis=0)
                    st.dataframe(table_summary)

                                                            # # # ---------------- Timing - Level 61 ------------------------
                                                            # # # ---------------- Timing - Level 61 ------------------------                     

        if sel_slider == 61:
            tuple_level_61 = tuple(df_variants_level_61['Variant_Name'].to_list())
            if len(tuple_level_61) == 1:
                tuple_level_61 = str(tuple(df_variants_level_61['Variant_Name'].to_list())).replace(",","")
            else:
                tuple_level_61 = str(tuple(df_variants_level_61['Variant_Name'].to_list()))
            with st.container():
                l1,l2 = st.columns(2)
                with l1:
                    st.image('images/timing/DFG_61.png')
                with l2:
                    query_1_time = """                    
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Hour' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval"),
                            MAX("interval"),
                            AVG("interval")	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ +  tuple_level_61 + """  
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Days' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/24 AS min,
                            MAX("interval")/24 AS max,
                            AVG("interval")/24 AS avg	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ + tuple_level_61 + """
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Years' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/8760 AS min,
                            MAX("interval")/8760 AS max,
                            AVG("interval")/8760 AS avg	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ + tuple_level_61 + """
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant" ; """
                    df_header_time = pd.read_sql(con = engine, sql = query_1_time).round(3)
                    h1,h2,h3 = st.columns(3)
                    with h1:
                        title_centered_h3("Min")
                        selector_1 = st.selectbox("weaa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_1]['min'].to_list()[0])
                    with h2:
                        title_centered_h3("Avg")
                        selector_2 = st.selectbox("we__aa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_2]['avg'].to_list()[0])
                    with h3:
                        title_centered_h3("Max")
                        selector_3 = st.selectbox("w__eaa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_3]['max'].to_list()[0])
                    st.markdown("<hr>",unsafe_allow_html = True)
                    query_61_b = """
                    SELECT 
                        "concept:name",
                        MIN("interval") AS min,
                        MAX("interval") AS max,
                        AVG("interval") AS mean,
                        STDDEV("interval") AS std,
                        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY "interval") AS q1,
                        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY "interval") AS q3
                    FROM 
                        billing.full_case_variant_time 
                    WHERE "Variant" IN  """ + tuple_level_61 + """ GROUP BY "concept:name"  """
                    table_summary = pd.read_sql(con=engine , sql = query_61_b)
                    table_summary = table_summary.T
                    table_summary.columns = table_summary.loc["concept:name",:]
                    table_summary = table_summary.drop("concept:name",axis=0)
                    st.dataframe(table_summary)

                                                            # # # ---------------- Timing - Level 76 ------------------------
                                                            # # # ---------------- Timing - Level 76 ------------------------                     

        if sel_slider == 76:
            tuple_level_76 = tuple(df_variants_level_76['Variant_Name'].to_list())
            if len(tuple_level_76) == 1:
                tuple_level_76 = str(tuple(df_variants_level_76['Variant_Name'].to_list())).replace(",","")
            else:
                tuple_level_76 = str(tuple(df_variants_level_76['Variant_Name'].to_list()))
            with st.container():
                l1,l2 = st.columns(2)
                with l1:
                    st.image('images/timing/DFG_76.png')
                with l2:
                    query_1_time = """                    
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Hour' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval"),
                            MAX("interval"),
                            AVG("interval")	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ +  tuple_level_76 + """  
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Days' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/24 AS min,
                            MAX("interval")/24 AS max,
                            AVG("interval")/24 AS avg	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ + tuple_level_76 + """
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Years' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/8760 AS min,
                            MAX("interval")/8760 AS max,
                            AVG("interval")/8760 AS avg	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ + tuple_level_76 + """
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant" ; """
                    df_header_time = pd.read_sql(con = engine, sql = query_1_time).round(3)
                    h1,h2,h3 = st.columns(3)
                    with h1:
                        title_centered_h3("Min")
                        selector_1 = st.selectbox("weaa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_1]['min'].to_list()[0])
                    with h2:
                        title_centered_h3("Avg")
                        selector_2 = st.selectbox("we__aa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_2]['avg'].to_list()[0])
                    with h3:
                        title_centered_h3("Max")
                        selector_3 = st.selectbox("w__eaa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_3]['max'].to_list()[0])
                    st.markdown("<hr>",unsafe_allow_html = True)
                    query_76_b = """
                    SELECT 
                        "concept:name",
                        MIN("interval") AS min,
                        MAX("interval") AS max,
                        AVG("interval") AS mean,
                        STDDEV("interval") AS std,
                        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY "interval") AS q1,
                        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY "interval") AS q3
                    FROM 
                        billing.full_case_variant_time 
                    WHERE "Variant" IN  """ + tuple_level_76 + """ GROUP BY "concept:name"  """
                    table_summary = pd.read_sql(con=engine , sql = query_76_b)
                    table_summary = table_summary.T
                    table_summary.columns = table_summary.loc["concept:name",:]
                    table_summary = table_summary.drop("concept:name",axis=0)
                    st.dataframe(table_summary)

                                                            # # # ---------------- Timing - Level 91 ------------------------
                                                            # # # ---------------- Timing - Level 91 ------------------------                     

        if sel_slider == 91:
            tuple_level_91 = tuple(df_variants_level_91['Variant_Name'].to_list())
            if len(tuple_level_91) == 1:
                tuple_level_91 = str(tuple(df_variants_level_91['Variant_Name'].to_list())).replace(",","")
            else:
                tuple_level_91 = str(tuple(df_variants_level_91['Variant_Name'].to_list()))
            with st.container():
                l1,l2 = st.columns(2)
                with l1:
                    st.image('images/timing/DFG_91.png')
                with l2:
                    query_1_time = """                    
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Hour' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval"),
                            MAX("interval"),
                            AVG("interval")	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ +  tuple_level_91 + """  
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Days' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/24 AS min,
                            MAX("interval")/24 AS max,
                            AVG("interval")/24 AS avg	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ + tuple_level_91 + """
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Years' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/8910 AS min,
                            MAX("interval")/8910 AS max,
                            AVG("interval")/8910 AS avg	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ + tuple_level_91 + """
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant" ; """
                    df_header_time = pd.read_sql(con = engine, sql = query_1_time).round(3)
                    h1,h2,h3 = st.columns(3)
                    with h1:
                        title_centered_h3("Min")
                        selector_1 = st.selectbox("weaa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_1]['min'].to_list()[0])
                    with h2:
                        title_centered_h3("Avg")
                        selector_2 = st.selectbox("we__aa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_2]['avg'].to_list()[0])
                    with h3:
                        title_centered_h3("Max")
                        selector_3 = st.selectbox("w__eaa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_3]['max'].to_list()[0])
                    st.markdown("<hr>",unsafe_allow_html = True)
                    query_91_b = """
                    SELECT 
                        "concept:name",
                        MIN("interval") AS min,
                        MAX("interval") AS max,
                        AVG("interval") AS mean,
                        STDDEV("interval") AS std,
                        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY "interval") AS q1,
                        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY "interval") AS q3
                    FROM 
                        billing.full_case_variant_time 
                    WHERE "Variant" IN  """ + tuple_level_91 + """ GROUP BY "concept:name"  """
                    table_summary = pd.read_sql(con=engine , sql = query_91_b)
                    table_summary = table_summary.T
                    table_summary.columns = table_summary.loc["concept:name",:]
                    table_summary = table_summary.drop("concept:name",axis=0)
                    st.dataframe(table_summary)

                                                            # # # ---------------- Timing - Level 100 ------------------------
                                                            # # # ---------------- Timing - Level 100 ------------------------                     

        if sel_slider >= 100:
            tuple_level_100 = tuple(df_variants_level_100['Variant_Name'].to_list())
            if len(tuple_level_100) == 1:
                tuple_level_100 = str(tuple(df_variants_level_100['Variant_Name'].to_list())).replace(",","")
            else:
                tuple_level_100 = str(tuple(df_variants_level_100['Variant_Name'].to_list()))
            with st.container():
                l1,l2 = st.columns(2)
                with l1:
                    st.image('images/timing/DFG_100.png')
                with l2:
                    query_1_time = """                    
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Hour' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval"),
                            MAX("interval"),
                            AVG("interval")	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ +  tuple_level_100 + """  
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Days' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/24 AS min,
                            MAX("interval")/24 AS max,
                            AVG("interval")/24 AS avg	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ + tuple_level_100 + """
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant"
                    UNION
                    SELECT  a1."Variant_Name", a2.min, a2.max,a2.avg,'Years' as Time  FROM billing.df_variants_level_1 a1
                    INNER JOIN ( 
                        SELECT "Variant",
                            MIN("interval")/81000 AS min,
                            MAX("interval")/81000 AS max,
                            AVG("interval")/81000 AS avg	
                        FROM billing.full_case_variant_time
                        WHERE "Variant" in """ + tuple_level_100 + """
                        GROUP BY "Variant") a2
                    on a1."Variant_Name" = a2."Variant" ; """
                    df_header_time = pd.read_sql(con = engine, sql = query_1_time).round(3)
                    h1,h2,h3 = st.columns(3)
                    with h1:
                        title_centered_h3("Min")
                        selector_1 = st.selectbox("weaa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_1]['min'].to_list()[0])
                    with h2:
                        title_centered_h3("Avg")
                        selector_2 = st.selectbox("we__aa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_2]['avg'].to_list()[0])
                    with h3:
                        title_centered_h3("Max")
                        selector_3 = st.selectbox("w__eaa",label_visibility= 'hidden', options = ['Hour','Days','Years'])
                        cent_text(df_header_time[df_header_time['time'] == selector_3]['max'].to_list()[0])
                    st.markdown("<hr>",unsafe_allow_html = True)
                    query_100_b = """
                    SELECT 
                        "concept:name",
                        MIN("interval") AS min,
                        MAX("interval") AS max,
                        AVG("interval") AS mean,
                        STDDEV("interval") AS std,
                        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY "interval") AS q1,
                        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY "interval") AS q3
                    FROM 
                        billing.full_case_variant_time 
                    WHERE "Variant" IN  """ + tuple_level_100 + """ GROUP BY "concept:name"  """
                    table_summary = pd.read_sql(con=engine , sql = query_100_b)
                    table_summary = table_summary.T
                    table_summary.columns = table_summary.loc["concept:name",:]
                    table_summary = table_summary.drop("concept:name",axis=0)
                    st.dataframe(table_summary)
    st.markdown("<hr>",unsafe_allow_html = True)
    with st.container():
        w1, w2 = st.columns([1,3])
        with w1:
            global df_plot_last
            __s1 = st.text_input("case 1",max_chars=4,value ='FGT')
            __s2 = st.text_input("case 2",max_chars=4,value ='OLD')
            __s3 = st.text_input("case 3",max_chars=4,value ='ZAZ')
            __s4 = st.text_input("case 4",max_chars=4,value ='P')
            __s5 = st.text_input("case 5",max_chars=4,value ='RLT')
            _in_query = str(tuple([__s1,__s2,__s3,__s4,__s5]))
            query__ = """ SELECT "time:timestamp","concept:name","case:concept:name"
                    FROM billiNG.full_case_variant_time
                    WHERE "case:concept:name" IN """ +  _in_query
            df_plot_last = pd.read_sql(con = engine, sql =query__)
        with w2:
            st.plotly_chart(plx.line(df_plot_last,x = 'concept:name', y = "time:timestamp", markers= True, color= "case:concept:name"),use_container_width = True)
        

# ---------------                #  Process Page   -------------------------------------------------------------------------------------------------------------- 
# ---------------                #  Process Page   -------------------------------------------------------------------------------------------------------------- 
# ---------------                #  Precess Page   -------------------------------------------------------------------------------------------------------------- 
# ---------------                #  Precess Page   --------------------------------------------------------------------------------------------------------------

if selectbox == 'Process':
    st.markdown("""<h1 style='text-align: center'>Process</h1>""",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    select_process_complexity = st.slider(label="Slide Complexity time", min_value=1, max_value=100, value=61,step = 15)


                                                            # # # ---------------- Process - Level 1 ------------------------
                                                            # # # ---------------- Process - Level 1 ------------------------
    
    if  select_process_complexity == 1:
        with st.container():
            t1,t2 = st.columns(2)
            with t1:
                title_centered_h3("Heurist Net")
                st.image('Images/heuristic_1.png',use_column_width=False)
            with t2:
                st.markdown("""<br><br><br>""",unsafe_allow_html=True)
                title_centered_h3("Starting Activities")
                st.dataframe(df_start_act_1,use_container_width  = True)
                title_centered_h3("End Activities")
                st.dataframe(transp_corr(df_end_act_1),use_container_width =True)
                st.markdown("""<h3 style='text-align:center'> Download Net </h3>""",unsafe_allow_html=True)
                st.download_button("Download Net",data = download_image('Images/heuristic_1.png'),mime="image/jpeg")
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            with st.expander('Additional Info'):
                title_centered_h3("% of ending Activities")
                plot_ends_1 = plx.bar(data_frame=df_end_act_1,y = 'Activity',x = 'Percentage')
                st.plotly_chart(plot_ends_1,use_container_width =True)
            title_centered_h3("Business Process Model")
            st.image('images/bpmn_1.png',use_column_width=True)
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Variants")
            y1,y2,y3 = st.columns([3,1,1])
            with y1:
                title_centered_h3("Select Variant")
                global selectbox_1
                selectbox_1 = st.selectbox(label = " - ", options = df_variants_level_1['Variant_Name'])
            with y2:
                global z
                title_centered_h3("Length of the Trace")
                z = df_variants_level_1.loc[(df_variants_level_1['Variant_Name'] == selectbox_1),'trace'].to_list()[0].split(",")
                z = [i.replace("(","") for i in z]
                z = [i.replace(")","") for i in z]
                st.info("Number of elements in the Trace: " + str(len(z) ))
                y = df_variants_level_1.loc[(df_variants_level_1['Variant_Name'] == selectbox_1),'percentage'].to_list()[0]
                st.info("Percentage of occurance of this trace: " + str(y))
            with y3:
                title_centered_h3("Elements of the trace")
                st.markdown(str(z))
            month_year_1 = st.radio(label ="select",label_visibility='hidden',options = ['Lenght of the Variant','Occurance of the Variant'],horizontal=True)
            if month_year_1 == 'Lenght of the Variant':
                len_variance_1 = plx.bar(df_variants_level_1,x = 'Variant_Name', y = 'len_trace' )
                st.plotly_chart(len_variance_1,use_container_width=True)
            else:
                ocurrance_1 = plx.bar(df_variants_level_1,x = 'Variant_Name', y = 'percentage')
                st.plotly_chart(ocurrance_1,use_container_width=True)
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Aditional Process Maps")
            u1,u2 = st.columns([7,1])
            with u1:
                st.image('images/net_inductive_1.png',use_column_width=True)
            with u2:
                st.download_button("Petri Net Inductive", data = download_image('images/net_inductive_1.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha", data = download_image('images/net_alpha_1.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha Plus", data = download_image('images/net_alphaplus_1.png'),mime= 'image/jpeg')
                
                                                            # # # ---------------- Process - Level 16 ------------------------
                                                            # # # ---------------- Process - Level 16 ------------------------

    if  select_process_complexity == 16:
        with st.container():
            a1,a2 = st.columns(2)
            with a1:
                title_centered_h3("Heurist Net")
                st.image('Images/heuristic_16.png',use_column_width=False)
            with a2:
                st.markdown("""<br><br><br>""",unsafe_allow_html=True)
                title_centered_h3("Starting Activities")
                st.dataframe(df_start_act_16,use_container_width  = True)
                title_centered_h3("End Activities")
                st.dataframe(transp_corr(df_end_act_16),use_container_width =True)
                st.markdown("""<h3 style='text-align:center'> Download Net </h3>""",unsafe_allow_html=True)
                st.download_button("Download Net",data = download_image('Images/heuristic_16.png'),mime="image/jpeg")
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            with st.expander('Additional Info'):
                title_centered_h3("% of ending Activities")
                plot_ends_16 = plx.bar(data_frame=df_end_act_16,y = 'Activity',x = 'Percentage')
                st.plotly_chart(plot_ends_16,use_container_width =True)
            title_centered_h3("Business Process Model")
            st.image('images/bpmn_16.png',use_column_width=True)        
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Variants")
            y1,y2,y3 = st.columns([3,1,1])
            with y1:
                title_centered_h3("Select Variant")
                global selectbox_16
                selectbox_16 = st.selectbox(label = " - ", options = df_variants_level_16['Variant_Name'])
            with y2:
                global z16
                title_centered_h3("Length of the Trace")
                z16 = df_variants_level_16.loc[(df_variants_level_16['Variant_Name'] == selectbox_16),'trace'].to_list()[0].split(",")
                z16 = [i.replace("(","") for i in z16]
                z16 = [i.replace(")","") for i in z16]
                st.info("Number of elements in the Trace: " + str(len(z16) ))
                y16 = df_variants_level_16.loc[(df_variants_level_16['Variant_Name'] == selectbox_16),'percentage'].to_list()[0]
                st.info("Percentage of occurance of this trace: " + str(y16))
            with y3:
                title_centered_h3("Elements of the trace")
                st.markdown(str(z16))
            month_year_16 = st.radio(label ="select",label_visibility='hidden',options = ['Lenght of the Variant','Occurance of the Variant'],horizontal=True)
            if month_year_16 == 'Lenght of the Variant':
                len_variance_16 = plx.bar(df_variants_level_16,x = 'Variant_Name', y = 'len_trace' )
                st.plotly_chart(len_variance_16,use_container_width=True)
            else:
                ocurrance_16 = plx.bar(df_variants_level_16,x = 'Variant_Name', y = 'percentage')
                st.plotly_chart(ocurrance_16,use_container_width=True)
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Aditional Process Maps")
            u1,u2 = st.columns([7,1])
            with u1:
                st.image('images/net_inductive_16.png',use_column_width=True)
            with u2:
                st.download_button("Petri Net Inductive", data = download_image('images/net_inductive_16.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha", data = download_image('images/net_alpha_16.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha Plus", data = download_image('images/net_alphaplus_16.png'),mime= 'image/jpeg')

                                                            # # # ---------------- Process - Level 31 ------------------------
                                                            # # # ---------------- Process - Level 31 ------------------------

    if  select_process_complexity == 31:
        with st.container():
            a1,a2 = st.columns(2)
            with a1:
                title_centered_h3("Heurist Net")
                st.image('Images/heuristic_31.png',use_column_width=False)
            with a2:
                st.markdown("""<br><br><br>""",unsafe_allow_html=True)
                title_centered_h3("Starting Activities")
                st.dataframe(df_start_act_31,use_container_width  = True)
                title_centered_h3("End Activities")
                st.dataframe(transp_corr(df_end_act_31),use_container_width =True)
                st.markdown("""<h3 style='text-align:center'> Download Net </h3>""",unsafe_allow_html=True)
                st.download_button("Download Net",data = download_image('Images/heuristic_31.png'),mime="image/jpeg")
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            with st.expander('Additional Info'):
                title_centered_h3("% of ending Activities")
                plot_ends_31 = plx.bar(data_frame=df_end_act_31,y = 'Activity',x = 'Percentage')
                st.plotly_chart(plot_ends_31,use_container_width =True)
            title_centered_h3("Business Process Model")
            st.image('images/bpmn_31.png',use_column_width=True)
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Variants")
            y1,y2,y3 = st.columns([3,1,1])
            with y1:
                title_centered_h3("Select Variant")
                global selectbox_31
                selectbox_31 = st.selectbox(label = " - ", options = df_variants_level_31['Variant_Name'])
            with y2:
                global z31
                title_centered_h3("Length of the Trace")
                z31 = df_variants_level_31.loc[(df_variants_level_31['Variant_Name'] == selectbox_31),'trace'].to_list()[0].split(",")
                z31 = [i.replace("(","") for i in z31]
                z31 = [i.replace(")","") for i in z31]
                st.info("Number of elements in the Trace: " + str(len(z31) ))
                y31 = df_variants_level_31.loc[(df_variants_level_31['Variant_Name'] == selectbox_31),'percentage'].to_list()[0]
                st.info("Percentage of occurance of this trace: " + str(y31))
            with y3:
                title_centered_h3("Elements of the trace")
                st.markdown(str(z31))
            month_year_31 = st.radio(label ="select",label_visibility='hidden',options = ['Lenght of the Variant','Occurance of the Variant'],horizontal=True)
            if month_year_31 == 'Lenght of the Variant':
                len_variance_31 = plx.bar(df_variants_level_31,x = 'Variant_Name', y = 'len_trace' )
                st.plotly_chart(len_variance_31,use_container_width=True)
            else:
                ocurrance_31 = plx.bar(df_variants_level_31,x = 'Variant_Name', y = 'percentage')
                st.plotly_chart(ocurrance_31,use_container_width=True)
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Aditional Process Maps")
            u1,u2 = st.columns([7,1])
            with u1:
                st.image('images/net_inductive_31.png',use_column_width=True)
            with u2:
                st.download_button("Petri Net Inductive", data = download_image('images/net_inductive_31.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha", data = download_image('images/net_alpha_31.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha Plus", data = download_image('images/net_alphaplus_31.png'),mime= 'image/jpeg')    

                                                            # # # ---------------- Process - Level 46 ------------------------
                                                            # # # ---------------- Process - Level 46 ------------------------

    if  select_process_complexity == 46:
        with st.container():
            a1,a2 = st.columns(2)
            with a1:
                title_centered_h3("Heurist Net")
                st.image('Images/heuristic_46.png',use_column_width=False)
            with a2:
                st.markdown("""<br><br><br>""",unsafe_allow_html=True)
                title_centered_h3("Starting Activities")
                st.dataframe(df_start_act_46,use_container_width  = True)
                title_centered_h3("End Activities")
                st.dataframe(transp_corr(df_end_act_46),use_container_width =True)
                st.markdown("""<h3 style='text-align:center'> Download Net </h3>""",unsafe_allow_html=True)
                st.download_button("Download Net",data = download_image('Images/heuristic_46.png'),mime="image/jpeg")
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            with st.expander('Additional Info'):
                title_centered_h3("% of ending Activities")
                plot_ends_46 = plx.bar(data_frame=df_end_act_46,y = 'Activity',x = 'Percentage')
                st.plotly_chart(plot_ends_46,use_container_width =True)
            title_centered_h3("Business Process Model")
            st.image('images/bpmn_46.png',use_column_width=True)
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Variants")
            y1,y2,y3 = st.columns([3,1,1])
            with y1:
                title_centered_h3("Select Variant")
                global selectbox_46
                selectbox_46 = st.selectbox(label = " - ", options = df_variants_level_46['Variant_Name'])
            with y2:
                global z46
                title_centered_h3("Length of the Trace")
                z46 = df_variants_level_46.loc[(df_variants_level_46['Variant_Name'] == selectbox_46),'trace'].to_list()[0].split(",")
                z46 = [i.replace("(","") for i in z46]
                z46 = [i.replace(")","") for i in z46]
                st.info("Number of elements in the Trace: " + str(len(z46) ))
                y46 = df_variants_level_46.loc[(df_variants_level_46['Variant_Name'] == selectbox_46),'percentage'].to_list()[0]
                st.info("Percentage of occurance of this trace: " + str(y46))
            with y3:
                title_centered_h3("Elements of the trace")
                st.markdown(str(z46))
            month_year_46 = st.radio(label ="select",label_visibility='hidden',options = ['Lenght of the Variant','Occurance of the Variant'],horizontal=True)
            if month_year_46 == 'Lenght of the Variant':
                len_variance_46 = plx.bar(df_variants_level_46,x = 'Variant_Name', y = 'len_trace' )
                st.plotly_chart(len_variance_46,use_container_width=True)
            else:
                ocurrance_46 = plx.bar(df_variants_level_46,x = 'Variant_Name', y = 'percentage')
                st.plotly_chart(ocurrance_46,use_container_width=True)
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Aditional Process Maps")
            u1,u2 = st.columns([7,1])
            with u1:
                st.image('images/net_inductive_46.png',use_column_width=True)
            with u2:
                st.download_button("Petri Net Inductive", data = download_image('images/net_inductive_46.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha", data = download_image('images/net_alpha_46.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha Plus", data = download_image('images/net_alphaplus_46.png'),mime= 'image/jpeg') 

                                                            # # # ---------------- Process - Level 61 ------------------------
                                                            # # # ---------------- Process - Level 61 ------------------------
    if  select_process_complexity == 61:
        with st.container():
            a1,a2 = st.columns(2)
            with a1:
                title_centered_h3("Heurist Net")
                st.image('Images/heuristic_61.png',use_column_width=True)
            with a2:
                st.markdown("""<br><br><br><br><br><br>""",unsafe_allow_html=True)
                title_centered_h3("Starting Activities")
                st.dataframe(df_start_act_61,use_container_width  = True)
                title_centered_h3("End Activities")
                st.dataframe(transp_corr(df_end_act_61),use_container_width =True)
                st.markdown("""<h3 style='text-align:center'> Download Net </h3>""",unsafe_allow_html=True)
                st.download_button("Download Net",data = download_image('Images/heuristic_61.png'),mime="image/jpeg")
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            with st.expander('Additional Info'):
                title_centered_h3("% of ending Activities")
                plot_ends_61 = plx.bar(data_frame=df_end_act_61,y = 'Activity',x = 'Percentage')
                st.plotly_chart(plot_ends_61,use_container_width =True)
            title_centered_h3("Business Process Model")
            st.image('images/bpmn_61.png',use_column_width=True)
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Variants")
            y1,y2,y3 = st.columns([3,1,1])
            with y1:
                title_centered_h3("Select Variant")
                global selectbox_61
                selectbox_61 = st.selectbox(label = " - ", options = df_variants_level_61['Variant_Name'])
            with y2:
                global z61
                title_centered_h3("Length of the Trace")
                z61 = df_variants_level_61.loc[(df_variants_level_61['Variant_Name'] == selectbox_61),'trace'].to_list()[0].split(",")
                z61 = [i.replace("(","") for i in z61]
                z61 = [i.replace(")","") for i in z61]
                st.info("Number of elements in the Trace: " + str(len(z61) ))
                y61 = df_variants_level_61.loc[(df_variants_level_61['Variant_Name'] == selectbox_61),'percentage'].to_list()[0]
                st.info("Percentage of occurance of this trace:: " + str(y61))
            with y3:
                title_centered_h3("Elements of the trace")
                st.markdown(str(z61))
            month_year_61 = st.radio(label ="select",label_visibility='hidden',options = ['Lenght of the Variant','Occurance of the Variant'],horizontal=True)
            if month_year_61 == 'Lenght of the Variant':
                len_variance_61 = plx.bar(df_variants_level_61,x = 'Variant_Name', y = 'len_trace' )
                st.plotly_chart(len_variance_61,use_container_width=True)
            else:
                ocurrance_61 = plx.bar(df_variants_level_61,x = 'Variant_Name', y = 'percentage')
                st.plotly_chart(ocurrance_61,use_container_width=True)
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Aditional Process Maps")
            u1,u2 = st.columns([7,1])
            with u1:
                st.image('images/net_inductive_61.png',use_column_width=True)
            with u2:
                st.download_button("Petri Net Inductive", data = download_image('images/net_inductive_61.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha", data = download_image('images/net_alpha_61.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha Plus", data = download_image('images/net_alphaplus_61.png'),mime= 'image/jpeg') 

                                                            # # # ---------------- Process - Level 76 ------------------------
                                                            # # # ---------------- Process - Level 76 ------------------------

    if  select_process_complexity == 76:
        with st.container():
            a1,a2 = st.columns(2)
            with a1:
                title_centered_h3("Heurist Net")
                st.image('Images/heuristic_76.png',use_column_width=True)
            with a2:
                st.markdown("""<br><br><br><br><br><br>""",unsafe_allow_html=True)
                title_centered_h3("Starting Activities")
                st.dataframe(df_start_act_76,use_container_width  = True)
                title_centered_h3("End Activities")
                st.dataframe(transp_corr(df_end_act_76),use_container_width =True)
                st.markdown("""<h3 style='text-align:center'> Download Net </h3>""",unsafe_allow_html=True)
                st.download_button("Download Net",data = download_image('Images/heuristic_76.png'),mime="image/jpeg")
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            with st.expander('Additional Info'):
                title_centered_h3("% of ending Activities")
                plot_ends_76 = plx.bar(data_frame=df_end_act_76,y = 'Activity',x = 'Percentage')
                st.plotly_chart(plot_ends_76,use_container_width =True)
            title_centered_h3("Business Process Model")
            st.image('images/bpmn_76.png',use_column_width=True)
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Variants")
            y1,y2,y3 = st.columns([3,1,1])
            with y1:
                title_centered_h3("Select Variant")
                global selectbox_76
                selectbox_76 = st.selectbox(label = " - ", options = df_variants_level_76['Variant_Name'])
            with y2:
                global z76
                title_centered_h3("Length of the Trace")
                z76 = df_variants_level_76.loc[(df_variants_level_76['Variant_Name'] == selectbox_76),'trace'].to_list()[0].split(",")
                z76 = [i.replace("(","") for i in z76]
                z76 = [i.replace(")","") for i in z76]
                st.info("Number of elements in the Trace: " + str(len(z76) ))
                y76 = df_variants_level_76.loc[(df_variants_level_76['Variant_Name'] == selectbox_76),'percentage'].to_list()[0]
                st.info("Percentage of occurance of this trace:: " + str(y76))
            with y3:
                title_centered_h3("Elements of the trace")
                st.markdown(str(z76))
            month_year_76 = st.radio(label ="select",label_visibility='hidden',options = ['Lenght of the Variant','Occurance of the Variant'],horizontal=True)
            if month_year_76 == 'Lenght of the Variant':
                len_variance_76 = plx.bar(df_variants_level_76,x = 'Variant_Name', y = 'len_trace' )
                st.plotly_chart(len_variance_76,use_container_width=True)
            else:
                ocurrance_76 = plx.bar(df_variants_level_76,x = 'Variant_Name', y = 'percentage')
                st.plotly_chart(ocurrance_76,use_container_width=True)
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Aditional Process Maps")
            u1,u2 = st.columns([7,1])
            with u1:
                st.image('images/net_inductive_76.png',use_column_width=True)
            with u2:
                st.download_button("Petri Net Inductive", data = download_image('images/net_inductive_76.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha", data = download_image('images/net_alpha_76.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha Plus", data = download_image('images/net_alphaplus_76.png'),mime= 'image/jpeg')

                                                            # # # ---------------- Process - Level 91 ------------------------
                                                            # # # ---------------- Process - Level 91 ------------------------
    if  select_process_complexity == 91:
        with st.container():
            a1,a2 = st.columns(2)
            with a1:
                title_centered_h3("Heurist Net")
                st.image('Images/heuristic_91.png',use_column_width=True)
            with a2:
                st.markdown("""<br><br><br><br><br><br>""",unsafe_allow_html=True)
                title_centered_h3("Starting Activities")
                st.dataframe(df_start_act_91,use_container_width  = True)
                title_centered_h3("End Activities")
                st.dataframe(transp_corr(df_end_act_91),use_container_width =True)
                st.markdown("""<h3 style='text-align:center'> Download Net </h3>""",unsafe_allow_html=True)
                st.download_button("Download Net",data = download_image('Images/heuristic_91.png'),mime="image/jpeg")
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            with st.expander('Additional Info'):
                title_centered_h3("% of ending Activities")
                plot_ends_91 = plx.bar(data_frame=df_end_act_91,y = 'Activity',x = 'Percentage')
                st.plotly_chart(plot_ends_91,use_container_width =True)
            title_centered_h3("Business Process Model")
            st.image('images/bpmn_91.png',use_column_width=True)
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Variants")
            y1,y2,y3 = st.columns([3,1,1])
            with y1:
                title_centered_h3("Select Variant")
                global selectbox_91
                selectbox_91 = st.selectbox(label = " - ", options = df_variants_level_91['Variant_Name'])
            with y2:
                global z91
                title_centered_h3("Length of the Trace")
                z91 = df_variants_level_91.loc[(df_variants_level_91['Variant_Name'] == selectbox_91),'trace'].to_list()[0].split(",")
                z91 = [i.replace("(","") for i in z91]
                z91 = [i.replace(")","") for i in z91]
                st.info("Number of elements in the Trace: " + str(len(z91) ))
                y91 = df_variants_level_91.loc[(df_variants_level_91['Variant_Name'] == selectbox_91),'percentage'].to_list()[0]
                st.info("Percentage of occurance of this trace:: " + str(y91))
            with y3:
                title_centered_h3("Elements of the trace")
                st.markdown(str(z91))
            month_year_91 = st.radio(label ="select",label_visibility='hidden',options = ['Lenght of the Variant','Occurance of the Variant'],horizontal=True)
            if month_year_91 == 'Lenght of the Variant':
                len_variance_91 = plx.bar(df_variants_level_91,x = 'Variant_Name', y = 'len_trace' )
                st.plotly_chart(len_variance_91,use_container_width=True)
            else:
                ocurrance_91 = plx.bar(df_variants_level_91,x = 'Variant_Name', y = 'percentage')
                st.plotly_chart(ocurrance_91,use_container_width=True)
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Aditional Process Maps")
            u1,u2 = st.columns([7,1])
            with u1:
                st.image('images/net_inductive_91.png',use_column_width=True)
            with u2:
                st.download_button("Petri Net Inductive", data = download_image('images/net_inductive_91.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha", data = download_image('images/net_alpha_91.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha Plus", data = download_image('images/net_alphaplus_91.png'),mime= 'image/jpeg')

                                                            # # # ---------------- Process - Level 100 ------------------------
                                                            # # # ---------------- Process - Level 100 ------------------------

    if  select_process_complexity >= 100:
        with st.container():
            a1,a2 = st.columns(2)
            with a1:
                title_centered_h3("Heurist Net")
                st.image('Images/heuristic_100.png',use_column_width=True)
            with a2:
                st.markdown("""<br><br><br><br><br><br>""",unsafe_allow_html=True)
                title_centered_h3("Starting Activities")
                st.dataframe(df_start_act_100,use_container_width  = True)
                title_centered_h3("End Activities")
                st.dataframe(transp_corr(df_end_act_100),use_container_width =True)
                st.markdown("""<h3 style='text-align:center'> Download Net </h3>""",unsafe_allow_html=True)
                st.download_button("Download Net",data = download_image('Images/heuristic_100.png'),mime="image/jpeg")
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            with st.expander('Additional Info'):
                title_centered_h3("% of ending Activities")
                plot_ends_100 = plx.bar(data_frame=df_end_act_100,y = 'Activity',x = 'Percentage')
                st.plotly_chart(plot_ends_100,use_container_width =True)
            title_centered_h3("Business Process Model")
            st.image('images/bpmn_100.png',use_column_width=True)
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Variants")
            y1,y2,y3 = st.columns([3,1,1])
            with y1:
                title_centered_h3("Select Variant")
                global selectbox_100
                selectbox_100 = st.selectbox(label = " - ", options = df_variants_level_100['Variant_Name'])
            with y2:
                global z100
                title_centered_h3("Length of the Trace")
                z100 = df_variants_level_100.loc[(df_variants_level_100['Variant_Name'] == selectbox_100),'trace'].to_list()[0].split(",")
                z100 = [i.replace("(","") for i in z100]
                z100 = [i.replace(")","") for i in z100]
                st.info("Number of elements in the Trace: " + str(len(z100) ))
                y100 = df_variants_level_100.loc[(df_variants_level_100['Variant_Name'] == selectbox_100),'percentage'].to_list()[0]
                st.info("Percentage of occurance of this trace:: " + str(y100))
            with y3:
                title_centered_h3("Elements of the trace")
                st.markdown(str(z100))
            month_year_100 = st.radio(label ="select",label_visibility='hidden',options = ['Lenght of the Variant','Occurance of the Variant'],horizontal=True)
            if month_year_100 == 'Lenght of the Variant':
                len_variance_100 = plx.bar(df_variants_level_100,x = 'Variant_Name', y = 'len_trace' )
                st.plotly_chart(len_variance_100,use_container_width=True)
            else:
                ocurrance_100 = plx.bar(df_variants_level_100,x = 'Variant_Name', y = 'percentage')
                st.plotly_chart(ocurrance_100,use_container_width=True)
        st.markdown("<hr>",unsafe_allow_html=True)
        with st.container():
            title_centered_h3("Aditional Process Maps")
            u1,u2 = st.columns([7,1])
            with u1:
                st.image('images/net_inductive_100.png',use_column_width=True)
            with u2:
                st.download_button("Petri Net Inductive", data = download_image('images/net_inductive_100.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha", data = download_image('images/net_alpha_100.png'),mime= 'image/jpeg')
                st.download_button("Petri Net Alpha Plus", data = download_image('images/net_alphaplus_100.png'),mime= 'image/jpeg')

# ---------------                #  Data Page   -------------------------------------------------------------------------------------------------------------- 
# ---------------                #  Data Page   -------------------------------------------------------------------------------------------------------------- 
# ---------------                #  Data Page   -------------------------------------------------------------------------------------------------------------- 
# ---------------                #  Data Page   --------------------------------------------------------------------------------------------------------------


if selectbox == 'Data':
    with st.container():
        title_centered_h1("Data")
        cent_text(""" Take a look at a sample of the Data, click the link below the table to download the file.
        This file is not human readable, please have a .XES.gz file reader if you want to explore for yourslef of use python  + pm4py """)        
        sample = pd.read_csv('dataframes/sample_df.csv')
        st.dataframe(sample,use_container_width = True)
        st.markdown(""" <a href = "https://data.4tu.nl/ndownloader/files/24058772" Download > Download XES Data """, unsafe_allow_html = True)
        st.markdown("<hr>", unsafe_allow_html = True)
        g1, g2 = st.columns(2)
        with g1:
            title_centered_h3("Description")
            cent_text(""" 
            The 'Hospital Billing' event log was obtained from the financial modules of the
                ERP system of a regional hospital. The event log contains events that are 
                related to the billing of medical services that have been provided by the 
                hospital. Each trace of the event log records the activities executed to bill 
                a package of medical services that were bundled together. The event log does 
                not contain information about the actual medical services provided by the 
                hospital. The 100,000 traces in the event log are a random sample of process instances 
                that were recorded over three years. Several attributes such as the 'state' of
                the process, the 'caseType', the underlying 'diagnosis' etc. are included in 
                the event log. Events and attribute values have been anonymized. The time 
                stamps of events have been randomized for this purpose, but the time between
                events within a trace has not been altered. More information about the event log can be found in the related publications.Please cite as:
                Mannhardt, F (Felix) (2017) Hospital Billing - Event Log. 
                Eindhoven University of Technology. Dataset. 
                https://doi.org/10.4121/uuid:76c46b83-c930-4798-a1c9-4be94dfeb741            
            """)
        with g2:
            title_centered_h3("Attributes")
            st.dataframe(pd.read_csv("dataframes/dataframes\Dataset Atrbutes.csv"))
 












