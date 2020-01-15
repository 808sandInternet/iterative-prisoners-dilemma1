







team_name = 'Kool Kidz Klub' # Only 10 chars displayed.
strategy_name = 'Collusion'
strategy_description = '#aintnosnitch'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    if len(my_history)==0:
        return 'c'
    elif my_history[-1] == 'c' and their_history[-1] == 'b': 
        return 'b'
    else:
        return 'b'