class EmailTask:

    def __init__(self, employee_name):
        self.employee_name = employee_name

    def run(self, agent):
        """AI generates output for human approval."""
        email_text = agent.generate_email(self.employee_name)

        return {
            "task_type": "email_generation",
            "employee_name": self.employee_name,
            "generated_email": email_text
        }
