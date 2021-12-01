# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/17 10:08:17 by mli               #+#    #+#              #
#    Updated: 2021/12/01 23:26:14 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def evaluate_guard(coefs, words) -> bool:
    if not all([isinstance(obj, list) for obj in [coefs, words]]):
        return False
    if len(coefs) != len(words):
        return False
    if not all([isinstance(obj, str) for obj in words]):
        return False
    if not all([isinstance(obj, (int, float)) for obj in coefs]):
        return False
    return True

class Evaluator:

    @staticmethod
    def zip_evaluate(coefs, words):
        if not evaluate_guard(coefs, words):
            return (-1)
        res = 0
        for word, nb in zip(words, coefs):
            res += len(word) * nb
        return (res)

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if not evaluate_guard(coefs, words):
            return (-1)
        res = 0
        for i, word in enumerate(words):
            res += len(word) * coefs[i]
        return (res)

if __name__ == "__main__":
    def test_evaluate(coefs, words):
        print(f"Test for {coefs}/{words}:")
        print(Evaluator.enumerate_evaluate(coefs, words))
        print(Evaluator.zip_evaluate(coefs, words))
        print()

    test_evaluate([1.0, 2.0, 1.0, 4.0, 0.5], ["Le", "Lorem", "Ipsum", "est", "simple"])
    test_evaluate([0.0, -1.0, 1.0, -12.0, 0.0, 42.42], ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"])
    test_evaluate([1, 2, 3], ["word", 2, "wordo"])
