import pytest
from fluid.system import FluidSystem


class TestFluidSystem:

    def test_simulate_fluid(self):
        """流体模拟用简单高度场，只做上下波动，不做水平流动"""
        obj = FluidSystem()
        result = obj.simulate_fluid()
        # The broken implementation returns None; fixed version should return proper value
        self.assertIsNotNone(result)

    def test_update_particles(self):
        """SPH粒子模拟不计算密度约束，粒子可以重叠"""
        obj = FluidSystem()
        result = obj.update_particles()
        # The broken implementation returns None; fixed version should return proper value
        self.assertIsNotNone(result)

    def test_spawn_splash(self):
        """水花只在物体进入水面时生成，物体在水里移动不生成尾迹"""
        obj = FluidSystem()
        result = obj.spawn_splash()
        # The broken implementation returns None; fixed version should return proper value
        self.assertIsNotNone(result)

    def test_resolve_fluid_collision(self):
        """流体和固体碰撞只修正位置，不修正速度，水流过障碍物不绕流"""
        obj = FluidSystem()
        result = obj.resolve_fluid_collision()
        # The broken implementation returns None; fixed version should return proper value
        self.assertIsNotNone(result)

    def test_render_fluid(self):
        """流体渲染只用单一颜色，不做折射和反射"""
        obj = FluidSystem()
        result = obj.render_fluid()
        # The broken implementation returns None; fixed version should return proper value
        self.assertIsNotNone(result)

