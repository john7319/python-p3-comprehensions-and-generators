#!/usr/bin/env python3

def return_evens(num_list):
    x = []
    for i in num_list:
        if i %2 == 0:
            x.append(i)
    return x

def make_exclamation(sentence_list):
    sentence = []
    for i in sentence_list:
        sentence.append(i+"!")
    return sentence

