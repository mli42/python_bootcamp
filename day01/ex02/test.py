# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2021/11/28 15:05:08 by mli               #+#    #+#              #
#    Updated: 2021/11/28 17:08:58 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from vector import Vector

def print_sep():
    print("---------------------------------------------------------------")

def print_test(has, expected: str) -> None:
    txt = repr(has) if isinstance(has, Vector) else str(has)
    print(txt, f"\nExpect: {expected}")
    print_sep()

def test_one():
    print("# Column vector of shape n * 1")
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print_test(v1 * 5, "Vector([[0.0], [5.0], [10.0], [15.0]])")

    print("# Row vector of shape 1 * n")
    v1 = Vector([0.0, 1.0, 2.0, 3.0])
    v2 = v1 * 5
    print_test(v2, "Vector([0.0, 5.0, 10.0, 15.0])")
    print_test(v1 / 2.0, "Vector([[0.0], [0.5], [1.0], [1.5]])")

    try:
        print(2.0 / v1)
    except ValueError as e:
        print(e)
    finally:
        print("Expect: ValueError('A scalar cannot be divided by a Vector.')")
        print_sep()

def test_two():
    print("# Column vector of shape n * 1")
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print_test(v1.shape, "(4,1)")
    print_test(v1.values, "[[0.0], [1.0], [2.0], [3.0]]")

    print("# Row vector of shape 1 * n")
    v2 = Vector([0.0, 1.0, 2.0, 3.0])
    print_test(v2.shape, "(1, 4)")
    print_test(v2.values, "[0.0, 1.0, 2.0, 3.0]")

def test_three():
    print_test(Vector([0.0, 1.0, 2.0, 3.0]), "[0.0, 1.0, 2.0, 3.0]")
    print_test(Vector([[0.0], [1.0], [2.0], [3.0]]), "[[0.0], [1.0], [2.0], [3.0]]")
    print_test(Vector(3), "[[0.0], [1.0], [2.0]]")
    print_test(Vector(range(10, 15)), "[[10.0], [11.0], [12.0], [13.0], [14.0]]")

if __name__ == "__main__":
    # test_one()
    print_sep()
    test_two()
    print_sep()
    test_three()
    print_sep()
