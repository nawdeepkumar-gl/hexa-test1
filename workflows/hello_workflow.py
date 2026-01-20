from temporalio import workflow
from datetime import timedelta

# Import activity safely
with workflow.unsafe.imports_passed_through():
    from activities.greeting_activity import generate_greeting

@workflow.defn
class HelloWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        result = await workflow.execute_activity(
            generate_greeting,
            name,
            start_to_close_timeout=timedelta(seconds=10),
        )
        return result
