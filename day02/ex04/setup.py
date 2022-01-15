# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    setup.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mli <mli@student.42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/11/22 17:24:47 by mli               #+#    #+#              #
#    Updated: 2022/01/15 14:32:31 by mli              ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='my_minipack',
    version="1.0.0",
    author='mli',
    author_email='mli@student.42.fr',
    description="How to create a package in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="None",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    license="GPLv3",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Students",
        "Topic :: Education",
        "Topic :: HowTo",
        "Topic :: Package",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires='>=3.7',
)
