"""
pairwise-fluid-system - FluidSystem

This module contains a deliberately broken implementation.
Fix all bugs so that tests pass.
"""


class FluidSystem:
    def __init__(self):
        self.state = {}

    def simulate_fluid(self, *args, **kwargs):
        """BUG: 流体模拟用简单高度场，只做上下波动，不做水平流动"""
        # Intentionally broken implementation
        return None

    def update_particles(self, *args, **kwargs):
        """BUG: SPH粒子模拟不计算密度约束，粒子可以重叠"""
        # Intentionally broken implementation
        return None

    def spawn_splash(self, *args, **kwargs):
        """BUG: 水花只在物体进入水面时生成，物体在水里移动不生成尾迹"""
        # Intentionally broken implementation
        return None

    def resolve_fluid_collision(self, *args, **kwargs):
        """BUG: 流体和固体碰撞只修正位置，不修正速度，水流过障碍物不绕流"""
        # Intentionally broken implementation
        return None

    def render_fluid(self, *args, **kwargs):
        """BUG: 流体渲染只用单一颜色，不做折射和反射"""
        # Intentionally broken implementation
        return None

