import PvzRH_node as pvn
from PvzRH_node import PlantType

# Configure the output folder and name
pvn.Config(name="sample level")

# Configure the grouping level (0 by default)
pvn.settings.group_level = 1

def Give_sun_based_on_wave():
    board = pvn.Board
    amount = 100 * board.Wave
    board.Sun += amount
    pvn.GameAPP.display_text("Gave ", amount, " sun!")

def main():
    with pvn.Trigger.OnPlantClicked() as plant:
        with pvn.If(plant.plantType == PlantType.SunFlower):
            Give_sun_based_on_wave()

pvn.add_graph(main)