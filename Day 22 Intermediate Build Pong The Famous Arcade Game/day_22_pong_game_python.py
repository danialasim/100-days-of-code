# Pong Game - Pygame Implementation
# Alternative version using Pygame instead of Turtle graphics

import pygame
import random

# Initialize Pygame
pygame.init()

#--------------------
# Game Constants
#--------------------

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Game objects dimensions
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 90
BALL_SIZE = 15

# Game speed
FPS = 60

#--------------------
# Game Setup
#--------------------

# Initialize display window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong Game')

# Initialize game clock
clock = pygame.time.Clock()

#--------------------
# Game Classes
#--------------------

class Paddle:
    """Class representing a paddle in the game."""
    
    def __init__(self, x, y):
        """Initialize paddle with position and dimensions."""
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 5

    def move(self, up=True):
        """Move paddle up or down and keep it within screen bounds."""
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        self.rect.clamp_ip(screen.get_rect())  # Keep paddle on screen

    def draw(self):
        """Draw paddle on screen."""
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    """Class representing the ball in the game."""
    
    def __init__(self):
        """Initialize ball with center position and random direction."""
        self.rect = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2,
                              HEIGHT // 2 - BALL_SIZE // 2,
                              BALL_SIZE, BALL_SIZE)
        # Set random initial direction
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])

    def move(self):
        """Move ball and handle wall collisions."""
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Bounce off top and bottom walls
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy *= -1

    def draw(self):
        """Draw ball on screen."""
        pygame.draw.rect(screen, WHITE, self.rect)

#--------------------
# Helper Functions
#--------------------

def draw_score(player_score, computer_score):
    """Draw scores on screen."""
    font = pygame.font.Font(None, 74)
    # Render score text
    player_text = font.render(str(player_score), 1, WHITE)
    computer_text = font.render(str(computer_score), 1, WHITE)
    # Position and draw scores
    screen.blit(player_text, (WIDTH * 3/4, 10))
    screen.blit(computer_text, (WIDTH / 4, 10))

#--------------------
# Main Game Loop
#--------------------

def main():
    """Main game function handling game loop and logic."""
    # Create game objects
    player_paddle = Paddle(WIDTH - PADDLE_WIDTH - 10, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    computer_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball()

    # Initialize scores
    player_score = 0
    computer_score = 0

    # Game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_paddle.move(up=True)
        if keys[pygame.K_DOWN]:
            player_paddle.move(up=False)

        # Computer AI movement
        if computer_paddle.rect.centery < ball.rect.centery:
            computer_paddle.move(up=False)
        elif computer_paddle.rect.centery > ball.rect.centery:
            computer_paddle.move(up=True)

        # Ball movement and collisions
        ball.move()
        if ball.rect.colliderect(player_paddle.rect) or ball.rect.colliderect(computer_paddle.rect):
            ball.dx *= -1

        # Scoring
        if ball.rect.left <= 0:
            player_score += 1
            ball = Ball()
        elif ball.rect.right >= WIDTH:
            computer_score += 1
            ball = Ball()

        # Check for win condition
        if player_score == 10 or computer_score == 10:
            break

        # Drawing
        screen.fill(BLACK)
        player_paddle.draw()
        computer_paddle.draw()
        ball.draw()
        draw_score(player_score, computer_score)

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

    # Game over screen
    font = pygame.font.Font(None, 74)
    if player_score > computer_score:
        text = font.render("You Win!", 1, WHITE)
    else:
        text = font.render("Computer Wins!", 1, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 
                      HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()

    # Wait before closing
    pygame.time.wait(3000)
    pygame.quit()

# Start game if script is run directly
if __name__ == "__main__":
    main()
