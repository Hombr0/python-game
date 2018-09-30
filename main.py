import pygame
from pygame.locals import *
import sys
import os
import random
width = 1100
hight = 700
square1 = [240, 65] 
square2 = [25, 65]
square3 = [25, 285]
square4 = [240, 285]
coords1 = [805, 35]
coords2 = [525, 35]
coords3 = [530, 295]
coords4 = [810, 295]
coords5 = [30, 540]
coords6 = [244, 540]
coords7 = [458, 540]
coords8 = [672, 540]
coords9 = [886, 540]
text1 = [160, 600]
text2 = [374, 600]
text3 = [588, 600]
text4 = [802, 600]
text5 = [1016, 600]

pygame.init()
screen = pygame.display.set_mode((width, hight))
pygame.display.set_caption('Hidden Boys')
class Person(pygame.sprite.Sprite):
  def __init__(self, image_file, location):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(image_file)
    self.rect = self.image.get_rect()
    self.rect.left, self.rect.top = location

class Puzzle_piece(pygame.sprite.Sprite):
  def __init__(self, image_file, location):
    pygame.sprite.Sprite.__init__(self)
    self.counter = 0
    self.image = pygame.image.load(image_file)
    self.rect = self.image.get_rect()
    self.rect.left, self.rect.top = location
    self.state = "still"
    self.angle = 0
    self.square = ""
    self.pos = "up"
    self.solution = False

  def move(self, coords = [0, 0]):
    self.rect = coords
    draw_all()
    screen.blit(self.image, self.rect)

  def rot_center(self):
    self.image = pygame.transform.rotate(self.image, self.angle)
    draw_all()
    screen.blit(self.image, self.rect)
    
class Frame(pygame.sprite.Sprite):
  def __init__(self, image_file = None, location = None, dim = screen, color = (250, 250, 250)):
    pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
    if image_file and location != None :
      self.image = pygame.image.load(image_file)
      self.rect = self.image.get_rect()
      self.rect.left, self.rect.top = location
    self.frame = pygame.Surface(dim.get_size())
    self.frame = self.frame.convert()
    self.frame.fill(color)

def create_text(dim, blitted, color = (0, 0, 0), font = "", msg = "", position = [width, hight], alias = True):
    font = pygame.font.SysFont(font, dim)
    text = font.render(msg, alias, color)
    textpos = text.get_rect()
    textpos.center = position
    blitted.blit(text, textpos)

def create_frames(name = "frame0", dim = screen, color = (250, 250, 250), image ="" ):
  name = pygame.Surface(dim.get_size())
  name = name.convert()
  name.fill(color)
  return name, img

def blit_frames(frame, coords = (0, 0), image = None, image_rect = None):
  if image and image_rect != None :
    frame.blit(image, image_rect)
  screen.blit(frame, coords)
  pygame.display.update()
  pygame.display.flip()

def draw_sprites(sprites, frame, group):
  group.update()
  group.draw(screen)
  pygame.display.flip()

def draw_texts(message = [], position = []):
  for x in range(5):
    create_text(font = "squared_display", dim = 100, msg = message[x], position = position[x], blitted = Frame1.frame)
    create_text(font = "squared_display", dim = 100, msg = message[x], position = position[x], blitted = Frame1_background.frame)

def draw_all():
  blit_frames(Frame1_background.frame, Frame1_background.rect, image = Frame1_background.image, image_rect = Frame1_background.rect)
  draw_sprites(sprites_group, Frame1_background.frame, Piece_sprites)
  draw_sprites(people_group, Frame1.frame, people_print)

def level1():
  if Piece1.square == "square3" and Piece1.pos == "right":
    Piece1.solution = True
  if Piece2.square == "square4" and Piece2.pos == "right":
    Piece2.solution = True
  if Piece3.square == "square2" and Piece3.pos == "right":
    Piece3.solution = True
  if Piece4.square == "square1" and Piece4.pos == "up":
    Piece4.solution = True

def win():
  if Piece1.solution and Piece2.solution and Piece3.solution and Piece4.solution == True:
    create_text(font = "squared_display", dim = 120, msg = "you won", position = (width/2, hight/2), blitted = Frame_win.frame)
    screen.blit(Frame_win.frame, (0, 0))
    return True

background = Frame()
Frame1 = Frame("images\\field1.png", [-20, 0])
Frame1_background = Frame("images\\field1.png", [-20, 0])
Frame_win = Frame()

pygame.mixer.music.load("music.mp3")


