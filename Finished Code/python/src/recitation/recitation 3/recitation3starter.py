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
    # TODO Implement this!



def main():
    print("Drawing a head.")
    # Initialize pygame but don't open window
    pygame.init()

    draw_face()

    pygame.quit()

if __name__ == "__main__":
    main()