from ball import Ball

class Gravitasjonsball(Ball):
    gravity = 0.2

    def move(self):
        self.dy += self.gravity
        super().move()

