from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = (255, 255, 255)
        line_Width = 2
        center = pygame.Vector2(self.position.x, self.position.y)
        pygame.draw.circle(screen, color, center, self.radius, line_Width)

    def update(self, dt):
        self.position += self.velocity * dt
        