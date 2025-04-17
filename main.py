import streamlit as st
import graphviz
from graphviz import Digraph
from dfa_checker import dfa_checker
import time
st.set_page_config(layout="wide")
# DFA definition
dfa_binary = {
    'q0': {1: 'q1', 0: 'q1'},
    'q1': {1: 'q3', 0: 'q2'},
    'q2': {1: 'q3', 0: 'q4'},
    'q3': {1: 'q4', 0: 'q2'},
    'q4': {0: 'q5', 1: 'q6'},
    'q5': {0: 'q7', 1: 'q8'},
    'q6': {0: 'q9', 1: 'q10'},
    'q7': {0: 'q5', 1: 'q12'},
    'q8': {0: 'q2', 1: 'q12'},
    'q9': {0: 'q2', 1: 'q12'},
    'q10': {0: 'q11', 1: 'q12'},
    'q11': {0: 'q10', 1: 'q12'},
    'q12': {1: 'q12', 0: 'q13'},
    'q13': {0: 'q15', 1: 'q14'},
    'q14': {0: 'q2', 1: 'q16'},
    'q15': {1: 'q14', 0: 'q16'},
    'q16': {1: 'q16', 0: 'q16'}
}
#------------------------------------------------------------------------------------------------------
st.text('Regex: (1+0)(1+0)*(11+00)(11+00)*(1+0)(0+1)(11*00*) ((00)*+(11)*)(11+00)(11+00)*(1+0)*')
input_string = st.text_input('Enter a string: (Ex. 101010...)')
#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
dot = Digraph()
place_holder = st.empty()
for state, transitions in dfa_binary.items():
    dot.node(state)
    
    for symbol,next_state in transitions.items():
        dot.edge(state,next_state,label = str(symbol))
dot.attr(rankdir ='LR')
place_holder.graphviz_chart(dot)

col1, col2, col3,col4 = st.columns([1,1,1,1])
with col1:
    simulate = st.button('Simulate Binary')
    if simulate:
        current_position = 'q0'
        dot.node('q0',color = 'red',stye='solid',fillcolor = 'transparent')
        place_holder.graphviz_chart(dot)
        time.sleep(1)
        for x in input_string:
            dot.node('q0',color = 'black',stye='solid',fillcolor = 'transparent')
            current_position = dfa_binary[current_position][int(x)]
            if current_position != 'q16':
                temp = current_position
                dot.node(current_position,color='red',stye='solid',fillcolor = 'transparent')
                place_holder.graphviz_chart(dot)
                dot.node(temp,color = 'black',stye='solid',fillcolor = 'transparent')
            elif current_position == 'q16':
                dot.node(current_position,color = 'green',style = 'filled')
                place_holder.graphviz_chart(dot)
                break
            time.sleep(1)

with col2:
    check = st.button('Check Binary')
    if check:
        results = dfa_checker(input_string,'binary')
        st.text(f"Result:{results}")
with col3:
    with st.popover('CFG'):
        st.text('S -> ABCDAAEH')
        st.text('   A -> 1|0')
        st.text('   B -> 1B|0B|e')
        st.text('   C -> 11|00')
        st.text('   D -> 11D|00D|e')
        st.text('   E -> 1F0G')
        st.text('   F -> 1F|e')
        st.text('   G -> 0G|e')
        st.text('   H -> 11B|00B')
with col4:
    with st.popover('PDA'):
        pass

st.divider()
#-------------------------------------------------------------------------
dfa_letter = {
    'q0':{'a':'q1','b':'q2'},
    'q1':{'a':'q3','b':'T'},
    'q2':{'b':'q3','a':'T'},
    'q3':{'a':'q4','b':'q5'},
    'q4':{'a':'q7','b':'q6'},
    'q5':{'a':'q9','b':'q8'},
    'q6':{'a':'q10','b':'q8'},
    'q7':{'a':'q10','b':'q6'},
    'q8':{'a':'q9','b':'q10'},
    'q9':{'a':'q7','b':'q10'},
    'q10':{'a':'q11','b':'q12'},
    'q11':{'a':'q13','b':'q10'},
    'q12':{'a':'q10','b':'q13'},
    'q13':{'a':'q13','b':'q14'},
    'q14':{'a':'q14','b':'q15'},
    'q15':{'a':'q16','b':'q17'},
    'q16':{'a':'q16','b':'q18'},
    'q17':{'a':'q20','b':'q19'},
    'q18':{'a':'q21','b':'q19'},
    'q19':{'a':'q21','b':'q21'},
    'q20':{'a':'q16','b':'q21'},
    'q21':{'a':'q21','b':'q21'},
    'T':{'a':'T','b':'T'}
}
#------------------------------------------------------------------------------------------------------

st.text('Regex: (aa+bb)(a+b)*(aba+bab+bbb+aaa)(ab+ba)*(bb+aa)(a+b)*(a*ba*ba*)(bab+bba+bbb+aba)(a+b)*')
input_letter = st.text_input('Enter a string: (Ex. ababab)')
#------------------------------------------------------------------------------------------------------

place_holder_letter = st.empty()
dot_letter = Digraph()
for state,transition in dfa_letter.items():
    dot_letter.node(state)
    for symbol, next_state in transition.items():
        dot_letter.edge(state,next_state,label=str(symbol))
dot_letter.attr(rankdir = 'LR')

place_holder_letter.graphviz_chart(dot_letter)

col1_letter,col2_letter,col3_letter,col4_letter = st.columns([1,1,1,1])

with col1_letter:
    simulate_letter = st.button('Simulate Letter')
    if simulate_letter:
        current_position = 'q0'
        dot_letter.node(current_position,color = 'red',stye='solid',fillcolor = 'transparent')
        place_holder_letter.graphviz_chart(dot_letter)
        time.sleep(1)
        for x in input_letter:
            dot_letter.node(current_position,color = 'black',stye='solid',fillcolor = 'transparent')
            current_position = dfa_letter[current_position][x]
            if current_position != 'q21':
                temp = current_position
                dot_letter.node(current_position,color='red',stye='solid',fillcolor = 'transparent')
                place_holder_letter.graphviz_chart(dot_letter)
                dot_letter.node(temp,color = 'black',stye='solid',fillcolor = 'transparent')
                if current_position == 'T':
                    dot_letter.node('T',color = 'red',style = 'filled')
                    place_holder_letter.graphviz_chart(dot_letter)
                    break
            elif current_position == 'q21':
                dot_letter.node(current_position,color = 'green',style = 'filled')
                place_holder_letter.graphviz_chart(dot_letter)
                break
            time.sleep(1)
with col2_letter:
    valir_onot = st.button('Check Letter')
    if valir_onot:
        results_binary = dfa_checker(input_letter,'letter')
        st.text(f'Result: {results_binary}')

with col3_letter:
    with st.popover('CFG'):
        pass
with col4_letter:
    with st.popover('PDA'):
        pass



