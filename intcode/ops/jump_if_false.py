from intcode.interfaces.base_op import BaseOp
from intcode.interpreter.state import MachineState


class JumpIfFalseOp(BaseOp):
    n_params = 2
    special_parameters = ['machine_state']

    @classmethod
    def execute(cls, a: int, destination: int, machine_state: MachineState) -> None:
        if not a:
            machine_state.machine_pointer = destination