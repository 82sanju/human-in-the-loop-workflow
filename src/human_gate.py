import time
from .utils.file_ops import load_if_exists

class HumanGate:

    @staticmethod
    def wait_for_decision(task_id):
        print(f"[HITL] Waiting for human input on task: {task_id}")

        while True:
            approved = load_if_exists("approved", task_id)
            rejected = load_if_exists("rejected", task_id)

            if approved:
                print("[HITL] Human APPROVED the task.")
                return "approved", approved

            if rejected:
                print("[HITL] Human REJECTED the task.")
                return "rejected", rejected

            time.sleep(2)  # don’t spam CPU like a fool
