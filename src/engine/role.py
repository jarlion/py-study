from engine.view import View


class Role:

    def __init__(self,
                 name: str,
                 description: str,
                 stats: dict[str, int],
                 speed: tuple[int, int] = [5, 0]):
        self.name = name
        self.description = description
        self.stats = stats
        self.speed = speed

    def attack(self, target):
        pass
        # 攻击目标角色，返回攻击结果，包括是否成功、伤害值等

    def defend(self, damage):
        pass
        # 防御受到的伤害，返回剩余生命值

    def use_item(self, item):
        pass
        # 使用物品，返回使用结果，包括是否成功、效果等

    def use_skill(self, skill):
        pass
        # 使用技能，返回使用结果，包括是否成功、效果等

    def get_status(self):
        pass
        # 获取角色当前状态，包括生命值、能量值、状态等

    def set_status(self, status):
        pass
        # 设置角色当前状态，包括生命值、能量值、状态等

    def get_stats(self):
        pass
        # 获取角色当前属性，包括攻击力、防御力、速度等

    def set_stats(self, stats):
        pass
        # 设置角色当前属性，包括攻击力、防御力、速度等

    def walk(self, direction):
        pass
        # 移动角色，返回移动结果，包括是否成功、位置等

    def run(self, direction):
        pass
        # 奔跑角色，返回奔跑结果，包括是否成功、位置等

    def jump(self, direction):
        pass
        # 跳跃角色，返回跳跃结果，包括是否成功、位置等

    def fall(self, direction):
        pass
        # 下落角色，返回下落结果，包括是否成功、位置等

    def climb(self, direction):
        pass
        # 爬墙角色，返回爬墙结果，包括是否成功、位置等

    def swim(self, direction):
        pass
        # 游泳角色，返回游泳结果，包括是否成功、位置等

    def fly(self, direction):
        pass

    def get_body(self):
        return self.body


class Player(Role):

    def __init__(self, name: str, description: str, stats: dict,
                 body: View) -> View:
        super().__init__(name, description, stats)
        self.body = body


class Monster(Role):

    def __init__(self, name: str, description: str, stats: dict):
        super().__init__(name, description, stats)


class NPC(Role):

    def __init__(self, name: str, description: str, stats: dict):
        super().__init__(name, description, stats)


class Boss(Role):

    def __init__(self, name: str, description: str, stats: dict):
        super().__init__(name, description, stats)
