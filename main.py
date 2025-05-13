import pygame

from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
            
        # for i in range(len(asteroids)):
        #     for j in range(i + 1, len(asteroids)):
        #         if asteroids[i].check_collision(asteroids[j]):
        #             print("Collision detected between asteroids!")
        #             asteroids[i].kill()
        #             asteroids[j].kill()
        #             # Handle asteroid collision here

        #     for bullet in bullets:
        #         if asteroids[i].check_collision(bullet):
        #             print("Collision detected between asteroid and shot!")
        #             # Handle asteroid and shot collision here
        #             asteroids[i].kill()
        #             bullet.kill()

        for elemenets in drawable:
            elemenets.draw(screen)

        # update the whole screen
        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
