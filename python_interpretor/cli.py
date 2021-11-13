#!/usr/bin/python3
import itertools
'''
# this collects the user input infinitely until the user stops
we will use itertools module which has iterator functions
we will use with.count which increments infinitely
'''
def get_user_input(): # generator function; a func with yield statement in it
    for i in itertools.count():
        try:
            yield i, input('In [%d]: ' %i)
            ''' 
                i in this case is a counter variable, input collects this and returns as a string
                saved in i. Yield works to return the  value without ending the function
                 unlike return statements would end immediately
             '''
        except KeyboardInterrupt:
            pass
        except EOFError:
            break

def exec_function(user_input): # higherlevel func because it returns a func
    '''
    if user_input == an expression return eval, else: return exec
    to sort this we use a compile func which creates a byte code of python code
    '''
    try:
        compile(user_input, '<stdin>', 'eval')
    except SyntaxError:
        return exec
    return eval

def exec_user_input(i, user_input, user_globals):
    '''
    # executing user_input using the user_globals dict
    exec works only when input is statement
    eval works for value/ expressions only
    to solve this we are going to develop a higher function(a func that returns a function)
    that will take a user input and return either eval or exec depending on the user input
    '''
    try: # used for exception that arise from entering an invalid value
         retval = exec_function(user_input)(
             user_input, user_globals
         )
    except Exception as e:
        # e is an exception object
        # exception has dunder class property referring to the class(ie name error class)
        # class will have a dunder name property rep. the name of the class as a string
        print('%s: %s' %(e.__class__.__name__, e))
    else:
         # we use retval to allow the return value(output) to printed on the screen
        if retval is not None:
            print('Out [%d]: %s' %(i, retval))

def selected_user_globals(user_globals): # this func works only to display the user globals in txt file
    # using generator expression
    return(
        (key, user_globals[key])
        for key in sorted(user_globals)
        if not key.startswith('__') or not key.endswith('__')
    )
def save_user_globals(user_globals, path='user_globals.txt'):# path guides the function where to save the variables
    # open file
    with open(path, 'w') as fd:
        for key, value in selected_user_globals(user_globals):
            fd.write('%s = %s (%s)\n' % (key, value, value.__class__.__name__))

def main():
    # globals dict to store the variables
    user_globals = {}
    # to monitor the contents of user global
    save_user_globals(user_globals)
    # looping through what get user func yields
    for i, user_input in get_user_input():
        exec_user_input(i, user_input, user_globals)
        save_user_globals(user_globals)



if __name__ == '__main__':
    main()