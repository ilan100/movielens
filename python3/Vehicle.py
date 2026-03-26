import math
import datetime
from enum import Enum

class MotorcycleType(Enum):
    CLASSIC = "Classic"
    CHOPPER = "Chopper"
    SPORT = "Sport"

class DrivetrainType(Enum):
    CHAIN = "Chain"
    BELT = "BELT"
    SHAFT = "Shaft"

class Vehicle():
    def __init__(self, id: int, volume: float,
                 horse_power: float, color: str, accel: float):
        self.id = id
        self.engine_volume = 0
        self.engine_horse_power = 0
        self.color = color
        self.accel = accel
    def get_info(self) -> dict:
        return {
            "id": self.id,
            "engine volume": self.engine_volume,
            "horse power": self.engine_horse_power,
            "color": self.color,
            "accel": self.accel,
        }

class Car(Vehicle):
    def __init__(self, id: int, volume: float, horse_power: float,
                 color: str, accel: float, num_doors: int, num_airbags: int):
        super().__init__(id, volume, horse_power, color, accel)
        self.num_doors = num_doors
        self.num_airbags = num_airbags
    def get_info(self) -> dict:
        info = super().get_info()  # get base data
        info.update({
            "num doors": self.num_doors,
            "num airbags": self.num_airbags
        })
        return info

class Motorcycle(Vehicle):
    def __init__(self, id: int, volume: float, horse_power: float,
                 color: str, accel: float, type: MotorcycleType, drivetrain: DrivetrainType):
        super().__init__(id, volume, horse_power, color, accel)
        self.type = type
        self.drivetrain = drivetrain
    def get_info(self) -> dict:
        info = super().get_info()  # get base data
        info.update({
            "type": self.type,
            "drivetrain": self.drivetrain
        })
        return info
#------------------------------------------------------------------------------------

if __name__ == '__main__':
    pass
