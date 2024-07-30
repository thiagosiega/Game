import pygame

class Player:
    def __init__(self, x, y, tiros):
        self.x = x
        self.y = y
        self.hp = 100
        self.mp = 100
        self.atk = 10
        self.defense = 5
        self.altura = 50
        self.largura = 50
        self.renger = 100
        self.tiros = tiros
        self.projetis = []
        self.ultimo_tiro = 0
        self.intervalo_tiro = 100

    def limite_tela(self, resolucao):
        if self.x < 0:
            self.x = 0
        if self.x + self.largura > resolucao[0]:
            self.x = resolucao[0] - self.largura
        if self.y < 0:
            self.y = 0
        if self.y + self.altura > resolucao[1]:
            self.y = resolucao[1] - self.altura

    def tiro(self, inimigos, screen):
        tempo_atual = pygame.time.get_ticks()
        
        if tempo_atual - self.ultimo_tiro >= self.intervalo_tiro:
            projeteis_a_remover = []
            inimigos_a_remover = []

            for tiro in self.projetis[:]:
                if tiro["x"] < 0 or tiro["x"] > screen.get_width() or tiro["y"] < 0 or tiro["y"] > screen.get_height():
                    projeteis_a_remover.append(tiro)

            for tiro in projeteis_a_remover:
                self.projetis.remove(tiro)

            if len(self.projetis) < self.tiros:
                inimigos_no_alcance = [inimigo for inimigo in inimigos if self.x - self.renger < inimigo.x < self.x + self.renger and self.y - self.renger < inimigo.y < self.y + self.renger]

                if inimigos_no_alcance:
                    inimigo = inimigos_no_alcance[0]
                    tiro_x = self.x + self.largura // 2
                    tiro_y = self.y + self.altura // 2
                    dx = inimigo.x + inimigo.largura // 2 - tiro_x
                    dy = inimigo.y + inimigo.altura // 2 - tiro_y
                    distancia = (dx ** 2 + dy ** 2) ** 0.5
                    if distancia != 0:
                        dx /= distancia
                        dy /= distancia
                    tiro_velocidade = 20
                    self.projetis.append({
                        "x": tiro_x,
                        "y": tiro_y,
                        "dx": dx * tiro_velocidade,
                        "dy": dy * tiro_velocidade
                    })

                    inimigo.hp -= self.atk
                    if inimigo.hp <= 0:
                        inimigos_a_remover.append(inimigo)

                for inimigo in inimigos_a_remover:
                    inimigos.remove(inimigo)

            self.ultimo_tiro = tempo_atual

    def atualizar_projetis(self, inimigos, screen):
        projeteis_a_remover = []
        inimigos_a_remover = []

        for tiro in self.projetis[:]:
            tiro["x"] += tiro["dx"]
            tiro["y"] += tiro["dy"]
            pygame.draw.circle(screen, (255, 0, 0), (int(tiro["x"]), int(tiro["y"])), 5)

            for inimigo in inimigos:
                if inimigo.x < tiro["x"] < inimigo.x + inimigo.largura and inimigo.y < tiro["y"] < inimigo.y + inimigo.altura:
                    inimigo.hp -= self.atk
                    projeteis_a_remover.append(tiro)

                    if inimigo.hp <= 0:
                        inimigos_a_remover.append(inimigo)

        for tiro in projeteis_a_remover:
            if tiro in self.projetis:
                self.projetis.remove(tiro)

        for inimigo in inimigos_a_remover:
            if inimigo in inimigos:
                inimigos.remove(inimigo)

        return bool(inimigos_a_remover)

    def renge(self, screen):
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
