class Palabra():
    
    def __init__(self, espanol, ingles):
        self.espanol = espanol
        self.ingles = ingles
        
    def __str__(self):
        return f"{self.espanol} - {self.ingles}"
    
    