"""
Introduction Arcade - dessiner un paysage
TP5 - Raul Mic
Construire une image avec la librairie Arcade et des formes de base
"""

import arcade

# Définition de valeurs constantes
IMAGE_WIDTH = 1024
IMAGE_HEIGHT = 1024
IMAGE_TITLE = "Paysage"


def draw_background():
    """
    Dessiner l'arrière-plan
    """
    # Dessiner le ciel
    arcade.draw_lrtb_rectangle_filled(0, IMAGE_WIDTH, IMAGE_HEIGHT,
                                      IMAGE_HEIGHT * (1 / 3), arcade.color.ITALIAN_SKY_BLUE)
    # Dessiner la terre
    arcade.draw_lrtb_rectangle_filled(0, IMAGE_WIDTH, IMAGE_HEIGHT / 3, 0, arcade.color.DARK_SPRING_GREEN)


def draw_sun(x, y):
    """
    Dessiner le soleil - cercle d'un rayon valeur constante 75 et des lignes comme rayons soleil
    Paramètres:
    - x: le centre du cercle sur l'axe x.
    - y: le centre du cercle sur l'axe y.
    """
    radius = 75
    arcade.draw_circle_filled(x, y, radius, arcade.color.AMBER)
    # Rayons soleil
    arcade.draw_line(x, y, x - 100, y, arcade.color.AMBER, 3)
    arcade.draw_line(x, y, x + 100, y, arcade.color.AMBER, 3)
    arcade.draw_line(x, y, x, y + 100, arcade.color.AMBER, 3)
    arcade.draw_line(x, y, x, y - 100, arcade.color.AMBER, 3)
    arcade.draw_line(x, y, x + 100, y + 100, arcade.color.AMBER, 3)
    arcade.draw_line(x, y, x + 100, y - 100, arcade.color.AMBER, 3)
    arcade.draw_line(x, y, x - 100, y + 100, arcade.color.AMBER, 3)
    arcade.draw_line(x, y, x - 100, y - 100, arcade.color.AMBER, 3)


def draw_bird(x, y):
    """
    Dessiner oiseau avec des arcs cercle
    Paramètres:
    - x: le centre de l'arc sur l'axe x.
    - y: le centre de l'arc sur l'axe y.
    """

    arcade.draw_arc_outline(x, y, 40, 40, arcade.color.LAVA, 0, 90)
    arcade.draw_arc_outline(x + 50, y, 40, 40, arcade.color.LAVA, 90, 180)


def draw_tree(x, y):
    """
    Dessiner arbre dans une position spécifique
    Paramètres:
    - x: coordonnée x sur l'axe x.
    - y: coordonnée y sur l'axe y.
   """

    # Dessiner les feuilles avec l'aide d'un triangle
    arcade.draw_triangle_filled(x + 80, y, x, y - 200, x + 160, y - 200, arcade.color.DARK_GREEN)
    # Dessiner le tronc avec l'aide d'un rectangle
    arcade.draw_lrtb_rectangle_filled(x + 60, x + 100, y - 200, y - 280, arcade.color.DARK_BROWN)


def draw_tent(x, y):
    """
    Dessiner une tente en forme de polygone et une ligne pour le zipper
    Paramètres:
    - x: coordonnée x sur l'axe x.
    - y: coordonnée y sur l'axe y.
   """

    point_list = ((x, y),
                  (x + 150, y),
                  (x + 150, y + 75),
                  (x + 100, y + 100),
                  (x + 50, y + 100),
                  (x, y + 75))
    arcade.draw_polygon_filled(point_list, arcade.color.SPANISH_VIOLET)
    arcade.draw_line(x + 75, y, x + 75, y + 100, arcade.color.BLACK, 3)


def draw_cloud(x, y):
    """
    Dessiner une nuage avec l'aide de trois ellipses
    Paramètres:
    - x: coordonnée x sur l'axe x.
    - y: coordonnée y sur l'axe y.
   """

    arcade.draw_ellipse_filled(x - 50, y, x / 20 * 3, 35, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(x + 50, y, x / 20 * 3, 35, arcade.csscolor.WHITE)
    arcade.draw_ellipse_filled(x + 150, y, x / 20 * 3, 35, arcade.csscolor.WHITE)


def write_text(x, y):
    """
    Affiche un texte dans une elipse.
    Paramètres:
    - x: coordonnée x de l'emplacement du texte dans la fenêtre.
    - y: coordonnée y de l'emplacement du texte dans la fenêtre.
    """

    # L'information à afficher.
    text_string = "Arcade - utilisation des figures géométriques de base"
    # Affichage du texte au centre.
    arcade.draw_text(text_string, x, y, arcade.color.GREEN, 20, width=IMAGE_WIDTH, align="center")


def main():
    """

    Programme principale

    """

    # Ouvrir fenêtre
    arcade.open_window(IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_TITLE)

    # Commencer à dessiner.
    arcade.start_render()

    # L'arrière-plan
    draw_background()

    # Le soleil
    draw_sun(130, 900)

    # Les arbres
    draw_tree(24, 511)
    draw_tree(150, 350)
    draw_tree(850, 580)
    draw_tree(400, 400)
    draw_tree(250, 580)
    draw_tree(700, 400)

    # Les oiseaux
    draw_bird(500, 860)
    draw_bird(400, 800)
    draw_bird(560, 830)
    draw_bird(300, 740)
    draw_bird(620, 800)

    # Tente de camping
    draw_tent(550, 300)

    # Nuage
    draw_cloud(800, 950)

    # Texte
    write_text(150, 75)

    # Finir à dessiner et afficher le paysage.
    arcade.finish_render()

    # Garder la fenêtre ouverte, l'utilisateur va le fermer.
    arcade.run()


if __name__ == "__main__":

    main()
