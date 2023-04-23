from unit_tools.behavior import Behavior
from unit_tools.team_manager import TeamManager
from auxiliary_tools.message_manager import MessageManager


class Preselection(Behavior):
    def __init__(self):
        super().__init__()
        self.surface = None
        self.flag.add_flag("preselection")

    def update_60(self):
        if self.unit.state_label.contain_flag("hidden") or self.unit.state_label.contain_flag("in_fog"):
            return

        unit_rect = self.unit.c_rect

        if TeamManager.is_player(self.unit.team):
            color = (100, 230, 100)
        elif TeamManager.is_alliance(TeamManager.player_team, self.unit.team) is False:
            color = (200, 100, 100)
        else:
            color = (255, 255, 255)

        center = unit_rect.left + unit_rect.width / 2
        MessageManager.send_message("ellipse_draw", [center, self.unit.volume * 1.2, color, 1])
