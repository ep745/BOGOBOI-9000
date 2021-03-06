#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
COMS W4701 Artificial Intelligence - Programming Homework 2

An AI player for Othello. This is the template file that you need to  
complete and submit. 

@author: YOUR NAME AND UNI 
"""

import random
import sys
import time
import math

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move

def compute_utility(board, color):
    score=get_score(board)
    if color==1:
      return score[0]-score[1]
    elif color==2:
      return score[1]-score[0]
    else:
      return 0

def isCorner(a,b):
  if a == 0 or a == 7:
    if b == 0 or b == 7:
      return True
  return False

############ MINIMAX ###############################

def minimax_min_node(board, color, counter):
  if counter>=12:
    return compute_utility(board,color)
  moves=get_possible_moves(board,color)
  worstMoveScore = math.inf
  if len(moves) == 1:
    x = moves[0][0]
    y = moves[0][1]
    newBoard = play_move(board, color, x, y)
    return(compute_utility(newBoard,color))
  else:
    for i in moves:
      newBoard = play_move(board, color, i[0], i[1])
      counter+=1
      score = minimax_max_node(newBoard,color, counter)
      if score < worstMoveScore:
        worstMoveScore = score
    return worstMoveScore
    
def minimax_max_node(board, color, counter):
  if counter>=11:
    return compute_utility(board,color)
  moves=get_possible_moves(board,color)
  bestMoveScore = -math.inf
  if len(moves) == 1:
    x=moves[0][0]
    y=moves[0][1]
    newBoard=play_move(board, color, x, y)
    return(compute_utility(newBoard,color))
  else:
    for i in moves:
      newBoard=play_move(board,color,i[0],i[1])
      counter+=1
      score=minimax_min_node(newBoard,color,counter)
      if score>bestMoveScore:
        bestMoveScore=score
    return bestMoveScore
  


def select_move_minimax(board, color):
  """
  Given a board and a player color, decide on a move. 
  The return value is a tuple of integers (i,j), where
  i is the column and j is the row on the board.  
  """
    
  moves = get_possible_moves(board, color)
  bestMoveScore = -math.inf
  bestMove = moves[0]
  for i in moves:
    x=i[0]
    y=i[1]
    if isCorner(x,y)==True:
      return i
    else:
     newBoard = play_move(board, color, i[0], i[1])
     score = minimax_min_node(newBoard,color,1)
     if score>bestMoveScore:
        bestMoveScore=score
        bestMove=i
    return bestMove
    
############ ALPHA-BETA PRUNING #####################

#alphabeta_min_node(board, color, alpha, beta, level, limit)
def alphabeta_min_node(board, color, alpha, beta): 
    return None


#alphabeta_max_node(board, color, alpha, beta, level, limit)
def alphabeta_max_node(board, color, alpha, beta):
    return None


def select_move_alphabeta(board, color): 
    return 0,0 


####################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("BOGOBOI 9000") # First line is the name of this AI  
    color = int(input()) # Then we read the color: 1 for dark (goes first), 
                         # 2 for light. 

    while True: # This is the main loop 
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over. 
            print 
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)
                    
            # Select the move and send it to the manager 
            movei, movej = select_move_minimax(board, color)
            #movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__":
    run_ai()
