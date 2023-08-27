/* eslint-disable no-unused-vars */
import { State, Action, ActionSpace, Game } from "./Game.js";
import { GameState } from "./config.js";

export class SearchTree {
	constructor(nodeState) {
		this.data = nodeState;
		this.children = [];
		this.terminate = false;
		this.parent = null;
	}
	addChild(childNode) {
		this.children.push(childNode);
	}

	getAllStates() {
		let states = [];
		let tempGame = Object.assign(
			Object.create(Object.getPrototypeOf(this.data)),
			this.data
		);
		let canMove = tempGame.move(ActionSpace.Missionary);
		if (canMove) {
			let tempNode = new SearchTree(tempGame);
			tempNode.parent = this;
			this.addChild(tempNode);
			states.push(tempNode);
		}

		tempGame = Object.assign(
			Object.create(Object.getPrototypeOf(this.data)),
			this.data
		);
		canMove = tempGame.move(ActionSpace.Cannibal);
		if (canMove) {
			let tempNode = new SearchTree(tempGame);
			states.push(tempNode);
		}

		tempGame = Object.assign(
			Object.create(Object.getPrototypeOf(this.data)),
			this.data
		);
		canMove = tempGame.move(ActionSpace.Missionary2);
		if (canMove) {
			let tempNode = new SearchTree(tempGame);

			states.push(tempNode);
		}

		tempGame = Object.assign(
			Object.create(Object.getPrototypeOf(this.data)),
			this.data
		);
		canMove = tempGame.move(ActionSpace.Cannibal2);
		if (canMove) {
			let tempNode = new SearchTree(tempGame);

			states.push(tempNode);
		}

		tempGame = Object.assign(
			Object.create(Object.getPrototypeOf(this.data)),
			this.data
		);
		canMove = tempGame.move(ActionSpace.MissionaryCannibal);
		if (canMove) {
			let tempNode = new SearchTree(tempGame);
			states.push(tempNode);
		}

		return states;
	}

	isEqual(other) {
		if (other instanceof SearchTree) {
			if (
				this.data.state.Missionary === other.data.state.Missionary &&
				this.data.state.Cannibal === other.data.state.Cannibal &&
				this.data.state.Boat === other.data.state.Boat
			) {
				return true;
			} else {
				return false;
			}
		}
		return false;
	}

	searchState() {
		let queue = [];
		let visited = [];
		let newGame = new Game();
		let initialNode = new SearchTree(newGame);
		queue.push(initialNode);
		while (queue.length > 0) {
			let currentState = queue.shift();
			if (visited.includes(currentState)) {
				continue;
			}
			visited.push(currentState);
			if (currentState.data.gameStatus === GameState.Won) {
				return currentState;
			}
			if (currentState.data.gameStatus === GameState.Running) {
				let newStates = currentState.getAllStates();
				for (let i = 0; i < newStates.length; i++) {
					currentState.addChild(newStates[i]);
					newStates[i].parent = currentState;
					if (!visited.includes(newStates[i])) {
						queue.push(newStates[i]);
					}
				}
			}
		}
	}
	display() {
		console.log(this.data);
	}
}

let newGame = new Game();
let searchTree = new SearchTree().searchState();
console.log(searchTree.data);
let temp = searchTree;
while (temp.parent != null) {
	temp.display();
	temp = temp.parent;
}
