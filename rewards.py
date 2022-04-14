import numpy as np
from rlgym.utils import RewardFunction
from rlgym.utils import common_values
from rlgym.utils.gamestates import GameState, PlayerData

ball_max_height = common_values.CEILING_Z - common_values.BALL_RADIUS

class JumpTouchReward(RewardFunction):
    def __init__(self, min_height=common_values.BALL_RADIUS, exp=1):
        self.min_height = min_height
        self.exp = exp
        self.div = common_values.CEILING_Z ** self.exp

    def reset(self, initial_state: GameState):
        pass

    def get_reward(
        self, player: PlayerData, state: GameState, previous_action: np.ndarray
    ) -> float:
        if player.ball_touched and not player.on_ground and state.ball.position[2] >= self.min_height:
            reward = (((state.ball.position[2] - common_values.BALL_RADIUS) ** self.exp) / self.div)
            if reward > .05:
                print(f"Aerial hit! % from ceiling: {round(reward*100,2)}%")
            return reward

        return 0

class WallTouchReward(RewardFunction):
    def __init__(self, min_height=common_values.BALL_RADIUS, exp=1):
        self.min_height = min_height
        self.exp = exp
        self.div = common_values.CEILING_Z ** self.exp

    def reset(self, initial_state: GameState):
        pass

    def get_reward(
        self, player: PlayerData, state: GameState, previous_action: np.ndarray
    ) -> float:
        if player.ball_touched and player.on_ground and state.ball.position[2] >= self.min_height:
            reward = (((state.ball.position[2] - common_values.BALL_RADIUS) ** self.exp) / self.div)
            print(f"Wall hit! % from ceiling: {round(reward*100,2)}%")
            return reward

        return 0