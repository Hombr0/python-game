import pygame
from pygame.locals import *
import sys
import os
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

pygame.init()
screen = pygame.display.set_mode((width, hight))
pygame.display.set_caption('Hidden Boys')

class Puzzle_piece(pygame.sprite.Sprite):
  def __init__(self, image_file, location):
    pygame.sprite.Sprite.__init__(self)
    self.counter = 0
    self.image = pygame.image.load(image_file)
    self.rect = self.image.get_rect()
    self.rect.left, self.rect.top = location
    self.state = "still"
    self.area = screen.get_rect()
    self.angle = 0
    self.rectpos = [self.rect.left, self.rect.top]


  def move(self, coords = [0, 0]):
    self.rectpos = coords
    blit_frames(Frame1_background.frame, Frame1_background.rect, image = Frame1_background.image, image_rect = Frame1_background.rect)
    draw_sprites(sprites_group, Frame1_background.frame, Piece_sprites)
    screen.blit(self.image, self.rectpos)

  def rot_center(self):
    self.image = pygame.transform.rotate(self.image, self.angle)
    blit_frames(Frame1_background.frame, Frame1_background.rect, image = Frame1_background.image, image_rect = Frame1_background.rect)
    draw_sprites(sprites_group, Frame1_background.frame, Piece_sprites)
    screen.blit(self.image, self.rectpos)
    



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

def create_text(dim, blitted, color = (0, 0, 0), font = "", msg = "", position = (width, hight), alias = True):
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

def create_multilinetext(text):
    counter = 0
    for x in text:
      counter += 1
      screen.blit((pygame.font.SysFont('constantia',12).render(x, True, BLACK)),(300,10*descriptioncounter))

def draw_sprites(sprites, frame, group):
  for x in range(len(sprites)):
    screen.blit(frame, sprites[x].rect, sprites[x].rect)
  group.update()
  group.draw(screen)
  pygame.display.flip()

def win_level1():
  pass
group = []
background = Frame()
Frame1 = Frame("images\\field1.png", [-20, 0])
Frame1_background = Frame("images\\field1.png", [-20, 0])
Piece1 = Puzzle_piece("images\\piece11.png", coords1)
Piece2 = Puzzle_piece("images\\piece21.png", coords2)
Piece3 = Puzzle_piece("images\\piece31.png", coords3)
Piece4 = Puzzle_piece("images\\piece41.png", coords4)
sprites_group = [Piece1, Piece2, Piece3, Piece4]
Piece_sprites = pygame.sprite.RenderPlain(sprites_group)

create_text(font = "squared_display", dim = 120, msg = "HIDDEN BOYS", position = (width/2, hight/4), blitted = background.frame)
create_text(font = "squared_display", dim = 50, msg = "Click to start", position = (width/2, hight/2), blitted = background.frame)

   

screen.blit(background.frame, (0, 0))
pygame.display.flip()

def main():
  clock = pygame.time.Clock()
  while True:
    frame = 0
    counter = 0
    clock.tick(30)
    for event in pygame.event.get():
      if event.type == QUIT:
        return
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if frame == 0:
          blit_frames(Frame1.frame, Frame1.rect, image = Frame1.image, image_rect = Frame1.rect)
          draw_sprites(sprites_group, Frame1.frame, Piece_sprites)
          frame += 1
      elif event.type == pygame.KEYDOWN and pygame.key.get_focused() == True:
        if event.key == K_w:
          Piece1.state = "selected"
          Piece1.counter += 1
          '''if Piece1 not in sprites_group:
            sprites_group.append(Piece1)'''
        elif event.key == K_a:
          Piece2.state = "selected"
          Piece2.counter += 1
          '''if Piece2 not in sprites_group:
            sprites_group.append(Piece2)'''
        elif event.key == K_s:
          Piece3.state = "selected"
          Piece3.counter += 1
          '''if Piece3 not in sprites_group:
            sprites_group.append(Piece3)'''
        elif event.key == K_d:
          Piece4.state = "selected"
          Piece4.counter += 1
          '''if Piece4 not in sprites_group:
            sprites_group.append(Piece4)'''

        elif event.key == K_1:
          for x in range(len(sprites_group)):
            if sprites_group[x].state == "selected":
              sprites_group[x].move(square1)
              pygame.display.flip()
              '''sprites_group.remove(sprites_group[x])'''

        elif event.key == K_2:
          for x in range(len(sprites_group)):
            if sprites_group[x].state == "selected":
              sprites_group[x].move(square2)
              pygame.display.flip()
              '''sprites_group.remove(sprites_group[x])'''

        elif event.key == K_3:
          for x in range(len(sprites_group)):
            if sprites_group[x].state == "selected":
              sprites_group[x].move(square3)
              pygame.display.flip()
              '''sprites_group.remove(sprites_group[x])'''

        elif event.key == K_4:
          for x in range(len(sprites_group)):
            if sprites_group[x].state == "selected":
              sprites_group[x].move(square4)
              pygame.display.flip()
              '''sprites_group.remove(sprites_group[x])'''
        elif event.key == K_r:
          for x in range(len(sprites_group)):
            if sprites_group[x].state == "selected":
              sprites_group[x].angle = -90
              sprites_group[x].rot_center()


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




      
      pygame.display.update()
      pygame.display.flip()
      print(Piece1.state)
      print(Piece2.state)
      print(Piece3.state)
      print(Piece4.state)

