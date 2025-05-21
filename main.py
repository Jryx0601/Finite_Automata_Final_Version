import streamlit as st
import graphviz
from graphviz import Digraph
from dfa_checker import dfa_checker
import time
from PIL import Image
from streamlit_pdf_reader import pdf_reader
import base64
from streamlit_extras.switch_page_button import switch_page
import pathlib
st.set_page_config(layout="wide",initial_sidebar_state='collapsed')

tab1, tab2,tab3,tab4 = st.tabs(['Regex 1','Regex 2','Members','User Manual'])
with tab1:
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
    st.header('Regex: (1+0)(1+0)\\*(11+00)(11+00)\\*(1+0)(0+1)(11\\*00\\*) ((00)\\*+(11)\\*)(11+00)(11+00)\\*(1+0)\\*')
    input_string1 = st.text_input('Enter a string number:')
    st.warning('Note: \n\n- Always end each input with a comma (,).\n\n- Example Input: (111111011,111111011,)\n\n - Valid Input Example: \n\n   - 111101000\n\n   - 1111111011', icon="⚠️")
    img = Image.open('PDA.drawio.png')

    col1,col3,col4 = st.columns([1,1,1])
    with col1:
        simulate = st.button('Simulate Binary')
    with col3:
        with st.popover('Context Free Grammar'):
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
        modal = st.button('Push Down Automata Binary')
        if modal:
            switch_page('PDA1')
            # st.switch_page('pages/PDA1.py')
#------------------------------------------------------------------------------------------------------
    dot = Digraph()
    place_holder = st.empty()
    for state, transitions in dfa_binary.items():
        dot.node(state)
    
        for symbol,next_state in transitions.items():
            dot.edge(state,next_state,label = str(symbol))
    dot.attr(rankdir ='LR')
    dot.node('q16',style = 'solid',color = 'green',penwidth = '3')
    place_holder.graphviz_chart(dot)
#------------------------------------------------------------------------------------------------------
    output = ""
#For Clearing the outputs
    clear_button = st.button('Clear Binary Button')
    if clear_button:
        output = ""
#------------------------------------------------------------------------------------------------------
    container = st.container()
    with container:
        placehold_printing = st.empty()
        if simulate:
            if input_string1[-1] != ",":
                st.error('No "," at the end.', icon="🚨")
            else:
                current_position = 'q0'
                dot.node('q0',color = 'red',stye='filled',fillcolor = 'firebrick1',penwidth = '3')
                place_holder.graphviz_chart(dot)
                time.sleep(1)
                for binary in input_string1:
                    if binary != ",":
                        dot.node('q0',color = 'black',stye='filled',fillcolor = 'transparent',penwidth = '1')
                        current_position = dfa_binary[current_position][int(binary)]
                        if current_position != 'q16':
                            temp = current_position
                            dot.node(current_position,color = 'red',stye='filled',fillcolor = 'firebrick1',penwidth = '3')
                            output += f'{binary} '
                            placehold_printing.markdown(output.strip())
                            place_holder.graphviz_chart(dot)
                            dot.node(temp,color = 'black',stye='filled',fillcolor = 'transparent',penwidth = '1')
                        elif current_position == 'q16':
                            dot.node(current_position,color = 'green',style = 'filled',fillcolor = 'darkolivegreen1',penwidth = '3')
                            temp = current_position
                            output += f"{binary} "
                            placehold_printing.markdown(output.strip())
                            place_holder.graphviz_chart(dot)
                            time.sleep(1)
                            continue
                        time.sleep(1)          
                    elif binary == ",":
                        if temp != 'q16':
                            output += " = Invalid \n\n"
                            placehold_printing.markdown(output.strip())
                            time.sleep(1)
                        else:
                            output += " = Valid \n\n"
                            
                            placehold_printing.markdown(output.strip())
                            time.sleep(1)
                        dot.node('q16',color = 'green',stye='filled', fillcolor = 'white',pendwith = '3')
                        place_holder.graphviz_chart(dot)
                        current_position = 'q0'
                        dot.node('q0',color = 'red',stye='filled',fillcolor = 'firebrick1',penwidth = '3')
                        place_holder.graphviz_chart(dot)
                        time.sleep(1)
                        continue
                dot.node('q0',color = 'black',stye='filled',fillcolor = 'transparent',penwidth = '1')
                place_holder.graphviz_chart(dot)
                time.sleep(1)
