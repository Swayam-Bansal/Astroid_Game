import pygame

from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def Title_Screen(screen):
    while True:
         # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw the title screen text
        font = pygame.font.Font("assets/fonts/staubach/Staubach.ttf", 74)
        text = font.render("Asteroids", True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        
        # check for any events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                game_loop(screen)
                return
            
        # Update the display
        pygame.display.flip()

def game_loop(screen):
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Asteroid.containers = updatable, drawable, asteroids
    Player.containers = updatable, drawable
    AsteroidField.containers = updatable
    Shot.containers = updatable, drawable, bullets

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            # on pressing escape, go back to title screen
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                Title_Screen(screen)
                return

        # Fill the screen with black
        screen.fill((0, 0, 0))

        for elemenets in updatable:
            elemenets.update(dt)

        for elemenets in asteroids:
            if elemenets.check_collision(player):
                print("Collision detected!")
                print("GAME OVER")
                pygame.quit()
                return
            
            for bullet in bullets:
                if elemenets.check_collision(bullet):
                    # print("Collision detected between asteroid and bullet!")
                    # elemenets.kill()
                    elemenets.split()
                    bullet.kill()

        for elemenets in drawable:
            elemenets.draw(screen)

        # update the whole screen
        pygame.display.flip()

        dt = clock.tick(60)/1000


def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    pygame.mouse.set_visible(False)

    Title_Screen(screen)
    game_loop(screen)


if __name__ == "__main__":
    main()
