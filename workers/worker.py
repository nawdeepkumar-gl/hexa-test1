import asyncio
from temporalio.client import Client
from temporalio.worker import Worker

from workflows.hello_workflow import HelloWorkflow
from activities.greeting_activity import generate_greeting

async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="hello-task-queue",
        workflows=[HelloWorkflow],
        activities=[generate_greeting],
    )

    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
