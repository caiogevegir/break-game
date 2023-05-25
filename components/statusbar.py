import pygame

class StatusBar:
    
    score_position = (4, 4)
    lives_position = (420, 4)
    win_loss_position = (180, 4)
    font = None
    color = (255, 255, 255) # White

    @staticmethod
    def initialize_font():
        StatusBar.font = pygame.font.SysFont('courier', 30)

    @staticmethod
    def display_score(screen, score):
        screen.blit(StatusBar.font.render(f'{score}', True, StatusBar.color), StatusBar.score_position)
        
    @staticmethod
    def display_lives(screen, lives):
        screen.blit(StatusBar.font.render(f'\u2665 {lives}', True, StatusBar.color), StatusBar.lives_position)
    
    @staticmethod
    def display_win_message(screen):
        screen.blit(StatusBar.font.render('Ganhou! :)', True, StatusBar.color), StatusBar.win_loss_position)

    @staticmethod
    def display_loss_message(screen):
        screen.blit(StatusBar.font.render('Perdeu! :(', True, StatusBar.color), StatusBar.win_loss_position)
        