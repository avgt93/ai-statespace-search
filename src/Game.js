/* eslint-disable no-unused-vars */
import { GameState } from "./config.js";

export class Action {
	constructor(missionaries, cannibals) {
		this.missionaries = missionaries;
		this.cannibals = cannibals;
	}
}

export const ActionSpace = {
	Cannibal: new Action(0, 1),
	Missionary: new Action(1, 0),
	Cannibal2: new Action(0, 2),
	Missionary2: new Action(2, 0),
	MissionaryCannibal: new Action(1, 1),
};

export class State {
	constructor(missionaries, cannibals, boat) {
		this.missionaries = missionaries;
		this.cannibals = cannibals;
		this.boat = boat;
	}
}

export class Game {
	constructor() {
		this.state = new State(3, 3, true);
	}
	//true = right, false = left
	gameStatus = GameState.Running;
	movePerformed = null;

	checkGameStatus() {
		let otherside = new State(
			3 - this.state.missionaries,
			3 - this.state.cannibals,
			!this.state.boat
		);

		if (
			(this.state.cannibals > this.state.missionaries &&
				this.state.missionaries != 0) ||
			(otherside.cannibals > otherside.missionaries &&
				otherside.missionaries != 0)
		) {
			this.gameStatus = GameState.Failed;
			return;
		}

		if (
			this.state.missionaries < 0 ||
			this.state.cannibals < 0 ||
			this.state.missionaries > 3 ||
			this.state.cannibals > 3
		) {
			this.gameStatus = GameState.Failed;
			return;
		}

		if (
			this.state.missionaries === 0 &&
			this.state.cannibals === 0 &&
			this.state.boat === false
		) {
			this.gameStatus = GameState.Won;
			return;
		}

		this.gameStatus = GameState.Running;
	}

	move(action) {
		let nextState = new State(
			this.state.missionaries,
			this.state.cannibals,
			this.state.boat
		);

		if (this.gameStatus != GameState.Running) {
			return false;
		}

		if (this.state.boat) {
			nextState.missionaries -= action.missionaries;
			nextState.cannibals -= action.cannibals;
			nextState.boat = false;
		} else {
			nextState.missionaries += action.missionaries;
			nextState.cannibals += action.cannibals;
			nextState.boat = true;
		}
		// console.log(nextState.boat);

		if (
			nextState.missionaries < 0 ||
			nextState.cannibals < 0 ||
			nextState.missionaries > 3 ||
			nextState.cannibals > 3
		) {
			this.gameStatus = GameState.Failed;
			return false;
		}

		this.movePerformed = action;
		this.state = nextState;
		this.checkGameStatus();
		return true;
	}

	display() {
		console.log(
			"Missionaries: " +
				this.state.missionaries +
				" Cannibals: " +
				this.state.cannibals +
				" Boat: " +
				this.state.boat
		);
	}
}

let newGame = new Game();
let actions = [
	ActionSpace.Cannibal2,
	ActionSpace.Cannibal,
	ActionSpace.Cannibal,
];

for (let i = 0; i < actions.length; i++) {
	newGame.move(actions[i]);
}

// let goalState = new State(0, 0, false);
// console.log(newGame.gameStatus);
// newGame.display();