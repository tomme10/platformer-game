
class object:
    drawOrder = 0
    updateOrder = 0

    collisions = False

    def reset(self):pass

    def update(self,dtime,objects):pass
    
    def draw(self,root):pass

    def collision(self,rect):
        return False