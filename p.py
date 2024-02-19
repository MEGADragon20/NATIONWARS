                if self.owner == playeronturn:
                        if d[a+2,b+1].typ in self.feldtyp: 
                            if d[a+2,b+1].entities != [] and d[a+2,b+1].entities[0].owner != self.owner:   
                                overlays.append(Overlay(d[a+2,b+1], "data/icons/overlayred.png", self))        
                            elif d[a+2,b+1].entities != [] and d[a+2,b+1].entities[0].owner == self.owner:   
                                pass
                            else:
                                overlays.append(Overlay(d[a+2,b+1], "data/icons/overlay.png", self))        