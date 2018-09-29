#### COPIED ####  VERIFIED
"""
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
If there is more than one possible reconstruction, return any of them.
If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""


# print one reconstruction, and return True, if re-constrictible
def _print_recon(ret_list, dictionary, sentence, index, memo):
    if len(sentence) == index:  # Dont forget
        return True

    # here we are finding only one result. so in memo, we will never store True.
    # we return True immediately.
    if memo[index] != -1:
        return memo[index]

    # go through the sentence
    for i in range(index, len(sentence)):
        if sentence[index:i + 1] in dictionary:  # a word is found in dict
            ret_list.append(sentence[index:i+1])
            if _print_recon(ret_list, dictionary, sentence, i+1, memo):
                return True

            ret_list.pop()  # no possible findings. pop out last word

    memo[index] = False
    return False


# print all reconstruction
def _print_all_recon(ret_list, results, dictionary, sentence, index, memo):
    if len(sentence) == index:  # Dont forget
        return True

    if memo[index] != -1:
        return memo[index]

    flag = False # keep a flag to update memo
    for i in range(index, len(sentence)):  # go through the sentence
        if sentence[index:i+1] in dictionary:
            ret_list.append(sentence[index:i+1])
            if _print_all_recon(ret_list, results, dictionary, sentence, i+1, memo):
                flag = True
                word = ret_list[-1]
                results[index].append(word)
            ret_list.pop()

    memo[index] = flag
    return flag


def print_words(result, index, ret_list):
    if index >= len(result):
        print(ret_list)
        return

    res_list = result[index]
    for i in res_list:
        ret_list.append(i)
        print_words(result, index+len(i), ret_list)
        ret_list.pop()


def print_result(result):
    ret_list = [] # a ret_list is needed because, for same initial word, there could be multiple combinations
    print_words(result, 0, ret_list)



def print_recon(dictionary, sentence):
    ret_list = []
    # since we have to find only one solution, we keep memo simplified
    # memo will be False if the rest of the 'sentence' cannot form words
    memo = [-1] * len(sentence)
    # result = [[]]*len(sentence)
    result = [list() for _ in range(len(sentence))]
    _print_all_recon(ret_list, result, dictionary, sentence, 0, memo)

    print_result(result)
    print('----------------')
    ret_list = []
    memo = [-1] * len(sentence)
    if _print_recon(ret_list, dictionary, sentence, 0, memo):
        print(ret_list)
    print(memo)


if __name__ == '__main__':
    sentence = 'atabedbatandbeyondlane'
    dictionary = {'bed', 'bat', 'bedba', 'bedb', 'ata', 'bey' ,'ndb', 'bedbate', 'bedbat', 'and', 'beyond', 'dl', 'lane'}
    dictionary = { "mobile", "samsung", "sam", "sung", "man", "mango", "icecream", "and", "go", "i", "like", "ice", "cream" }
    sentence = 'ilikemangoandicecreamandsamsung'
    print_recon(dictionary, sentence)
