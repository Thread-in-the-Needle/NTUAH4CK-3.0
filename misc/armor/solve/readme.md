# Solution
- A simple `import main` and then `dir(main)` will show you the global variables and functions in the main module.
- We can see that there is a `check` function, a `first` variable and `second`, `third` and `fourth` functions.
- `print(main.first)` will give you the first part.
- For the second and third parts, we can `import pdb` and then `pdb.run('main.second("foo")')`. Pressing `c` and `s` will make you reach the execution of each function. Stepping a few more times and printing `locals()` will give you the 2 next parts.
- For the last part, we can reach the execution of the `fourth` function as previously and then print `globals()['__pdb_convenience_variables']['_frame'].f_code.co_consts` to get the last part. It is a list of decimal values that we can convert to ASCII and then Base64 decode to get the flag.