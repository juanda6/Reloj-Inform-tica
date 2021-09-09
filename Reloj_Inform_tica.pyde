vertical_position = 0
def setup ():
    size (250, 500)
    
    
def draw ():
        global vertical_position 
        background (255)
        circle (50, vertical_position, 50)
        fill (18, 3, 255)
        if vertical_position > height :
           vertical_position = 0
        else:
           vertical_position = map (second(), 0, 59, 0, height) 
           
        circle (width / 2, vertical_position, 50)
        fill (255, 3, 3)
        if vertical_position > height :
           vertical_position = 0
        else : 
            vertical_position = map (hour(), 0, 23, 0, height)
            
        circle (200, vertical_position, 50)
        fill (246, 255, 3)
        if vertical_position > height :
           vertical_position = 0
        else : 
           vertical_position= map (minute(), 0, 59, 0, height)
