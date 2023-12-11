from abc import ABC, abstractmethod


class Robot:
    def __init__(self):
        self.head = None
        self.arms = None
        self.leg = None
        self.battery = None

class RobotBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_head(self):
        pass

    @abstractmethod
    def build_arms(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass 

    @abstractmethod
    def build_battery(self):
        pass


class AndroidBuilder(RobotBuilder):
    def __init__(self):
        self.robot = Robot()
        self.reset()

    def reset(self):
        self.robot = Robot()

    def build_head(self):
        self.robot.head = 'Android head'

    def build_arms(self):
        self.robot.arms = 'Android arms'

    def build_leg(self):
        self.robot.leg = 'Android leg'

    def build_battery(self):
        self.robot.battery = 'Android battery'

    def get_robot(self):
        return self.robot
    

class HumanoidBuilder(RobotBuilder):
    def __init__(self):
        self.robot = Robot()
        self.reset()

    def reset(self):
        self.robot = Robot()

    def build_head(self):
        self.robot.head = 'Humanoid head'

    def build_arms(self):
        self.robot.arms = 'Humanoid arms'

    def build_leg(self):
        self.robot.leg = 'Humanoid leg'

    def build_battery(self):
        self.robot.battery = 'Humanoid battery'

    def get_robot(self):
        return self.robot
    

class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder
    
    def build_android(self):
        self.builder.build_head()
        self.builder.build_arms()
        self.builder.build_leg()
        self.builder.build_battery()
        return self.builder.get_robot()
    
    def build_humanoid(self):
        self.builder.build_head()
        self.builder.build_arms()
        self.builder.build_leg()
        self.builder.build_battery()
        return self.builder.get_robot()
    

if __name__ == '__main__':
    director = Director()
    android_builder = AndroidBuilder()
    humanoid_builder = HumanoidBuilder()
    director.set_builder(android_builder)
    android = director.build_android()
    print('Android Robot Components:')
    print(android.head)
    print(android.arms)
    print(android.leg)
    print(android.battery)
    director.set_builder(humanoid_builder)
    humanoid = director.build_humanoid()
    print('-------------------------')
    print('Humanoid Robot Components:')
    print(humanoid.head)
    print(humanoid.arms)
    print(humanoid.leg)
    print(humanoid.battery)