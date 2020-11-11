# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 16:15:10 by mli               #+#    #+#              #
#    Updated: 2020/11/11 20:58:49 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def text_analyzer(entry: str = None) -> None:
	'''This function counts the number of upper characters, lower characters,
	punctuation and spaces in a given text.'''

	ulps = [0, 0, 0, 0]
	if entry is None:
		entry = ""
		for line in sys.stdin:
			entry += line.rstrip('\n')
	for char in entry:
		if char.isupper():
			ulps[0] += 1
		elif char.islower():
			ulps[1] += 1
		elif char in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
			ulps[2] += 1
		elif char.isspace():
			ulps[3] += 1
	print("The text contains %d characters:" %len(entry))
	print("- %d upper letters" %ulps[0])
	print("- %d lower letters" % ulps[1])
	print("- %d punctuation marks" %ulps[2])
	print("- %d spaces" %ulps[3])

"""
text_analyzer("Python 2.0, released 2000, introduced features \
like List comprehensions and a garbage collection system capable of \
collecting reference cycles.")
"""