if __name__ == '__main__': main()
''' if event.key == K_SPACE and frame == 0:
          create_text(12, font = "squared_display", msg = "ciao", position = (0, 0), blitted = Frame0.frame)
          blit_frames(Frame0.frame)'''
'''if event.type == MOUSEBUTTONDOWN:
              if pygame.mouse.get_pos in square1:
                Piece1.movepos = square1
                Piece1.move()
              elif pygame.mouse.get_pos() in square2:
'''
'''https://youtu.be/72FaRseZIqA
https://youtu.be/Hyj_CrvS5-o
https://youtu.be/4T73cvFPvxg
https://youtu.be/Ujqdle7CvIU'''

'''[240, 45] 
square2 = [25, 55]
square3 = [25, 245]
square4 = [248, 245]
coords1 = [800, 50]
coords2 = [550, 50]
coords3 = [550, 250]
coords4 = [810, 250]'''
'''if event.type == pygame.MOUSEBUTTONDOWN:
        if frame == 0:
          blit_frames(Frame1.frame, Frame1.rect, image = Frame1.image, image_rect = Frame1.rect)
          draw_sprites(sprites_group, Frame1.frame, Piece_sprites)
          frame += 1
        elif frame == 1:
          x, y = event.pos
          if Piece1.rect.collidepoint(x, y):
            print("ciao")
            Piece1.state = "selected"
            Piece1.counter += 1
            move_pieces(Piece1)
            pygame.display(coords1)
            
          if pygame.mouse.get_pos() in coords2:
            print("ciao")
            Piece2.state = "selected"
            Piece2.counter += 1
            move_pieces(Piece2)

          if pygame.mouse.get_pos() in coords3:
            Piece3.state = "selected"
            Piece3.counter += 1
            move_pieces(Piece3)

          if pygame.mouse.get_pos() in coords4:
            Piece4.state = "selected"
            Piece4.counter += 1
            move_pieces(Piece4)
            
      if event.type == pygame.MOUSEBUTTONUP:
        if pygame.mouse.get_pos() in coords1 or coords2 or coords3 or coords4:
          if Piece1.counter % 2 == 0:
            Piece1.state = "unselected"
          if Piece2.counter % 2 == 0:
            Piece2.state = "unselected"
          if Piece3.counter % 2 == 0:
            Piece3.state = "unselected"
          if Piece4.counter % 2 == 0:
            Piece4.state = "unselected"'''
'''for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      print("HEY")
      if pygame.mouse.get_pos() in square1 and piece.state == "selected":
        print("ciao")
        piece.updates(square2)
        piece.move()
      elif pygame.mouse.get_pos() in square2:
        piece.updates(square2)
        piece.move()
      elif pygame.mouse.get_pos() in square3:
        piece.updates(square3)
        piece.move()
      elif pygame.mouse.get_pos() in square4:
        piece.updates(square4)
        piece.move()'''
'''for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      print("HEY")
      if event.key == K_1:
        print("ciao")
        piece.updates(square1)
        piece.move()
      elif kevent.key == K_2:
        print("ciao")
        piece.updates(square2)
        piece.move()
      elif event.key == K_3:
        print("ciao")
        piece.updates(square3)
        piece.move()
      elif event.key == K_4:
        print("ciao")
        piece.updates(square4)
        piece.move()'''
