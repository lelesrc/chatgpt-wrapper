from chatgpt_wrapper.core.plugin import Plugin
import chatgpt_wrapper.core.util as util

class Test(Plugin):

    def setup(self):
        self.log.info(f"This is the test plugin, running with backend: {self.backend.name}")

    def get_shell_completions(self, _base_shell_completions):
        commands = {}
        commands[util.command_with_leader('test')] = util.list_to_completion_hash(['one', 'two', 'three'])
        return commands

    async def do_test(self, arg):
        """
        Test plugin command

        Examples:
            {COMMAND} one
        """
        if not arg:
            return False, arg, "Argument is required"
        return True, arg, f"Test: {arg}"
