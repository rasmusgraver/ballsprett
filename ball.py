import pygame
import math

class Ball:
    def __init__(self, farge, radius, x, y, dx, dy):
        self.farge = farge
        self.radius = radius
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.mass = radius ** 2  # Mass is proportional to the square of the radius

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.farge, (self.x, self.y), self.radius)

    def check_collision(self, screen):
        if self.x - self.radius < 0:
            self.dx = -self.dx
            self.x = self.radius
        if self.x + self.radius > screen.get_width():
            self.dx = -self.dx
            self.x = screen.get_width() - self.radius

        if self.y - self.radius < 0:
            self.dy = -self.dy
            self.y = self.radius
        if self.y + self.radius > screen.get_height():
            self.dy = -self.dy
            self.y = screen.get_height() - self.radius
    
    def check_collision_with_balls(self, balls):
        for ball in balls:
            if self == ball:
                continue
            if self.distance_to(ball) < self.radius + ball.radius:
                self.resolve_collision_with(ball)
    
    def distance_to(self, ball):
        return ((self.x - ball.x) ** 2 + (self.y - ball.y) ** 2) ** 0.5
    
    def resolve_collision_with(self, ball):
        # calculate the angle between the two balls
        angle = math.atan2(self.y - ball.y, self.x - ball.x)
        distance = self.distance_to(ball)
        
        # calculate the relative speed
        relative_speed_x = self.dx - ball.dx
        relative_speed_y = self.dy - ball.dy
        
        # calculate the change in speed due to the collision
        change_in_speed_x = (relative_speed_x * math.cos(angle) + relative_speed_y * math.sin(angle)) * math.cos(angle)
        change_in_speed_y = (relative_speed_x * math.cos(angle) + relative_speed_y * math.sin(angle)) * math.sin(angle)
        
        # calculate the new velocities after the collision
        total_mass = self.mass + ball.mass
        self.dx -= (2 * ball.mass / total_mass) * change_in_speed_x
        self.dy -= (2 * ball.mass / total_mass) * change_in_speed_y
        ball.dx += (2 * self.mass / total_mass) * change_in_speed_x
        ball.dy += (2 * self.mass / total_mass) * change_in_speed_y
        
        # separate the balls to avoid overlap
        overlap = 0.5 * (self.radius + ball.radius - distance + 1)
        self.x += overlap * math.cos(angle)
        self.y += overlap * math.sin(angle)
        ball.x -= overlap * math.cos(angle)
        ball.y -= overlap * math.sin(angle)

