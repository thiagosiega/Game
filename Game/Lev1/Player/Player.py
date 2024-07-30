import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 100
        self.mp = 100
        self.atk = 10
        self.defense = 5
        self.altura = 50
        self.largura = 50
        self.renger = 200
        self.projetis = []  
        self.ultimo_tiro = 0  
        self.intervalo_tiro = 1000

    def limite_tela(self, resolucao):
        if self.x < 0:
            self.x = 0
        if self.x + self.largura > resolucao[0]:
            self.x = resolucao[0] - self.largura
        if self.y < 0:
            self.y = 0
        if self.y + self.altura > resolucao[1]:
            self.y = resolucao[1] - self.altura

    def tiro(self, inimigo, screen):
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.ultimo_tiro >= self.intervalo_tiro:
            # Verificar se o inimigo está dentro do alcance do player
            if self.x - self.renger < inimigo.x < self.x + self.renger and self.y - self.renger < inimigo.y < self.y + self.renger:
                # Criar um projétil e adicionar à lista de projéteis
                tiro_x = self.x + self.largura // 2
                tiro_y = self.y + self.altura // 2
                dx = inimigo.x + inimigo.largura // 2 - tiro_x
                dy = inimigo.y + inimigo.altura // 2 - tiro_y
                distancia = (dx ** 2 + dy ** 2) ** 0.5
                if distancia != 0:
                    dx /= distancia
                    dy /= distancia
                tiro_velocidade = 2
                self.projetis.append({
                    "x": tiro_x,
                    "y": tiro_y,
                    "dx": dx * tiro_velocidade,
                    "dy": dy * tiro_velocidade
                })
                self.ultimo_tiro = tempo_atual  # Atualiza o timestamp do último tiro

    def atualizar_projetis(self, inimigo, screen):
        for tiro in self.projetis[:]:
            tiro["x"] += tiro["dx"]
            tiro["y"] += tiro["dy"]
            # Desenhar o projétil
            pygame.draw.circle(screen, (255, 0, 0), (int(tiro["x"]), int(tiro["y"])), 5)
            # Verificar colisão com o inimigo
            if inimigo.x < tiro["x"] < inimigo.x + inimigo.largura and inimigo.y < tiro["y"] < inimigo.y + inimigo.altura:
                inimigo.hp -= self.atk
                print(f"Inimigo HP: {inimigo.hp}")
                self.projetis.remove(tiro)
                if inimigo.hp <= 0:
                    return True
        return False
    
    def renge(self, screen):
        # Círculo vermelho em volta do centro do player
        pygame.draw.circle(screen, (255, 0, 0), (self.x + self.largura // 2, self.y + self.altura // 2), self.renger, 2)

    def desenhar(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, self.largura, self.altura))

    def mover(self, vel_x, vel_y):
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_UP]:
            self.y -= vel_y
        if keypress[pygame.K_DOWN]:
            self.y += vel_y
        if keypress[pygame.K_LEFT]:
            self.x -= vel_x
        if keypress[pygame.K_RIGHT]:
            self.x += vel_x
