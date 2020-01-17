# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/17 10:08:17 by mli               #+#    #+#              #
#    Updated: 2020/01/17 10:41:30 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Evaluator:

    @staticmethod
    def zip_evaluate(coefs, words):
        if (len(coefs) != len(words)):
            return (-1)
        res = 0
        try:
            for word, nb in zip(words, coefs):
                res += len(str(word)) * float(nb)
        except ValueError:
            return (-1)
        return (res)

    def enumerate_evaluate(coefs, words):
        if (len(coefs) != len(words)):
            return (-1)
        res = 0
        try:
            for i, word in enumerate(words):
                res += len(str(word)) * float(coefs[i])
        except ValueError:
            return (-1)
        return (res)

#words = ["Le", "Lorem", "Ipsum", "est", "simple"]
#coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

#words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
#coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]

#print(Evaluator.enumerate_evaluate(coefs, words))
#print(Evaluator.zip_evaluate(coefs, words))
