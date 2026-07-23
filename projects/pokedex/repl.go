package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type cliCommand struct {
	name string
	description string
	callback func() error
}

func getCommands() map[string]cliCommand {
	return map[string]cliCommand {
		"help": {
			name: "help",
			description: "Displays a help message",
			callback: commandHelp,
		},
		"exit": {
			name: "exit",
			description: "Exit the Pokedex",
			callback: commandExit,
		},
	}
}

func startRepl() {
	scanner := bufio.NewScanner(os.Stdin)
	commands := getCommands()

	for {
		fmt.Print("Pokedex > ")
		if !scanner.Scan() {
			break
		}
		input := scanner.Text()
		words := cleanInput(input)

		if len(words) == 0 {
			continue
		}
		commandName := words[0]
		command, exists := commands[commandName]

		if exists {
			err := command.callback()
			if err != nil {
				fmt.Println(err)
			}
		} else {
			fmt.Println("Unknown command")
		}
	}
}

func cleanInput(text string) []string {
	lowered := strings.ToLower(text)
	words := strings.Fields(lowered)
	return words
}