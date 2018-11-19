### Jiaxin Ge
### 58153795
### PyGame view


import pygame

import game_mechanics


ROW = 13
COLUMN = 6

S_COLOR = pygame.Color(224, 169, 146)
T_COLOR = pygame.Color(35, 80, 176)
V_COLOR = pygame.Color(146, 201, 224)
W_COLOR = pygame.Color(255, 56, 56)
X_COLOR = pygame.Color(162, 224, 146)
Y_COLOR = pygame.Color(224, 221, 146)
Z_COLOR = pygame.Color(226, 5, 255)
MATCH_COLOR = pygame.Color(255, 255, 255)
FRAME_COLOR = pygame.Color(255, 255, 255)

BACK_GROUND_COLOR = pygame.Color(146, 224, 206)

BOARD_COLOR = pygame.Color(82, 83, 92)

             

class ColumnGame():

    def __init__(self):
        """
        initialize the Column Game
        """
        self._running = True
        self._state = game_mechanics.ColumnState(ROW, COLUMN)


    def run(self) -> None:
        """
        the main function that run the game
        """
        pygame.init()

        self._resize_surface((800, 800))

        clock = pygame.time.Clock()
        tick = 0

        while self._running:
            
            if tick == 14:
                tick = 0
                board_init = self._state._copy_game_board ()
                self._state.command(" ")
                board_final = self._state._copy_game_board ()
   
                if self._check_if_drop_command_work(board_init, board_final):
                     self._state.command("F")
                self._state.print_game_board()

            clock.tick(15)             
            tick +=1
            self._handle_events()
            self._draw_interface()
                
        
        pygame.quit()



    ### PRIVATE METHOD

    def _check_if_drop_command_work(self, board_init: list, board_final: list) -> bool:
        """
        check if the drop command changes the gaming board; if not, return False
        """
        for col in range (self._state._column):
            for row in range (self._state._row):
                if board_final[col][row] != board_init[col][row]:
                    return False
                    

        return True
        
    
    def _handle_events(self) -> None:
        """
        handle the events during the game, including key pressed and Quit
        """
            
        for event in pygame.event.get():
            self._handle_event(event)

        self._handle_keys()


    def _handle_keys(self) -> None:
        """
        the command for key pressed
        """

        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE]:
            self._state.command("R")

        if key[pygame.K_LEFT]:
            self._state.command("<")

        if key[pygame.K_RIGHT]:
            self._state.command(">")


    def _handle_event(self, event) -> None:
        """
        handle the events wtih quit and changing the size of the surface
        """

        if event.type == pygame.QUIT:
            self._end_game()
        elif event.type == pygame.VIDEORESIZE:
            self._resize_surface(event.size)

    
    def _draw_interface(self) -> None:
        """
        draw the interface of the game
        """
        surface = pygame.display.get_surface()

        surface.fill(BACK_GROUND_COLOR)

        self._draw_board_background(surface)

        self._draw_board_item()

        pygame.display.flip()



    def _draw_board_background(self, surface) -> None:
        """
        draw game board background with BOARD_COLOR
        """

        pygame.draw.rect(surface, BOARD_COLOR, (self._frac_x_to_pixel_x(0.3),
                        self._frac_y_to_pixel_y(0.05),
                        self._frac_x_to_pixel_x(0.42),
                        self._frac_y_to_pixel_y(0.91)))
        


    def _draw_board_item(self) -> None:
        """
        draw each different items in the board
        """

        for row in range (self._state._row):
            for col in range (self._state._column):

                if "[" in str(self._state._board[col][row]):
                    self._draw_colors_with_frame(col, row)

                elif "*" in str(self._state._board[col][row]):
                    self._draw_color_with_rect(MATCH_COLOR, col, row)

                elif "|" in str(self._state._board[col][row]):
                    self._draw_colors_with_frame(col, row)
                    self._draw_inner_rect(col, row)


                if self._state._board[col][row] == " S ":
                    self._draw_color_with_rect(S_COLOR, col, row)
                elif self._state._board[col][row] == " T ":
                    self._draw_color_with_rect(T_COLOR, col, row)
                elif self._state._board[col][row] == " V ":
                    self._draw_color_with_rect(V_COLOR, col, row)
                elif self._state._board[col][row] == " W ":
                    self._draw_color_with_rect(W_COLOR, col, row)
                elif self._state._board[col][row] == " X ":
                    self._draw_color_with_rect(X_COLOR, col, row)
                elif self._state._board[col][row] == " Y ":
                    self._draw_color_with_rect(Y_COLOR, col, row)
                elif self._state._board[col][row] == " Z ":
                    self._draw_color_with_rect(Z_COLOR, col, row)
                    

    def _draw_color_with_rect(self, color: pygame.Color, col, row) -> None:
        """
        draw rectangle in specific color
        """
        surface = pygame.display.get_surface()
        
        pygame.draw.rect(surface, color, (self._frac_x_to_pixel_x(0.3 + 0.07 * col) ,
                                          self._frac_y_to_pixel_y(0.05 + 0.07 * row),
                                            self._frac_x_to_pixel_x(0.06),
                                            self._frac_y_to_pixel_y(0.06)))
    
    def _draw_color_with_rect_frame(self, color: pygame.Color, col, row) -> None:
        """
        draw rectangle  frame in specific color
        """
        surface = pygame.display.get_surface()
        
        pygame.draw.rect(surface, color, (self._frac_x_to_pixel_x(0.3 + 0.07 * col) ,
                                          self._frac_y_to_pixel_y(0.05 + 0.07 * row),
                                            self._frac_x_to_pixel_x(0.06),
                                            self._frac_y_to_pixel_y(0.06)), 8)
     

    def _draw_colors_with_frame(self, col: int, row: int) -> None:
        """
        draw rectangle with frame in specific color
        """
        
        if str(self._state._board[col][row][1]) == "S":
            self._draw_color_with_rect_frame(S_COLOR, col, row)
        elif str(self._state._board[col][row][1])  == "T":
            self._draw_color_with_rect_frame(T_COLOR, col, row)
        elif str(self._state._board[col][row][1])  == "V":
            self._draw_color_with_rect_frame(V_COLOR, col, row)
        elif str(self._state._board[col][row][1])  == "W":
            self._draw_color_with_rect_frame(W_COLOR, col, row)
        elif str(self._state._board[col][row][1])  == "X":
            self._draw_color_with_rect_frame(X_COLOR, col, row)
        elif str(self._state._board[col][row][1])  == "Y":
            self._draw_color_with_rect_frame(Y_COLOR, col, row)
        elif str(self._state._board[col][row][1])  == "Z":
            self._draw_color_with_rect_frame(Z_COLOR, col, row)


    def _draw_inner_rect(self, col: int, row: int) -> None:
        """
        draw white inner rectangle 
        """

        surface = pygame.display.get_surface()
        
        pygame.draw.rect(surface, MATCH_COLOR, (self._frac_x_to_pixel_x(0.3 + 0.07 * col + 0.01) ,
                                              self._frac_y_to_pixel_y(0.05 + 0.07 * row + 0.01),
                                                self._frac_x_to_pixel_x(0.04),
                                                self._frac_y_to_pixel_y(0.04)))


    def _end_game(self) -> None:
        """
        end the game
        """
        self._running = False

    
    def _resize_surface(self, size:(int, int)) -> None:
        """
        resize the surface of the game
        """
        surface = pygame.display.set_mode(size, pygame.RESIZABLE)
        self._surface = surface


    def _frac_x_to_pixel_x(self, frac_x: float) -> int:
        return self._frac_to_pixel(frac_x, self._surface.get_width())


    def _frac_y_to_pixel_y(self, frac_y: float) -> int:
        return self._frac_to_pixel(frac_y, self._surface.get_height())


    def _frac_to_pixel(self, frac: float, max_pixel: int) -> int:
        return int(frac * max_pixel)



if __name__ == '__main__':
    ColumnGame().run()


