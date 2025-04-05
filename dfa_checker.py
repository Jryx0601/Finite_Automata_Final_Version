#regex (1+0)(1+0)*(11+00)(11+00)*(1+0)(0+1)(11*00*) ((00)*+(11)*)(11+00)(11+00)*(1+0)*
dfa_binary = {
    'q0':{1:'q1',0:'q1'},
    'q1':{1:'q3',0:'q2'},
    'q2':{1:'q3',0:'q4'},
    'q3':{1:'q4',0:'q2'},
    'q4':{0:'q5',1:'q6'},
    'q5':{0:'q7',1:'q8'},
    'q6':{0:'q9',1:'q10'},
    'q7':{0:'q5',1:'q12'},
    'q8':{0:'q2',1:'q12'},
    'q9':{0:'q2',1:'q12'},
    'q10':{0:'q11',1:'q12'},
    'q11':{0:'q10',1:'q12'},
    'q12':{1:'q12',0:'q13'},
    'q13':{0:'q15',1:'q14'},
    'q14':{0:'q2',1:'q16'},
    'q15':{1:'q14',0:'q16'},
    'q16':{1:'q16',0:'q16'}
}

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
def valid_ornot(final_outcome,types):
    if types == 'binary':
        if final_outcome == 'q16':
            return 'Accepted'
        else:
            return 'Rejected'
    elif types == 'letter':
        if final_outcome == 'q21':
            return 'Accepted'
        else:
            return 'Rejected'
    



def dfa_checker(string,types):
    global states
    current_state = 'q0'
    if types == 'binary':
        for x in string:
            current_state= dfa_binary[current_state][int(x)]
        results = valid_ornot(current_state,types)
        states = []
        return results
    
    elif types == 'letter':
        for x in string:
            current_state= dfa_letter[current_state][x]
        results = valid_ornot(current_state,types)
        states = []
        return results