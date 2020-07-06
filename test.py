from text_rpg_maker import *  
game = Game('test')
ree = game.ask_choices("How are you?", ["Good!", "Meh...", "FeelsBadMan"])
game.say(ree)
