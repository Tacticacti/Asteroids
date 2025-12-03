from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_state, log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_degree = random.uniform(20, 50)
        smaller_asteroid_1_direction = self.velocity.rotate(random_degree)
        smaller_asteroid_2_direction = self.velocity.rotate(-random_degree)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        smaller_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_asteroid_1.velocity = smaller_asteroid_1_direction * 1.2
        smaller_asteroid_2.velocity = smaller_asteroid_2_direction * 1.2