with tab2:
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
    st.header('Regex: (aa+bb)(a+b)\\*(aba+bab+bbb+aaa)(ab+ba)\\*(bb+aa)(a+b)\\*(a\\*ba\\*ba\\*)(bab+bba+bbb+aba)(a+b)\\*')
    input_letter = st.text_input('Enter a string letter:')
    st.warning('Note: \n\n- Always end each input with a comma (,).\n\n- Example Input: (aaaaaaaaaa,aaaaaaaaaa,)\n\n- Valid Input Examples: \n\n    - aaababbbbbaba,\n\n   - bbbababaabbbaba,', icon="⚠️")
    img2 = Image.open('PDA2_Regex.png')
    col1_letter,col3_letter,col4_letter = st.columns([1,1,1])
    with col1_letter:
        simulate_letter = st.button('Simulate Letter')
    with col3_letter:
        with st.popover('Context Free Grammar'):
            st.text('S -> ACDEFGHLM')
            st.text('A -> aa|bb')
            st.text('C -> aC|bC|e')
            st.text('D -> aba|bab|bbb|aaa')
            st.text('E -> abE|baE|e')
            st.text('F -> bb|aa')
            st.text('G -> aG|bG|e')
            st.text('H -> IbIbI')
            st.text('I -> aI|e')
            st.text('L -> bab|bba|bbb|aba')
            st.text('M -> aM|bM|e')
    with col4_letter:
        if st.button('Push Down Automata Letter'):
            switch_page('PDA2')
            # st.switch_page('pages/PDA2.py')
    #------------------------------------------------------------------------------------------------------
    place_holder_letter = st.empty()
    dot_letter = Digraph()
    for state,transition in dfa_letter.items():
        dot_letter.node(state)
        for symbol, next_state in transition.items():
            dot_letter.edge(state,next_state,label=str(symbol))
    dot_letter.attr(rankdir = 'LR')
    dot_letter.node('q21',style = 'solid',color = 'green',penwidth = '3')
    place_holder_letter.graphviz_chart(dot_letter)
    #------------------------------------------------------------------------------------------------------
    output_letter = ""
    #For Clearing the outputs
    clear_button_letter = st.button('Clear Letter Button')
    if clear_button_letter:
        output_letter = ""
    #------------------------------------------------------------------------------------------------------
    container_letter = st.container()
    with container_letter:
        placehold_printing_letter = st.empty()
        if simulate_letter:
            if input_letter[-1] != ",":
                st.error('No "," at the end.', icon="🚨")
            else:
                current_position = 'q0'
                dot_letter.node('q0',color = 'red',stye='filled',fillcolor = 'firebrick1',penwidth = '3')
                place_holder_letter.graphviz_chart(dot_letter)
                time.sleep(1)
                for letter in input_letter:
                    if letter != ",":
                        dot_letter.node('q0',color = 'black',stye='filled',fillcolor = 'transparent',penwidth = '1')
                        current_position = dfa_letter[current_position][letter]
                        if current_position != 'q21':
                            temp = current_position
                            dot_letter.node(current_position,color = 'red',stye='filled',fillcolor = 'firebrick1',penwidth = '3')
                            output_letter += f'{letter} '
                            placehold_printing_letter.markdown(output_letter.strip())
                            place_holder_letter.graphviz_chart(dot_letter)
                            dot_letter.node(temp,color = 'black',stye='filled',fillcolor = 'transparent',penwidth = '1')
                        elif current_position == 'T':
                            dot_letter.node(current_position,color = 'red',stye='filled',fillcolor = 'firebrick1',penwidth = '3')
                            output_letter += f'{letter} '
                            placehold_printing_letter.markdown(output_letter.strip())
                            place_holder_letter.graphviz_chart(dot_letter)
                            time.sleep(1)
                            continue
                        elif current_position == 'q21':
                            dot_letter.node(current_position,color = 'green',style = 'filled',fillcolor = 'darkolivegreen1',penwidth = '3')
                            temp = current_position

                            output_letter += f"{letter} "
                            placehold_printing_letter.markdown(output_letter.strip())
                            place_holder_letter.graphviz_chart(dot_letter)
                            time.sleep(1)
                            continue
                        time.sleep(1)
                    elif letter == ",":
                        if temp != 'q21' or temp == 'T':
                            output_letter += " = Invalid \n\n"
                            placehold_printing_letter.markdown(output_letter.strip())
                            time.sleep(1)
                        else:
                            output_letter += " = Valid \n\n"
                            placehold_printing_letter.markdown(output_letter.strip())
                            time.sleep(1)
                        dot_letter.node('q21',color = 'green',stye='filled', fillcolor = 'white',pendwith = '3')
                        place_holder_letter.graphviz_chart(dot_letter)
                        time.sleep(1)
                        current_position = 'q0'
                        dot_letter.node('q0',color = 'red',stye='filled',fillcolor = 'firebrick1',penwidth = '3')
                        place_holder_letter.graphviz_chart(dot_letter)
                        time.sleep(1)
                        continue
                dot_letter.node('q0',color = 'black',stye='filled',fillcolor = 'transparent',penwidth = '1')
                place_holder_letter.graphviz_chart(dot_letter)
                time.sleep(1)
with tab3:
    st.header('GROUP 2 Members:')
    st.write('- Balan, Joseph Anton')
    st.write('- Caling, Zandro Alvaro')
    st.write('- Llamera, Josh Mickel')
    st.write('- Matel, Francis Ellison S.')

with tab4:
    file_path = 'Module_6-Week_15-16_Privacy_and_Civil_Liberty_BCS34.pdf'
    pdf_reader(file_path)
#-------------------------------------------------------------------------




