/* eslint-disable react-hooks/rules-of-hooks */
/* eslint-disable react/prop-types */
/* eslint-disable no-unused-vars */
import { useState } from "react";
import { Game } from "../src/game/Game.js";
import { State } from "../src/game/Game.js";
import { parse, stringify } from "flatted";
import { searchResults } from "../src/game/Search.js";
import Node from "./assets/Node.jsx";
import "./styles/App.css";
import { GameState } from "./game/config.js";

let data = parse(stringify(searchResults));
console.log(data);

const useDataParser = (d) => {
	const [data, setData] = useState({
		gameStatus: d.data.gameStatus,
		movePerformed: d.data.movePerformed
			? `Missionaries:${d.data.movePerformed.missionaries}, Cannibals:${d.data.movePerformed.cannibals}`
			: "No move performed",
		state: d.data.state
			? `Missionaries:${d.data.state.missionaries},Cannibals:${d.data.state.cannibals},Boat:${d.data.state.boat}`
			: "No state",
	});

	// console.log(d);
	return data;
};
const App = () => {
	return (
		<div className="App">
			<h1>Missionaries-Cannibal Game Search Tree</h1>
			<Node node={data} />
		</div>
	);
};

export default App;
