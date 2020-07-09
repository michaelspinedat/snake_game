#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 22:04:46 2020

@author: michael
"""

import pygame, sys, time, random
from pygame.locals import *

pygame.init()
width, height = 500, 500

screen = pygame.display.set_mode((height, width))
fps = pygame.time.Clock()

def food_spawn(snakeD):
    food_pos = [random.randint(0, 49)*snakeD, random.randint(0, 49)*snakeD]
    return food_pos

def main():
    run = True
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    snakeD = 10    
    direction = 'R'
    change = direction
    food_pos = food_spawn(snakeD)
    score = 0
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:                    
                    change = 'R'
                if event.key == pygame.K_LEFT:
                    change = 'L'
                if event.key == pygame.K_UP:
                    change = 'U'
                if event.key == pygame.K_DOWN:
                    change = 'D'
                    
        if change == 'R' and direction != 'L':
            direction = change
        if change == 'L' and direction != 'R':
            direction = change
        if change == 'U' and direction != 'D':
            direction = change
        if change == 'D' and direction != 'U':
            direction = change
            
        if direction == 'R':
            snake_pos[0] += snakeD
        if direction == 'L':
            snake_pos[0] -= snakeD
        if direction == 'U':
            snake_pos[1] -= snakeD
        if direction == 'D':
            snake_pos[1] += snakeD
        
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            food_pos = food_spawn(snakeD)
            score += 1
        else:        
            snake_body.pop()
                
        screen.fill((0, 0, 0))
        
        for pos in snake_body:
            pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(pos[0], pos[1], snakeD, snakeD))
        pygame.draw.rect(screen, (255, 160, 60), pygame.Rect(food_pos[0], food_pos[1], snakeD, snakeD))
        
        if snake_pos[0] <= 0 or snake_pos[0] >= width:
            print(f"Game Over! Score: {score}")
            run = False
            
        if snake_pos[1] <= 0 or snake_pos[1] >= height:
            print(f"Game Over! Score: {score}")
            run = False    
            
        if snake_pos in snake_body[1:]:
            print(f"Game Over! Score: {score}")
            run = False 
            
        
        pygame.display.flip()
        fps.tick(10)
        
main()
pygame.quit()        