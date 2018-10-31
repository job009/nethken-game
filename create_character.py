def setupGUI(self):
    self.pack(fill=BOTH, expand=1)
    Game.player_input = Entry(self, bg="white")
    Game.player_input.bind("<Return>", self.process)
    Game.player_input.pack(side=BOTTOM, fill=X)
    Game.player_input.focus()

    text_frame = Frame(self, width=WIDTH / 2)
    Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
    Game.text.pack(fill=Y, expand=1)
    text_frame.pack(side=RIGHT, fill=Y)
    text_frame.pack_propagate(False)