import torch
import torch.nn as nn
import numpy as np
import curses

VISUAL_CHAR = (',', '*', '#', '@')
SIZE_MAP = (8, 8)
reward_count = 3
obstacle_count = 4
def Main(stdscr):
	curses.curs_set(0)
	stdscr.clear()

	def Map_Gen(SIZE_MAP, reward_count):
		matrix = np.zeros(SIZE_MAP, dtype=int)
		for i in range(reward_count):
			while True:
				x, y = np.random.randint(0, SIZE_MAP[0]),np.random.randint(0, SIZE_MAP[1])
				if matrix[x,y] == 0:
					matrix[x, y] = 1
					break

		for i in range(obstacle_count):
			while True:
				x, y = np.random.randint(0, SIZE_MAP[0]),np.random.randint(0, SIZE_MAP[1])
				if matrix[x,y] == 0:
					matrix[x, y] = 2
					break
		while True:
			x, y = np.random.randint(0, SIZE_MAP[0]),np.random.randint(0, SIZE_MAP[1])
			if matrix[x,y] == 0:
				hero = (x,y)
				break
		return matrix, hero

	def Visual(matrix, hero):
		matrix[hero[0],hero[1]] = 3
		for y, row in enumerate(matrix):
			for x, cell in enumerate(row):
				stdscr.addstr(y, x, VISUAL_CHAR[cell])
		stdscr.refresh()
		stdscr.getch()

	matrix, hero = Map_Gen(SIZE_MAP, reward_count)
	Visual(matrix, hero)

curses.wrapper(Main)
