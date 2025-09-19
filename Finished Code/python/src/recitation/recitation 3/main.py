import pygame

def draw_face() -> None:
    """
    Draws a simple cartoon face onto the given Pygame surface.
    The face consists of:
      - A large white head (circle)
      - Two black eyes (circles)
      - A small black nose (circle)
      - A red rectangular mouth
    Args:
        None
    Returns:
        None
    """

    # Create an off-screen surface
    width, height = 1000, 2000
    surface = pygame.Surface((width, height))
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    surface.fill(black)
    # add head (white circle)
    pygame.draw.circle(surface, white, (500, 500), 200)

    # add nose (black circle)
    pygame.draw.circle(surface, black, (500, 550), 10)

    # add eyes (black circles)
    pygame.draw.circle(surface, black, (425, 475), 15)
    pygame.draw.circle(surface, black, (575, 475), 15)

    # add mouth (red rectangle)
    pygame.draw.rect(surface, red, (400, 600, 200, 20))

    # save to file
    pygame.image.save(surface, "fun.png")

def main():
    print("Drawing a head.")

    # Initialize pygame but don't open window
    pygame.init()

    draw_face()

    pygame.quit()

if __name__ == "__main__":
    main()