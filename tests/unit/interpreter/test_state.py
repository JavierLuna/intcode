from typing import List

import pytest

from intcode.interpreter.state import MachineState, AccessMode


@pytest.fixture
def mocked_program() -> List[int]:
    return [1, 2, 3]


@pytest.fixture
def mocked_machine_state(mocked_program) -> MachineState:
    return MachineState(mocked_program)


def test_get_registry_value_position(mocked_program, mocked_machine_state):
    position = 0
    assert mocked_machine_state.get_registry_value(AccessMode.POSITION, position) == mocked_program[
        position]


def test_get_registry_value_non_existing_position_zero(mocked_program, mocked_machine_state):
    position = len(mocked_program)
    assert mocked_machine_state.get_registry_value(AccessMode.POSITION, position) == 0


def test_get_registry_value_immediate(mocked_program, mocked_machine_state):
    position = 0
    assert mocked_machine_state.get_registry_value(AccessMode.IMMEDIATE, position) == position


def test_get_registry_value_relative():
    program = [1, 2, 3]
    position = 0
    relative_base = 1
    machine_state = MachineState(program, relative_base=relative_base)
    assert machine_state.get_registry_value(AccessMode.RELATIVE, position) == program[
        machine_state.relative_base + position]


@pytest.mark.parametrize("delta", [-1, 0, 1])
def test_shift_relative_base(delta):
    initial_relative_base = 0
    machine_state = MachineState([], relative_base=initial_relative_base)
    machine_state.shift_relative_base(delta)
    assert machine_state.relative_base == delta
