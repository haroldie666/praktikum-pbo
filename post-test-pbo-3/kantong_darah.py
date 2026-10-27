class KantongDarah:
    def __init__(self, id_kantong, gol_darah, volume):
        self.id_kantong = id_kantong
        self.gol_darah = gol_darah
        self.volume = volume

    def __str__(self): 
        # Operator Overloading
        return f"[{self.id_kantong}] Darah {self.gol_darah} ({self.volume} ml)"