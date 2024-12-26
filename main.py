import pygame
from ball import Ball
from gravitasjonsball import Gravitasjonsball

def main():
    # Initialize Pygame
    pygame.init()
    # Set up the display
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Ball Game")

    clock = pygame.time.Clock()
    FPS = 60

    # Create a list of balls
    balls = []
    balls.append(Ball((100, 0, 0), 10, 100, 300, 5, 5))
    balls.append(Ball((0, 100, 0), 20, 200, 300, -3, -6))
    balls.append(Ball((0, 0, 100), 30, 150, 100, 7, -2))
    balls.append(Ball((30, 50, 0), 5, 200, 150, -5, 3))
    balls.append(Ball((0, 100, 100), 15, 100, 250, 4, -4))
    balls.append(Gravitasjonsball((140, 140, 0), 35, 100, 40, 4, 0))

    # Main loop
    running = True
    while running:
        clock.tick(FPS)
        
        # Clear the screen
        screen.fill((255, 255, 255))

        # Update the positions of the balls
        for i in range(len(balls)):
            balls[i].move()
            balls[i].check_collision(screen)
            #for j in range(i + 1, len(balls)):
            balls[i].check_collision_with_balls(balls[i + 1:])
        # for ball in balls:
        #    ball.move()
        #    ball.check_collision(screen)
        #    ball.check_collision_with_balls(balls)
        
        # Draw the balls
        for ball in balls:
            ball.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the display
        pygame.display.update()
        
    # End the game after the loop has ended:
    pygame.quit()

if __name__ == '__main__':
    main()
