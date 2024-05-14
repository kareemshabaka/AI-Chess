import pygame
import sys
import random
import os
import neat


pygame.init()

WIDTH = 1080

NUM_TILES = 8
TILE_SIZE = WIDTH / NUM_TILES

screen = pygame.display.set_mode((WIDTH, WIDTH))
clock = pygame.time.Clock()

b_pawn = pygame.transform.scale(pygame.image.load('assets/b_pawn.png'), (int(TILE_SIZE) - 20, int(TILE_SIZE) - 20))

w_pawn = pygame.transform.scale(pygame.image.load('assets/w_pawn.png'), (int(TILE_SIZE) - 20, int(TILE_SIZE) - 20))

WHITE_PIECE = 0
BLACK_PIECE = 1

def chess_pos_to_cords(x, y):
    return (x * TILE_SIZE, y * TILE_SIZE)

class Piece(pygame.sprite.Sprite):
    def __init__(self, color, image):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.image = image
        self.rect = self.image.get_rect(center=pygame.Rect(0, 0, TILE_SIZE, TILE_SIZE).center)

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Pawn(Piece):
    def __init__(self, color):
        image = None
        if color == WHITE_PIECE:
            image = w_pawn
        else:
            image = b_pawn

        Piece.__init__(self, color, image)

class Board:
    def __init__(self):
        self.image = pygame.image.load('assets/board.png')
        self.tiles = [None for _ in range(NUM_TILES*NUM_TILES)]
    def draw(self):
        screen.blit(self.image, (0, 0))

    def get_index(self, x, y):
        return int(x / TILE_SIZE) + int(y / TILE_SIZE) * NUM_TILES
    
    def is_tile_empty(self, x, y):
        return self.tiles[self.get_index(x, y)] == None
    
    def add_piece(self, piece, x, y):
        self.tiles[self.get_index(x, y)] = piece
        piece.move(x, y)
    
    def remove_piece(self, piece, x, y):
        self.tiles[self.get_index(x, y)] = None

    def move_piece(self, piece, x1, y1, x2, y2):
        piece = self.tiles[self.get_index(x1, y1)]
        self.tiles[self.get_index(x1, y1)] = None
        self.tiles[self.get_index(x2, y2)] = piece

    def get_piece(self, x, y):
        return self.tiles[self.get_index(x, y)]
    

def main():

    running = True

    board = Board()

    pieces = pygame.sprite.Group()
    for i in range(1):
        white_pawn = Pawn(WHITE_PIECE)
        black_pawn = Pawn(BLACK_PIECE)

        pieces.add(white_pawn)
        pieces.add(black_pawn)

        cords = chess_pos_to_cords(i, 1)
        board.add_piece(white_pawn, cords[0], cords[1])

        cords = chess_pos_to_cords(i, 6)
        board.add_piece(black_pawn, cords[0], cords[1])

    # for _ in range(2):
    #     pieces.add(Rook(WHITE_PIECE))
    #     pieces.add(Rook(BLACK_PIECE))

    # for _ in range(2):
    #     pieces.add(Knight(WHITE_PIECE))
    #     pieces.add(Knight(BLACK_PIECE))
    
    # for _ in range(2):
    #     pieces.add(Bishop(WHITE_PIECE))
    #     pieces.add(Bishop(BLACK_PIECE))
    
    # pieces.add(Queen(WHITE_PIECE))
    # pieces.add(Queen(BLACK_PIECE))
    # pieces.add(King(WHITE_PIECE))
    # pieces.add(King(BLACK_PIECE))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        board.draw()
        pieces.draw(screen)

        #pygame.draw.rect(screen, (255, 0, 0), board.tiles[8].rect, 2)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()