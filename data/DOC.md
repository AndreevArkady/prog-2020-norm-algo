to execute the programm type in command line:
   "py <file_path> --input=<input_filename> --output=<output_filename>"
for instance:
    "py C:\Users\Maxim\PycharmProjects\prog-2020-norm-algo\norm_algo.py
      --input=input.txt --output=output.txt"


input_file data format:

        "n" - where n integer positive
    
    then in each of following n lines type:
        "X_i-.Y_i"
      or
        "X_i-Y_i" 
    where X and Y are words, use X-.Y for final substitutions
                                 X-Y  for non-final substitutions
    
    then type the input word, which will be affected by Markovs Algorithm
        "word"