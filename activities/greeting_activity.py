from temporalio import activity

@activity.defn
async def generate_greeting(name: str) -> str:
    return f"Hello, {name} from Temporal Activities!"
