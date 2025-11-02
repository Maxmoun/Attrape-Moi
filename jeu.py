import pygame
import sys
import random

pygame.init()


LARGEUR_ECRAN = 800
HAUTEUR_ECRAN = 600
ECRAN = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN))
pygame.display.set_caption("Maman Attrape-Moi ! La Chasse aux Bêtises")


BLANC = (255, 255, 255)
VERT = (0, 200, 0)      
BLEU = (0, 0, 200)      
ROUGE = (200, 0, 0)     
NOIR = (0, 0, 0)
GRIS_CLAIR = (200, 200, 200)


VITESSE_JEU = 6       
VITESSE_MAMAN = 5     
TAILLE_MAMAN = 50
TAILLE_ENFANT = 40
TAILLE_OBSTACLE = 30
INTERVALLE_BASE_OBS = 100 


maman_rect = pygame.Rect(100, HAUTEUR_ECRAN // 2 - TAILLE_MAMAN // 2, 
                        TAILLE_MAMAN, TAILLE_MAMAN)
enfant_rect = pygame.Rect(maman_rect.x + 50, maman_rect.y, TAILLE_ENFANT, TAILLE_ENFANT)
obstacles = []
SCORE = 0
JEU_ACTIF = True
generation_intervalle = INTERVALLE_BASE_OBS



def reinitialiser_jeu():
    """Réinitialise toutes les variables pour commencer une nouvelle partie."""
    global JEU_ACTIF, SCORE, obstacles, generation_intervalle
    JEU_ACTIF = True
    SCORE = 0
    obstacles = []
    generation_intervalle = INTERVALLE_BASE_OBS
    maman_rect.y = HAUTEUR_ECRAN // 2 - TAILLE_MAMAN // 2

def dessiner_bouton(texte, rect, couleur_fond):
    """Dessine le bouton et renvoie son rectangle."""
    pygame.draw.rect(ECRAN, couleur_fond, rect)
    
    police = pygame.font.Font(None, 40)
    texte_rendu = police.render(texte, True, NOIR)
    
  
    texte_rect = texte_rendu.get_rect(center=rect.center)
    ECRAN.blit(texte_rendu, texte_rect)
    return rect

def dessiner_objets():
    """Dessine tous les éléments sur l'écran."""
    ECRAN.fill(BLANC)

    pygame.draw.rect(ECRAN, BLEU, enfant_rect)
   
    pygame.draw.rect(ECRAN, VERT, maman_rect)

    for obs in obstacles:
        pygame.draw.rect(ECRAN, ROUGE, obs)

    police = pygame.font.Font(None, 36)
    texte_score = police.render(f"Bêtises Évitées: {SCORE}", True, NOIR)
    ECRAN.blit(texte_score, (10, 10))

    pygame.display.flip()

def generer_obstacle():
    """Crée un nouvel obstacle aléatoirement."""
    y = random.randint(0, HAUTEUR_ECRAN - TAILLE_OBSTACLE)
    nouvel_obstacle = pygame.Rect(LARGEUR_ECRAN, y, TAILLE_OBSTACLE, TAILLE_OBSTACLE)
    obstacles.append(nouvel_obstacle)

def deplacer_obstacles():
    """Déplace les obstacles et met à jour le score."""
    global SCORE, generation_intervalle
    for obs in obstacles[:]:
        obs.x -= VITESSE_JEU
        if obs.right < 0:
            obstacles.remove(obs)
            SCORE += 1
            generation_intervalle = max(30, generation_intervalle - 1) 

horloge = pygame.time.Clock()
generation_timer = 0
bouton_redemarrer_rect = pygame.Rect(0, 0, 0, 0)

while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not JEU_ACTIF and evenement.type == pygame.MOUSEBUTTONDOWN:
            if bouton_redemarrer_rect.collidepoint(evenement.pos):
                reinitialiser_jeu()

    if JEU_ACTIF:
        
        touches = pygame.key.get_pressed()
        if touches[pygame.K_UP]:
            maman_rect.y -= VITESSE_MAMAN
        if touches[pygame.K_DOWN]:
            maman_rect.y += VITESSE_MAMAN

        maman_rect.top = max(0, maman_rect.top)
        maman_rect.bottom = min(HAUTEUR_ECRAN, maman_rect.bottom)

  
        deplacer_obstacles()
        generation_timer += 1
        if generation_timer > generation_intervalle:
            generer_obstacle()
            generation_timer = 0
       
        for obs in obstacles:
            if maman_rect.colliderect(obs):
                JEU_ACTIF = False 
                print(f"GAME OVER! Score final: {SCORE}")
                
        dessiner_objets()


    else:
        ECRAN.fill(NOIR)
        
        police_fin = pygame.font.Font(None, 74)
        texte_fin = police_fin.render("GAME OVER", True, ROUGE)
        texte_score_fin = police_fin.render(f"Score final: {SCORE}", True, BLANC)
        
        ECRAN.blit(texte_fin, (LARGEUR_ECRAN//2 - texte_fin.get_width()//2, HAUTEUR_ECRAN//3 - 40))
        ECRAN.blit(texte_score_fin, (LARGEUR_ECRAN//2 - texte_score_fin.get_width()//2, HAUTEUR_ECRAN//3 + 40))

        bouton_rect = pygame.Rect(0, 0, 250, 70)
        bouton_rect.center = (LARGEUR_ECRAN // 2, HAUTEUR_ECRAN // 3 + 150)
        bouton_redemarrer_rect = dessiner_bouton("REJOUER", bouton_rect, GRIS_CLAIR)
        
        pygame.display.flip()

    horloge.tick(60)