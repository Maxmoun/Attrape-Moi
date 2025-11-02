    Description du Jeu

Ce jeu de carrés est un projet réalisé dans un cadre académique et personnel. Ce travail m'a permis de comprendre et d'utiliser des bibliothèques Python que je ne connaissais pas avant. Le jeu commence en définissant la taille de l'écran, les couleurs, les vitesses, et les dimensions des objets (le carré du joueur et les carrés Obstacles). La partie est gérée par la boucle principale qui vérifie si le jeu est actif (JEU_ACTIF).
Tant que le jeu est actif, le joueur contrôle le carré fixe (vert) avec les flèches Haut/Bas pour éviter les Obstacles (rouges) qui se déplacent de droite à gauche. Les obstacles apparaissent régulièrement. Chaque obstacle évité augmente le SCORE et réduit le temps d'attente avant l'apparition du prochain obstacle, ce qui rend le jeu plus rapide.
Le joueur perd si son carré fixe touche un Obstacle. Quand le jeu s'arrête (JEU_ACTIF = False), l'écran affiche "GAME OVER", le score final, et un bouton "REJOUER" qui permet de tout réinitialiser pour recommencer une nouvelle partie.

Le programme exécutable, prêt pour l'installation, est disponible dans le répertoire Rendu.
