from axion.core import ActionRegistry, Executor, Dispatcher
from axion.arsenal import Action


class TestAction(Action):

    name = "test"

    def execute(self, args=None):
        return f"Received: {args}"


registry = ActionRegistry()

registry.register(
    "test",
    TestAction()
)


executor = Executor(registry)

dispatcher = Dispatcher(executor)


print(
    dispatcher.dispatch(
        "test hello world"
    )
)