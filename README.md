# Advent of Code 2020

## Introduction

> Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like.

Follow to [adventofcode.com](https://adventofcode.com/) for details. 

## My experience

The challenge for me is to try each year a different language. And use only the standard library.
This helps me to understand the language in itself. Having that in mind, 
my concern is to create the properly maintainable code, which is nice to read and hopefully learn from it. 

My choices so far were Java in [2019](https://github.com/shpikat/advent-of-code-2019). 
It was actually my first attempt of joining the fascinating world of Advent of Code.
And Java was my main workforce at that moment--seemed straightforwardly logical.
Unfortunately haven't finished that year yet.

This year`s choice was Python.
As I understood after solving part of 2019, the challenge is mainly about the algorithms.
Python proved that somewhat right: the solutions are quite easy to express most of the time.
But with the complexity of the problem growing the code becomes massively complicated.

That brought me to Golang in [2021](https://github.com/shpikat/advent-of-code-2021), see repositories for more details.

## Solutions

[![Check all solutions](https://github.com/shpikat/advent-of-code-2020/actions/workflows/check-solutions.yml/badge.svg)](https://github.com/shpikat/advent-of-code-2020/actions/workflows/check-solutions.yml)

The solutions are organized by days. As long as both parts are usually related, 
they share one Python file: `solution.py`.
The sample test cases and the actual puzzle answer can be found in `test_solution.py` test file.

All the tests can be run with one command. Each test has its own execution time stopwatch.
```shell
python -m unittest -v
```