Piece1 = Puzzle_piece("images\\piece11.png", coords1)
Piece1.pos = "right"
Piece2 = Puzzle_piece("images\\piece21.png", coords2)
Piece3 = Puzzle_piece("images\\piece31.png", coords3)
Piece4 = Puzzle_piece("images\\piece41.png", coords4)

Person1 = Person("images\\person1.jpeg", coords5)
Person2 = Person("images\\person2.jpeg", coords6)
Person3 = Person("images\\person3.jpeg", coords7)
Person4 = Person("images\\person4.jpeg", coords8)
Person5 = Person("images\\person5.jpeg", coords9)

people_group = [Person1, Person2, Person3, Person4, Person5]
sprites_group = [Piece1, Piece2, Piece3, Piece4]

Piece_sprites = pygame.sprite.RenderPlain(sprites_group)
people_print = pygame.sprite.RenderPlain(people_group)

solution = ["= 0", "= 1", "= 2", "= 3", "= 1"]
position = [text1, text2, text3, text4, text5]
create_text(font = "squared_display", dim = 120, msg = "HIDDEN BOYS", position = (width/2, hight/4), blitted = background.frame)
create_text(font = "squared_display", dim = 50, msg = "Click to start", position = (width/2, hight/2), blitted = background.frame)

screen.blit(background.frame, (0, 0))
pygame.display.flip()

def main():
  clock = pygame.time.Clock()
  crash = False
  while not crash:
    frame = 0
    counter = 0
    clock.tick(40)

    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.mixer.music.stop()
        failed = True

      elif event.type == pygame.MOUSEBUTTONDOWN:
        if frame == 0:
          draw_texts(solution, position)
          draw_all()
          pygame.mixer.music.play(-1, 0.0)
          frame += 1

      elif event.type == pygame.KEYDOWN and pygame.key.get_focused() == True:
        if event.key == K_w:
          Piece1.state = "selected"
          Piece1.counter += 1

        elif event.key == K_a:
          Piece2.state = "selected"
          Piece2.counter += 1
          
        elif event.key == K_s:
          Piece3.state = "selected"
          Piece3.counter += 1
          
        elif event.key == K_d:
          Piece4.state = "selected"
          Piece4.counter += 1

        elif event.key == K_1:
          for x in range(len(sprites_group)):
            if sprites_group[x].state == "selected":
              sprites_group[x].move(square1)
              sprites_group[x].square = "square1"
              pygame.display.flip()

        elif event.key == K_2:
          for x in range(len(sprites_group)):
            if sprites_group[x].state == "selected":
              sprites_group[x].move(square2)
              sprites_group[x].square = "square2"
              pygame.display.flip()

        elif event.key == K_3:
          for x in range(len(sprites_group)):
            if sprites_group[x].state == "selected":
              sprites_group[x].move(square3)
              sprites_group[x].square = "square3"
              pygame.display.flip()

        elif event.key == K_4:
          for x in range(len(sprites_group)):
            if sprites_group[x].state == "selected":
              sprites_group[x].move(square4)
              sprites_group[x].square = "square4"
              pygame.display.flip()

        elif event.key == K_r:
          for x in range(len(sprites_group)):
            if sprites_group[x].state == "selected":
              sprites_group[x].angle = -90
              sprites_group[x].rot_center()
              if sprites_group[x] == Piece1:
                if sprites_group[x].pos == "right":
                  sprites_group[x].pos = "left"
                else:
                  sprites_group[x].pos = "right"
              else:
                if sprites_group[x].pos == "up":
                  sprites_group[x].pos = "right"
                elif sprites_group[x].pos == "right":
                  sprites_group[x].pos = "down"
                elif sprites_group[x].pos == "down":
                  sprites_group[x].pos = "left"
                elif sprites_group[x].pos == "left":
                  sprites_group[x].pos = "up"


      elif event.type == pygame.KEYUP:
        if event.key == K_w or K_a or K_s or K_d:
          if Piece1.counter % 2 == 0:
            Piece1.state = "unselected"
          if Piece2.counter % 2 == 0:
            Piece2.state = "unselected"
          if Piece3.counter % 2 == 0:
            Piece3.state = "unselected"
          if Piece4.counter % 2 == 0:
            Piece4.state = "unselected"
        draw_sprites(sprites_group, Frame1_background.frame, Piece_sprites)
        level1()
        win()
        if win() == True:
          crash = True
          pygame.time.wait(1500)
      pygame.display.flip()

if __name__ == '__main__': main()