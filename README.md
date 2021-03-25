# Ulauncher-Rake

A simple [Ulauncher](https://ulauncher.io/) extension which runs a [Rake](https://github.com/ruby/rake) command in a terminal.

The default command uses `gnome-terminal` and keeps the terminal open after the command completes, however this behavior can be overridden.

# Instructions / Example

1. Install [this extension](https://github.com/sa-0001/ulauncher-rake)
1. Create a Rakefile in your home directory (`~/Rakefile`)
1. Create a task:
	```ruby
	task 'hello', [:name] do |task, args|
		sh %(echo "Hello, #{args.name}!")
	end
	```
1. Open Ulauncher
1. Type the following command:
	```bash
	rake hello[World]
	```
1. The Rake command `hello[World]` is run in a terminal (which stays open after the command completes)
