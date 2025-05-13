import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0.0
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        color = (255, 255, 255)
        line_Width = 2
        pygame.draw.polygon(screen, color, self.triangle(), line_Width)
        # pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius, line_Width)

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt):
        initial_vector = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += initial_vector * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)

        if keys[pygame.K_SPACE] or keys[pygame.K_LCTRL]:
            if self.shoot_timer > 0.0:
                self.shoot_timer -= dt
                # print("cant shoot right now : ", self.shoot_timer)
            else:
                self.shoot()
                # print("shooting")
                self.shoot_timer += self.shoot_cooldown

    def shoot(self):
        bullet = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        color = (255, 255, 0)
        line_Width = 2
        pygame.draw.circle(screen, color, self.position, self.radius, line_Width)

    def update(self, dt):
        self.position += self.velocity * dt

        