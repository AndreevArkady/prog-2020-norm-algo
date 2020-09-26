import argparse


def argparser():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument("--input", action="store", dest="input_file")
    my_parser.add_argument("--output", action="store", dest="output_file")
    return my_parser.parse_args()


args = argparser()

fin = open(args.input_file, 'r')

loop_list = []
left_part_of_MS = []  # MS = Markov substitution
right_part_of_MS = []
subst_is_final = []

n = fin.readline()
n = int(n)
for i in range(n):  # reading input data
    new_subst = str(fin.readline())
    if new_subst.count("-.") > 0:
        new_subst_parts = new_subst.split("-.")
        subst_is_final.append(1)
    else:
        new_subst_parts = new_subst.split("-")
        subst_is_final.append(0)
    left_part_of_MS.append(new_subst_parts[0])
    new_subst_parts[1] = new_subst_parts[1][:-1]
    right_part_of_MS.append(new_subst_parts[1])
input_word = fin.read()
fin.close()
loop_list.append(input_word)
algo_finished = False
not_looped = True
while (not algo_finished) & not_looped:  # searching for first applicable Markov's substitution
    for j in range(n):
        if input_word.count(left_part_of_MS[j]) > 0:  # if MS applicable
            input_word = input_word.replace(left_part_of_MS[j], right_part_of_MS[j], 1)
            if loop_list.count(input_word) > 0:
                not_looped = False
            loop_list.append(input_word)
            if subst_is_final[j] == 1:
                algo_finished = True
            break
        if j == n - 1:
            algo_finished = True
            break
if algo_finished:  # result of the algorithm
    with open(args.output_file, 'w') as fout:
        fout.write(input_word)
else:
    print("Infinite loop, your algorithm cannot be applied to the given word")

'''if __name__ == '__main__':
    args = argparser()
'''