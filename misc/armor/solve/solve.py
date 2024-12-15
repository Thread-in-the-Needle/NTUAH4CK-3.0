import main
import pdb

print(dir(main)) # see whats going on


print(main.first) # first part



pdb.set_trace()
pdb.run('main.second("test")')
pdb.run('main.third("test")')
pdb.run('main.fourth("test")')
'''
press c to continue once
s to step into a few times
then locals() to see the variables
    or 
globals()['__pdb_convenience_variables']['_frame'].f_code.co_consts
'''
