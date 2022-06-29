import streamlit as st
from analisis import analize_dataset,analize_single_query

if __name__ == '__main__':
   
    st.title('Dataset Analyzer')
    
    st.sidebar.header("Select Actions")
    
    cran = 'cranfield'
    vasw = 'vaswani'

    selected_options = st.sidebar.multiselect('Select the dataset', (
     cran,
     vasw
    ),    )

    query = st.sidebar.text_input('Input query',"query")
    output = ""
    if query == "query":
        for ds in selected_options:
            results = analize_dataset(ds)
            output += results
            output += "\n"

        out = output.split('\n')
        for _st in out:    
            st.write(_st)
    else:
        output = ""
        for ds in selected_options:
            _result = analize_single_query(ds,query)
            output+= _result +"\n"
            
        out = output.split('\n')
        for _st in out:    
            st.write(_st)
            
        
    
    
    
    
    
    
    
    
    
    
    

    

    
