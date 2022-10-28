import pm4py as pm
import pandas as pd
import numpy as np

class variants:
    def __init__(self, eventlog):
        self.eventlog = eventlog

    def get_variants_df(eventlog):
        trace = []
        elements_trace = []
        trace_l = pm.get_variants_as_tuples(eventlog)
        for trace_, info in trace_l.items():
            trace.append(trace_)
            elements_trace.append(info)
        cases_len = []
        for i in elements_trace:
            cases_len.append(len(i))
        r = []
        for list_ in elements_trace:
            cases_outer = []
            for value in list_:
                internal_cases = []
                for internal_dict in value:
                    cases_list = []
                    for key_,value_ in dict(internal_dict).items():
                        if key_ == 'case:concept:name':
                            cases_list.append(value_)
                    for case_ in cases_list:
                        internal_cases.append(case_)
                for internal_case in internal_cases:
                    cases_outer.append(internal_case)
            cases_outer = pd.Series(cases_outer)
            cases_outer = cases_outer.unique().tolist()
            r.append(cases_outer)

                
        df_variants = pd.DataFrame({
            'trace': trace,
            'info': elements_trace,
            'len':cases_len,
            'Cases':r
        })

        df_variants['percentage'] = df_variants['len'] / df_variants['len'].sum()* 100
        df_variants= df_variants.sort_values('percentage',ascending=False)
        variant_name = ['Variant_'+str(i) for i in np.arange(len(df_variants))]
        df_variants['Variant_Name'] = variant_name

        return df_variants