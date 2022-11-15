def solution(s):
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    word_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = ''
    for num, word in zip(num_list, word_list):
        s = s.replace(word, str(num)) 
    return int(s)