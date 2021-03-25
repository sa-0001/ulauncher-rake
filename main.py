import os
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

##======================================================================================================================

class RunExtension(Extension):
	def __init__(self):
		super(RunExtension, self).__init__()
		self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
		self.subscribe(ItemEnterEvent, ItemEnterEventListener())

class KeywordQueryEventListener(EventListener):
	def on_event(self, event, extension):
		task_name = event.get_argument()
		items = [
			ExtensionResultItem(
				icon="images/icon.png",
				name="Run a Rake task in a terminal",
				description="" if not task_name else f"Run the Rake task \"{task_name}\" in a terminal",
				on_enter=ExtensionCustomAction(task_name),
			),
		]
		return RenderResultListAction(items)

class ItemEnterEventListener(EventListener):
	def on_event(self, event, extension):
		task_name = event.get_data() or ""
		command = extension.preferences["command"]
		command = command.replace("$TASK", task_name)
		os.system(command)
		return RenderResultListAction([])

##------------------------------------------------------------------------------

if __name__ == "__main__":
	RunExtension().run()
