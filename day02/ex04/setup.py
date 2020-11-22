# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    setup.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/22 17:24:47 by mli               #+#    #+#              #
#    Updated: 2020/11/22 18:19:41 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ai42',
    version="1.0.0",
    author='mli',
    author_email='mli@student.42.fr',
    description="A small example package for 42AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mli42/python_bootcamp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
