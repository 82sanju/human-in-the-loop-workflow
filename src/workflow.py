from src.agent import Agent
from src.tasks.email_task import EmailTask
from src.human_gate import HumanGate
from src.utils.file_ops import save_pending, move_to

def run_workflow():
    print("=== HITL WORKFLOW STARTED ===")

    agent = Agent()

    # Example task - generate an onboarding email
    task = EmailTask(employee_name="Rahul")

    output = task.run(agent)
    print("[AI] Generated email:\n", output["generated_email"])

    # Store for human approval
    task_id, filepath = save_pending(output)
    print(f"[HITL] Task stored for human review: {filepath}")

    # Wait for human approval
    decision, data = HumanGate.wait_for_decision(task_id)

    if decision == "approved":
        move_to("approved", task_id, data)
        print("[WORKFLOW] Email approved. Proceeding with next steps.")
    else:
        move_to("rejected", task_id, data)
        print("[WORKFLOW] Email rejected. Stopping workflow.")

    print("=== WORKFLOW COMPLETE ===")
