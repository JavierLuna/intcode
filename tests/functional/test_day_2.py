from typing import List

import pytest

from intcode import IntCodeMachine


@pytest.fixture
def day_2_input() -> List[int]:
    str_code = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,6,27,1,9,27,31,1,31,10,35,2,13,35,39,1,39,10,43,1,43,9,47,1,47,13,51,1,51,13,55,2,55,6,59,1,59,5,63,2,10,63,67,1,67,9,71,1,71,13,75,1,6,75,79,1,10,79,83,2,9,83,87,1,87,5,91,2,91,9,95,1,6,95,99,1,99,5,103,2,103,10,107,1,107,6,111,2,9,111,115,2,9,115,119,2,13,119,123,1,123,9,127,1,5,127,131,1,131,2,135,1,135,6,0,99,2,0,14,0"  # noqa: E501
    return [int(i.strip()) for i in str_code.split(',') if i.strip()]


@pytest.mark.parametrize("program,position,result", [("1,0,0,0,99", 0, 2),
                                                     ("2,3,0,3,99", -2, 6),
                                                     ("2,4,4,5,99,0", -1, 9801),
                                                     ("1,1,1,4,99,5,6,0,99", 0, 30)])
def test_day_2_previous_tests(program, position, result):
    machine = IntCodeMachine(program)
    machine.run()
    assert machine.machine_state.registries[position] == result


def test_day_2_part_1(day_2_input):
    day_2_input[1] = 12
    day_2_input[2] = 2
    machine = IntCodeMachine(day_2_input)
    machine.run()
    assert machine.machine_state.registries[0] == 4138658


def test_day2_part_2(day_2_input):
    day_2_input[1] = 72
    day_2_input[2] = 64
    machine = IntCodeMachine(day_2_input)
    machine.run()
    assert machine.machine_state.registries[0] == 19690720
