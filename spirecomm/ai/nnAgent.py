import time
import random
import logging

from spirecomm.spire.game import Game
from spirecomm.spire.character import Intent, PlayerClass
import spirecomm.spire.card
from spirecomm.spire.screen import RestOption
from spirecomm.communication.action import *
from spirecomm.ai.priorities import *
from spirecomm.ai.agent import Agent
from neuralNet.interactor import NeuralNetInteractor

class NnAgent(Agent):

    def __init__(self, chosen_class=PlayerClass.THE_SILENT):
        super().__init__(chosen_class)
        self.interactor = NeuralNetInteractor()

    def change_class(self, chosen_class: PlayerClass):
        pass

    def get_next_combat_action(self):
        return self.interactor.run_combat(self.game)

    def get_card_reward_action(self):
        return super().get_card_reward_action()

    def get_rest_action(self):
        return super().get_rest_action()

    def get_screen_action(self):
        return super().get_screen_action()

    def get_map_choice_action(self):
        return super().get_map_choice_action()